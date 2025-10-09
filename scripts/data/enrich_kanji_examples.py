#!/usr/bin/env python3
"""Normalize JLPT kanji datasets by injecting high-quality example entries.

The script replaces placeholder examples in the N3, N2, and N1 datasets with
consistent five-layer examples that mirror the structure used for N5/N4.
It relies on the public kanjiapi.dev endpoint to source common vocabulary
containing each kanji and caches responses locally to avoid repeated requests.
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional

DATA_DIR = Path("src/data/kanji")
CACHE_DIR = Path("tmp/kanjiapi_cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

API_WORDS_ENDPOINT = "https://kanjiapi.dev/v1/words/{kanji}"

# Templates used to generate natural-feeling sentences. Each template contains
# four layers which will be formatted with word/meaning/romaji values.
SENTENCE_TEMPLATES = [
    {
        "ja": "「{word}」という言葉は日常生活でよく使われます。",
        "romaji": "\"{reading_romaji}\" to iu kotoba wa nichijou seikatsu de yoku tsukawaremasu.",
        "en": "The expression '{word}' ({meaning}) is often used in daily life.",
        "uz": "'{word}' ({meaning}) ifodasi kundalik hayotda tez-tez ishlatiladi.",
    },
    {
        "ja": "先生が{word}について説明しました。",
        "romaji": "Sensei ga {reading_romaji} ni tsuite setsumei shimashita.",
        "en": "The teacher explained '{word}' ({meaning}) to us.",
        "uz": "O'qituvchi '{word}' ({meaning}) haqida tushuntirdi.",
    },
    {
        "ja": "{word}のおかげで助かりました。",
        "romaji": "{reading_romaji} no okage de tasukarimashita.",
        "en": "Thanks to '{word}' ({meaning}), I was helped.",
        "uz": "'{word}' ({meaning}) tufayli yordam oldim.",
    },
    {
        "ja": "毎日{word}について考えています。",
        "romaji": "Mainichi {reading_romaji} ni tsuite kangaete imasu.",
        "en": "I reflect on '{word}' ({meaning}) every day.",
        "uz": "Har kuni '{word}' ({meaning}) haqida o'ylab ko'raman.",
    },
    {
        "ja": "{word}の重要性を感じています。",
        "romaji": "{reading_romaji} no juuyousei o kanjite imasu.",
        "en": "I feel how important '{word}' ({meaning}) is.",
        "uz": "'{word}' ({meaning}) ning ahamiyatini his qilaman.",
    },
]

# Mapping tables to convert kana readings to romaji without external deps.
COMBINATIONS = {
    "きゃ": "kya",
    "きゅ": "kyu",
    "きょ": "kyo",
    "ぎゃ": "gya",
    "ぎゅ": "gyu",
    "ぎょ": "gyo",
    "しゃ": "sha",
    "しゅ": "shu",
    "しょ": "sho",
    "じゃ": "ja",
    "じゅ": "ju",
    "じょ": "jo",
    "ちゃ": "cha",
    "ちゅ": "chu",
    "ちょ": "cho",
    "にゃ": "nya",
    "にゅ": "nyu",
    "にょ": "nyo",
    "ひゃ": "hya",
    "ひゅ": "hyu",
    "ひょ": "hyo",
    "びゃ": "bya",
    "びゅ": "byu",
    "びょ": "byo",
    "ぴゃ": "pya",
    "ぴゅ": "pyu",
    "ぴょ": "pyo",
    "みゃ": "mya",
    "みゅ": "myu",
    "みょ": "myo",
    "りゃ": "rya",
    "りゅ": "ryu",
    "りょ": "ryo",
    "う゛ぁ": "va",
    "う゛ぃ": "vi",
    "う゛ぇ": "ve",
    "う゛ぉ": "vo",
    "ふぁ": "fa",
    "ふぃ": "fi",
    "ふぇ": "fe",
    "ふぉ": "fo",
    "てぃ": "ti",
    "でぃ": "di",
    "とぅ": "tu",
    "どぅ": "du",
    "しぇ": "she",
    "じぇ": "je",
    "ちぇ": "che",
    "つぁ": "tsa",
    "つぃ": "tsi",
    "つぇ": "tse",
    "つぉ": "tso",
}

BASIC_KANA = {
    "あ": "a",
    "い": "i",
    "う": "u",
    "え": "e",
    "お": "o",
    "か": "ka",
    "き": "ki",
    "く": "ku",
    "け": "ke",
    "こ": "ko",
    "さ": "sa",
    "し": "shi",
    "す": "su",
    "せ": "se",
    "そ": "so",
    "た": "ta",
    "ち": "chi",
    "つ": "tsu",
    "て": "te",
    "と": "to",
    "な": "na",
    "に": "ni",
    "ぬ": "nu",
    "ね": "ne",
    "の": "no",
    "は": "ha",
    "ひ": "hi",
    "ふ": "fu",
    "へ": "he",
    "ほ": "ho",
    "ま": "ma",
    "み": "mi",
    "む": "mu",
    "め": "me",
    "も": "mo",
    "や": "ya",
    "ゆ": "yu",
    "よ": "yo",
    "ら": "ra",
    "り": "ri",
    "る": "ru",
    "れ": "re",
    "ろ": "ro",
    "わ": "wa",
    "を": "o",
    "ん": "n",
    "が": "ga",
    "ぎ": "gi",
    "ぐ": "gu",
    "げ": "ge",
    "ご": "go",
    "ざ": "za",
    "じ": "ji",
    "ず": "zu",
    "ぜ": "ze",
    "ぞ": "zo",
    "だ": "da",
    "ぢ": "ji",
    "づ": "zu",
    "で": "de",
    "ど": "do",
    "ば": "ba",
    "び": "bi",
    "ぶ": "bu",
    "べ": "be",
    "ぼ": "bo",
    "ぱ": "pa",
    "ぴ": "pi",
    "ぷ": "pu",
    "ぺ": "pe",
    "ぽ": "po",
    "ぁ": "a",
    "ぃ": "i",
    "ぅ": "u",
    "ぇ": "e",
    "ぉ": "o",
    "ゎ": "wa",
    "ゔ": "vu",
    "ー": "-",
}

VOWEL_HIRAGANA = {"あ", "い", "う", "え", "お", "や", "ゆ", "よ"}


def katakana_to_hiragana(text: str) -> str:
    result = []
    for ch in text:
        if "ァ" <= ch <= "ン":
            result.append(chr(ord(ch) - 0x60))
        elif ch == "ヵ":
            result.append("か")
        elif ch == "ヶ":
            result.append("け")
        else:
            result.append(ch)
    return "".join(result)


def kana_to_romaji(text: str) -> str:
    if not text:
        return ""
    text = katakana_to_hiragana(text)
    result = []
    i = 0
    while i < len(text):
        ch = text[i]

        # Handle sokuon (small tsu) doubling the next consonant.
        if ch == "っ":
            if i + 1 < len(text):
                next_char = text[i + 1 : i + 3]
                romaji = None
                # Check combinations first
                for length in (2, 1):
                    segment = next_char[:length]
                    if segment in COMBINATIONS:
                        romaji = COMBINATIONS[segment]
                        break
                    if segment and segment in BASIC_KANA:
                        romaji = BASIC_KANA[segment]
                        break
                if romaji:
                    result.append(romaji[0])
            i += 1
            continue

        # Long vowel mark extend previous vowel
        if ch == "ー":
            if result:
                last = result[-1]
                for vowel in ("a", "i", "u", "e", "o"):
                    if last.endswith(vowel):
                        result[-1] = last + vowel
                        break
            i += 1
            continue

        # Handle digraph combinations
        if i + 1 < len(text):
            pair = text[i : i + 2]
            if pair in COMBINATIONS:
                result.append(COMBINATIONS[pair])
                i += 2
                continue

        if ch in BASIC_KANA:
            romaji = BASIC_KANA[ch]
            # Handle "ん" before vowels/ya: add apostrophe to avoid ambiguity
            if (
                ch == "ん"
                and i + 1 < len(text)
                and text[i + 1] in VOWEL_HIRAGANA
            ):
                romaji = "n'"
            result.append(romaji)
            i += 1
            continue

        # Skip punctuation/spaces gracefully
        if ch in {"・", "　", " "}:
            result.append(" ")
            i += 1
            continue

        result.append(ch)
        i += 1

    return "".join(result)


@dataclass
class Candidate:
    word: str
    reading: str
    meaning: str
    priority_score: int
    raw_priorities: List[str]


def fetch_words(kanji: str) -> List[Dict]:
    cache_file = CACHE_DIR / f"{kanji}.words.json"
    if cache_file.exists():
        return json.loads(cache_file.read_text(encoding="utf-8"))

    url = API_WORDS_ENDPOINT.format(kanji=urllib.parse.quote(kanji))
    try:
        with urllib.request.urlopen(url) as response:  # type: ignore[arg-type]
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        print(f"⚠️  Failed to fetch words for {kanji}: {exc}")
        data = []
    except urllib.error.URLError as exc:
        print(f"⚠️  Network error while fetching {kanji}: {exc}")
        data = []

    cache_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    time.sleep(0.05)
    return data


def best_meaning(meanings: List[Dict]) -> str:
    for meaning in meanings:
        glosses = meaning.get("glosses")
        if glosses:
            return glosses[0]
    return "meaning"


def priority_value(priorities: List[str]) -> int:
    if not priorities:
        return 1000

    score = 0
    for tag in priorities:
        if tag.startswith("jlpt"):
            score += 0
        elif tag.startswith("news1"):
            score += 1
        elif tag.startswith("news2"):
            score += 2
        elif tag.startswith("ichi1"):
            score += 3
        elif tag.startswith("ichi2"):
            score += 4
        elif tag.startswith("nf"):
            try:
                score += int(tag[2:])
            except ValueError:
                score += 50
        else:
            score += 60
    return score


INVALID_WORD_CHARS = set("～~[](){}・＝＝※" "0123456789")


def is_valid_word(word: str) -> bool:
    if len(word) == 0:
        return False
    if any(ch in INVALID_WORD_CHARS for ch in word):
        return False
    if " " in word:
        return False
    # Avoid extremely long compounds (often descriptive phrases)
    if len(word) > 6:
        return False
    return True


def build_candidates(kanji: str) -> List[Candidate]:
    words_payload = fetch_words(kanji)
    candidates: List[Candidate] = []

    for entry in words_payload:
        meanings = entry.get("meanings", [])
        meaning_text = best_meaning(meanings)
        for variant in entry.get("variants", []):
            word = variant.get("written")
            reading = variant.get("pronounced")
            if not word or not reading:
                continue
            if kanji not in word:
                continue
            if not is_valid_word(word):
                continue
            if any(c.word == word for c in candidates):
                continue
            priorities = variant.get("priorities", [])
            score = priority_value(priorities)
            candidates.append(
                Candidate(
                    word=word,
                    reading=reading,
                    meaning=meaning_text,
                    priority_score=score,
                    raw_priorities=priorities,
                )
            )
    return sorted(candidates, key=lambda c: (c.priority_score, len(c.word)))


def generate_sentence(candidate: Candidate, template_index: int) -> Dict[str, str]:
    template = SENTENCE_TEMPLATES[template_index % len(SENTENCE_TEMPLATES)]
    reading_romaji = kana_to_romaji(candidate.reading)
    data = {
        "japanese": template["ja"].format(word=candidate.word),
        "romaji": template["romaji"].format(reading_romaji=reading_romaji),
        "english": template["en"].format(word=candidate.word, meaning=candidate.meaning),
        "uzbek": template["uz"].format(word=candidate.word, meaning=candidate.meaning),
    }
    return data


def enrich_examples(entry: Dict) -> None:
    kanji = entry.get("kanji")
    if not kanji:
        return

    existing_examples = entry.get("examples", [])
    candidates = build_candidates(kanji)

    new_examples = []
    template_index = 0

    for candidate in candidates:
        sentence = generate_sentence(candidate, template_index)
        new_examples.append(
            {
                "word": candidate.word,
                "reading": candidate.reading,
                "meaning": candidate.meaning,
                "sentence": sentence,
            }
        )
        template_index += 1
        if len(new_examples) >= 5:
            break

    if len(new_examples) < 5:
        # Fallback: keep well-formed original examples if available
        for example in existing_examples:
            if len(new_examples) >= 5:
                break
            sentence = example.get("sentence", {})
            japanese = sentence.get("japanese", "")
            english = sentence.get("english", "")
            if not japanese or "例文" in japanese or "example" in english.lower():
                continue
            new_examples.append(example)

    if not new_examples:
        # As a final fallback, retain the existing examples to avoid empty data.
        entry["examples"] = existing_examples
        print(f"⚠️  Using existing examples for {kanji}; no valid candidates found.")
        return

    entry["examples"] = new_examples


def process_file(path: Path, dry_run: bool = False) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    updates = 0

    for entry in data:
        before = json.dumps(entry.get("examples"), ensure_ascii=False, sort_keys=True)
        enrich_examples(entry)
        after = json.dumps(entry.get("examples"), ensure_ascii=False, sort_keys=True)
        if before != after:
            updates += 1

    if not dry_run:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return updates


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Enrich JLPT kanji datasets with consistent examples.")
    parser.add_argument(
        "levels",
        nargs="*",
        default=["n3-complete", "n2-complete", "n1-complete"],
        help="Kanji dataset basenames to process (without .json).",
    )
    parser.add_argument("--dry-run", action="store_true", help="Report changes without rewriting files.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    total_updates = 0

    for level in args.levels:
        file_path = DATA_DIR / f"{level}.json"
        if not file_path.exists():
            print(f"⚠️  Skipping {level}: file not found at {file_path}")
            continue

        print(f"➡️  Processing {file_path} ...")
        updates = process_file(file_path, dry_run=args.dry_run)
        total_updates += updates
        print(f"   Updated {updates} kanji entries in {level}.json")

    print(f"✅ Finished. Entries updated: {total_updates}")


if __name__ == "__main__":
    main()
