#!/usr/bin/env python3
import json

# Read existing N3 data
with open('src/data/kanji/n3-complete.json', 'r', encoding='utf-8') as f:
    n3_data = json.load(f)

print(f'Current N3 kanji count: {len(n3_data)}')

# Additional N3 kanji data
additional_kanji = [
    {
        "id": "n3-033",
        "kanji": "議",
        "readings": {"on": ["ぎ"], "kun": []},
        "meanings": ["discussion", "deliberation"],
        "jlptLevel": "N3",
        "frequency": 33,
        "strokes": 20,
        "examples": [
            {
                "word": "会議",
                "reading": "かいぎ",
                "meaning": "meeting, conference",
                "sentence": {
                    "japanese": "会議に参加しました。",
                    "romaji": "Kaigi ni sanka shimashita.",
                    "english": "I participated in the meeting.",
                    "uzbek": "Yig'ilishda qatnashdim."
                }
            }
        ]
    },
    {
        "id": "n3-034",
        "kanji": "求",
        "readings": {"on": ["きゅう"], "kun": ["もとめる"]},
        "meanings": ["seek", "request", "demand"],
        "jlptLevel": "N3",
        "frequency": 34,
        "strokes": 7,
        "examples": [
            {
                "word": "要求",
                "reading": "ようきゅう",
                "meaning": "request, demand",
                "sentence": {
                    "japanese": "要求を出しました。",
                    "romaji": "Yōkyū o dashimashita.",
                    "english": "I made a request.",
                    "uzbek": "So'rov bildirdim."
                }
            }
        ]
    },
    {
        "id": "n3-035",
        "kanji": "級",
        "readings": {"on": ["きゅう"], "kun": []},
        "meanings": ["grade", "level", "class"],
        "jlptLevel": "N3",
        "frequency": 35,
        "strokes": 9,
        "examples": [
            {
                "word": "学年",
                "reading": "がくねん",
                "meaning": "school year, grade",
                "sentence": {
                    "japanese": "学年が上がりました。",
                    "romaji": "Gakunen ga agarimashita.",
                    "english": "I moved up a grade.",
                    "uzbek": "Sinf ko'tarildim."
                }
            }
        ]
    },
    {
        "id": "n3-036",
        "kanji": "球",
        "readings": {"on": ["きゅう"], "kun": ["たま"]},
        "meanings": ["ball", "sphere", "globe"],
        "jlptLevel": "N3",
        "frequency": 36,
        "strokes": 11,
        "examples": [
            {
                "word": "野球",
                "reading": "やきゅう",
                "meaning": "baseball",
                "sentence": {
                    "japanese": "野球をします。",
                    "romaji": "Yakyū o shimasu.",
                    "english": "I play baseball.",
                    "uzbek": "Beysbol o'ynayman."
                }
            }
        ]
    },
    {
        "id": "n3-037",
        "kanji": "給",
        "readings": {"on": ["きゅう"], "kun": []},
        "meanings": ["salary", "wage", "supply"],
        "jlptLevel": "N3",
        "frequency": 37,
        "strokes": 12,
        "examples": [
            {
                "word": "給料",
                "reading": "きゅうりょう",
                "meaning": "salary, wage",
                "sentence": {
                    "japanese": "給料をもらいました。",
                    "romaji": "Kyūryō o moraimashita.",
                    "english": "I received my salary.",
                    "uzbek": "Maoshimni oldim."
                }
            }
        ]
    },
    {
        "id": "n3-038",
        "kanji": "居",
        "readings": {"on": ["きょ"], "kun": ["いる"]},
        "meanings": ["reside", "live", "stay"],
        "jlptLevel": "N3",
        "frequency": 38,
        "strokes": 8,
        "examples": [
            {
                "word": "居住",
                "reading": "きょじゅう",
                "meaning": "residence, dwelling",
                "sentence": {
                    "japanese": "ここに居住しています。",
                    "romaji": "Koko ni kyojū shite imasu.",
                    "english": "I live here.",
                    "uzbek": "Bu yerda yashayman."
                }
            }
        ]
    },
    {
        "id": "n3-039",
        "kanji": "許",
        "readings": {"on": ["きょ"], "kun": ["ゆるす"]},
        "meanings": ["permit", "allow", "forgive"],
        "jlptLevel": "N3",
        "frequency": 39,
        "strokes": 11,
        "examples": [
            {
                "word": "許可",
                "reading": "きょか",
                "meaning": "permission, license",
                "sentence": {
                    "japanese": "許可をもらいました。",
                    "romaji": "Kyoka o moraimashita.",
                    "english": "I got permission.",
                    "uzbek": "Ruxsat oldim."
                }
            }
        ]
    },
    {
        "id": "n3-040",
        "kanji": "境",
        "readings": {"on": ["きょう"], "kun": ["さかい"]},
        "meanings": ["boundary", "border", "situation"],
        "jlptLevel": "N3",
        "frequency": 40,
        "strokes": 14,
        "examples": [
            {
                "word": "国境",
                "reading": "こっきょう",
                "meaning": "national border",
                "sentence": {
                    "japanese": "国境を越えました。",
                    "romaji": "Kokkyō o koemashita.",
                    "english": "I crossed the border.",
                    "uzbek": "Chegarani kesib o'tdim."
                }
            }
        ]
    },
    {
        "id": "n3-041",
        "kanji": "競",
        "readings": {"on": ["きょう"], "kun": ["きそう"]},
        "meanings": ["compete", "contest", "race"],
        "jlptLevel": "N3",
        "frequency": 41,
        "strokes": 20,
        "examples": [
            {
                "word": "競争",
                "reading": "きょうそう",
                "meaning": "competition, race",
                "sentence": {
                    "japanese": "競争に参加しました。",
                    "romaji": "Kyōsō ni sanka shimashita.",
                    "english": "I participated in the competition.",
                    "uzbek": "Musobaqada qatnashdim."
                }
            }
        ]
    },
    {
        "id": "n3-042",
        "kanji": "共",
        "readings": {"on": ["きょう"], "kun": ["とも"]},
        "meanings": ["together", "common", "both"],
        "jlptLevel": "N3",
        "frequency": 42,
        "strokes": 6,
        "examples": [
            {
                "word": "共同",
                "reading": "きょうどう",
                "meaning": "cooperation, joint",
                "sentence": {
                    "japanese": "共同で作業します。",
                    "romaji": "Kyōdō de sagyō shimasu.",
                    "english": "We work together.",
                    "uzbek": "Birgalikda ishlaymiz."
                }
            }
        ]
    }
]

# Combine data
all_n3_data = n3_data + additional_kanji

# Write back to file
with open('src/data/kanji/n3-complete.json', 'w', encoding='utf-8') as f:
    json.dump(all_n3_data, f, ensure_ascii=False, indent=2)

print(f'Updated N3 kanji count: {len(all_n3_data)}')
