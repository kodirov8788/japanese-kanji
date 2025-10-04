#!/usr/bin/env python3
import json

# Read existing N3 data
with open('src/data/kanji/n3-complete.json', 'r', encoding='utf-8') as f:
    n3_data = json.load(f)

print(f'Current N3 kanji count: {len(n3_data)}')

# Additional N3 kanji data (293-342)
additional_kanji = [
    {
        "id": "n3-293",
        "kanji": "忙",
        "readings": {"on": ["ぼう"], "kun": ["いそがしい"]},
        "meanings": ["busy", "hurried"],
        "jlptLevel": "N3",
        "frequency": 293,
        "strokes": 6,
        "examples": [
            {
                "word": "忙しい",
                "reading": "いそがしい",
                "meaning": "busy",
                "sentence": {
                    "japanese": "忙しい日でした。",
                    "romaji": "Isogashii hi deshita.",
                    "english": "It was a busy day.",
                    "uzbek": "Band kun edi."
                }
            }
        ]
    },
    {
        "id": "n3-294",
        "kanji": "冒",
        "readings": {"on": ["ぼう"], "kun": ["おかす"]},
        "meanings": ["risk", "brave", "venture"],
        "jlptLevel": "N3",
        "frequency": 294,
        "strokes": 9,
        "examples": [
            {
                "word": "冒険",
                "reading": "ぼうけん",
                "meaning": "adventure",
                "sentence": {
                    "japanese": "冒険をしました。",
                    "romaji": "Bōken o shimashita.",
                    "english": "I had an adventure.",
                    "uzbek": "Sarguzasht qildim."
                }
            }
        ]
    },
    {
        "id": "n3-295",
        "kanji": "暴",
        "readings": {"on": ["ぼう"], "kun": ["あばく", "あばれる"]},
        "meanings": ["violent", "rage", "expose"],
        "jlptLevel": "N3",
        "frequency": 295,
        "strokes": 15,
        "examples": [
            {
                "word": "暴力",
                "reading": "ぼうりょく",
                "meaning": "violence",
                "sentence": {
                    "japanese": "暴力を避けました。",
                    "romaji": "Bōryoku o sakemashita.",
                    "english": "I avoided violence.",
                    "uzbek": "Zo'ravonlikdan qochdim."
                }
            }
        ]
    },
    {
        "id": "n3-296",
        "kanji": "望",
        "readings": {"on": ["ぼう"], "kun": ["のぞむ", "のぞみ"]},
        "meanings": ["hope", "wish", "expect"],
        "jlptLevel": "N3",
        "frequency": 296,
        "strokes": 11,
        "examples": [
            {
                "word": "希望",
                "reading": "きぼう",
                "meaning": "hope, wish",
                "sentence": {
                    "japanese": "希望を持ちました。",
                    "romaji": "Kibō o mochimashita.",
                    "english": "I had hope.",
                    "uzbek": "Umid qildim."
                }
            }
        ]
    },
    {
        "id": "n3-297",
        "kanji": "某",
        "readings": {"on": ["ぼう"], "kun": []},
        "meanings": ["certain", "some", "one"],
        "jlptLevel": "N3",
        "frequency": 297,
        "strokes": 9,
        "examples": [
            {
                "word": "某所",
                "reading": "ぼうしょ",
                "meaning": "certain place",
                "sentence": {
                    "japanese": "某所に行きました。",
                    "romaji": "Bōsho ni ikimashita.",
                    "english": "I went to a certain place.",
                    "uzbek": "Bir joyga bordim."
                }
            }
        ]
    },
    {
        "id": "n3-298",
        "kanji": "棒",
        "readings": {"on": ["ぼう"], "kun": []},
        "meanings": ["stick", "rod", "pole"],
        "jlptLevel": "N3",
        "frequency": 298,
        "strokes": 12,
        "examples": [
            {
                "word": "棒切れ",
                "reading": "ぼうきれ",
                "meaning": "piece of stick",
                "sentence": {
                    "japanese": "棒切れを拾いました。",
                    "romaji": "Bōkire o hiroimashita.",
                    "english": "I picked up a piece of stick.",
                    "uzbek": "Tayoq parchasini oldim."
                }
            }
        ]
    },
    {
        "id": "n3-299",
        "kanji": "包",
        "readings": {"on": ["ほう"], "kun": ["つつむ"]},
        "meanings": ["wrap", "package", "contain"],
        "jlptLevel": "N3",
        "frequency": 299,
        "strokes": 5,
        "examples": [
            {
                "word": "包装",
                "reading": "ほうそう",
                "meaning": "packaging, wrapping",
                "sentence": {
                    "japanese": "包装をしました。",
                    "romaji": "Hōsō o shimashita.",
                    "english": "I packaged it.",
                    "uzbek": "O'radim."
                }
            }
        ]
    },
    {
        "id": "n3-300",
        "kanji": "胞",
        "readings": {"on": ["ほう"], "kun": []},
        "meanings": ["cell", "membrane"],
        "jlptLevel": "N3",
        "frequency": 300,
        "strokes": 9,
        "examples": [
            {
                "word": "細胞",
                "reading": "さいぼう",
                "meaning": "cell",
                "sentence": {
                    "japanese": "細胞を観察しました。",
                    "romaji": "Saibō o kansatsu shimashita.",
                    "english": "I observed cells.",
                    "uzbek": "Hujayralarni kuzatdim."
                }
            }
        ]
    },
    {
        "id": "n3-301",
        "kanji": "宝",
        "readings": {"on": ["ほう"], "kun": ["たから"]},
        "meanings": ["treasure", "precious"],
        "jlptLevel": "N3",
        "frequency": 301,
        "strokes": 8,
        "examples": [
            {
                "word": "宝物",
                "reading": "たからもの",
                "meaning": "treasure",
                "sentence": {
                    "japanese": "宝物を見つけました。",
                    "romaji": "Takaramono o mitsukemashita.",
                    "english": "I found treasure.",
                    "uzbek": "Xazina topdim."
                }
            }
        ]
    },
    {
        "id": "n3-302",
        "kanji": "抱",
        "readings": {"on": ["ほう"], "kun": ["だく", "いだく"]},
        "meanings": ["embrace", "hug", "hold"],
        "jlptLevel": "N3",
        "frequency": 302,
        "strokes": 8,
        "examples": [
            {
                "word": "抱擁",
                "reading": "ほうよう",
                "meaning": "embrace, hug",
                "sentence": {
                    "japanese": "抱擁しました。",
                    "romaji": "Hōyō shimashita.",
                    "english": "I embraced.",
                    "uzbek": "Quchib oldim."
                }
            }
        ]
    },
    {
        "id": "n3-303",
        "kanji": "報",
        "readings": {"on": ["ほう"], "kun": ["むくいる"]},
        "meanings": ["report", "news", "reward"],
        "jlptLevel": "N3",
        "frequency": 303,
        "strokes": 12,
        "examples": [
            {
                "word": "報告書",
                "reading": "ほうこくしょ",
                "meaning": "report document",
                "sentence": {
                    "japanese": "報告書を書きました。",
                    "romaji": "Hōkokusho o kakimashita.",
                    "english": "I wrote a report.",
                    "uzbek": "Hisobot yozdim."
                }
            }
        ]
    },
    {
        "id": "n3-304",
        "kanji": "奉",
        "readings": {"on": ["ほう"], "kun": ["たてまつる"]},
        "meanings": ["serve", "offer", "dedicate"],
        "jlptLevel": "N3",
        "frequency": 304,
        "strokes": 8,
        "examples": [
            {
                "word": "奉仕",
                "reading": "ほうし",
                "meaning": "service, volunteer work",
                "sentence": {
                    "japanese": "奉仕をしました。",
                    "romaji": "Hōshi o shimashita.",
                    "english": "I served.",
                    "uzbek": "Xizmat qildim."
                }
            }
        ]
    },
    {
        "id": "n3-305",
        "kanji": "封",
        "readings": {"on": ["ふう"], "kun": []},
        "meanings": ["seal", "close", "envelope"],
        "jlptLevel": "N3",
        "frequency": 305,
        "strokes": 9,
        "examples": [
            {
                "word": "封筒",
                "reading": "ふうとう",
                "meaning": "envelope",
                "sentence": {
                    "japanese": "封筒を開けました。",
                    "romaji": "Fūtō o akemashita.",
                    "english": "I opened the envelope.",
                    "uzbek": "Konvertni ochdim."
                }
            }
        ]
    },
    {
        "id": "n3-306",
        "kanji": "峰",
        "readings": {"on": ["ほう"], "kun": ["みね"]},
        "meanings": ["peak", "summit", "ridge"],
        "jlptLevel": "N3",
        "frequency": 306,
        "strokes": 10,
        "examples": [
            {
                "word": "山峰",
                "reading": "さんぽう",
                "meaning": "mountain peak",
                "sentence": {
                    "japanese": "山峰に登りました。",
                    "romaji": "Sanpō ni noborimashita.",
                    "english": "I climbed the mountain peak.",
                    "uzbek": "Tog' cho'qqisiga chiqdim."
                }
            }
        ]
    },
    {
        "id": "n3-307",
        "kanji": "崩",
        "readings": {"on": ["ほう"], "kun": ["くずれる", "くずす"]},
        "meanings": ["collapse", "break down", "crumble"],
        "jlptLevel": "N3",
        "frequency": 307,
        "strokes": 11,
        "examples": [
            {
                "word": "崩壊",
                "reading": "ほうかい",
                "meaning": "collapse, breakdown",
                "sentence": {
                    "japanese": "崩壊しました。",
                    "romaji": "Hōkai shimashita.",
                    "english": "It collapsed.",
                    "uzbek": "Qulab tushdi."
                }
            }
        ]
    },
    {
        "id": "n3-308",
        "kanji": "北",
        "readings": {"on": ["ほく"], "kun": ["きた"]},
        "meanings": ["north"],
        "jlptLevel": "N3",
        "frequency": 308,
        "strokes": 5,
        "examples": [
            {
                "word": "北側",
                "reading": "きたがわ",
                "meaning": "north side",
                "sentence": {
                    "japanese": "北側にあります。",
                    "romaji": "Kitagawa ni arimasu.",
                    "english": "It's on the north side.",
                    "uzbek": "Shimoliy tomonda."
                }
            }
        ]
    },
    {
        "id": "n3-309",
        "kanji": "墨",
        "readings": {"on": ["ぼく"], "kun": ["すみ"]},
        "meanings": ["ink", "black ink"],
        "jlptLevel": "N3",
        "frequency": 309,
        "strokes": 14,
        "examples": [
            {
                "word": "墨汁",
                "reading": "ぼくじゅう",
                "meaning": "ink",
                "sentence": {
                    "japanese": "墨汁で書きました。",
                    "romaji": "Bokujū de kakimashita.",
                    "english": "I wrote with ink.",
                    "uzbek": "Siya bilan yozdim."
                }
            }
        ]
    },
    {
        "id": "n3-310",
        "kanji": "撲",
        "readings": {"on": ["ぼく"], "kun": []},
        "meanings": ["strike", "hit", "beat"],
        "jlptLevel": "N3",
        "frequency": 310,
        "strokes": 15,
        "examples": [
            {
                "word": "撲滅",
                "reading": "ぼくめつ",
                "meaning": "extermination, eradication",
                "sentence": {
                    "japanese": "撲滅を図りました。",
                    "romaji": "Bokumetsu o hakarimashita.",
                    "english": "I planned extermination.",
                    "uzbek": "Yo'q qilishni rejalashtirdim."
                }
            }
        ]
    },
    {
        "id": "n3-311",
        "kanji": "没",
        "readings": {"on": ["ぼつ"], "kun": ["おぼれる"]},
        "meanings": ["sink", "drown", "die"],
        "jlptLevel": "N3",
        "frequency": 311,
        "strokes": 7,
        "examples": [
            {
                "word": "没落",
                "reading": "ぼつらく",
                "meaning": "ruin, downfall",
                "sentence": {
                    "japanese": "没落しました。",
                    "romaji": "Botsuraku shimashita.",
                    "english": "It fell into ruin.",
                    "uzbek": "Qulab tushdi."
                }
            }
        ]
    },
    {
        "id": "n3-312",
        "kanji": "本",
        "readings": {"on": ["ほん"], "kun": ["もと"]},
        "meanings": ["book", "origin", "main"],
        "jlptLevel": "N3",
        "frequency": 312,
        "strokes": 5,
        "examples": [
            {
                "word": "本物",
                "reading": "ほんもの",
                "meaning": "genuine article, real thing",
                "sentence": {
                    "japanese": "本物です。",
                    "romaji": "Honmono desu.",
                    "english": "It's genuine.",
                    "uzbek": "Haqiqiy narsa."
                }
            }
        ]
    },
    {
        "id": "n3-313",
        "kanji": "翻",
        "readings": {"on": ["ほん"], "kun": ["ひるがえる"]},
        "meanings": ["flip", "turn over", "translate"],
        "jlptLevel": "N3",
        "frequency": 313,
        "strokes": 18,
        "examples": [
            {
                "word": "翻訳",
                "reading": "ほんやく",
                "meaning": "translation",
                "sentence": {
                    "japanese": "翻訳をしました。",
                    "romaji": "Honyaku o shimashita.",
                    "english": "I translated.",
                    "uzbek": "Tarjima qildim."
                }
            }
        ]
    },
    {
        "id": "n3-314",
        "kanji": "凡",
        "readings": {"on": ["ぼん"], "kun": ["おおよそ"]},
        "meanings": ["ordinary", "common", "general"],
        "jlptLevel": "N3",
        "frequency": 314,
        "strokes": 3,
        "examples": [
            {
                "word": "平凡",
                "reading": "へいぼん",
                "meaning": "ordinary, commonplace",
                "sentence": {
                    "japanese": "平凡な生活です。",
                    "romaji": "Heibon na seikatsu desu.",
                    "english": "It's an ordinary life.",
                    "uzbek": "Oddiy hayot."
                }
            }
        ]
    },
    {
        "id": "n3-315",
        "kanji": "盆",
        "readings": {"on": ["ぼん"], "kun": []},
        "meanings": ["tray", "basin", "festival"],
        "jlptLevel": "N3",
        "frequency": 315,
        "strokes": 9,
        "examples": [
            {
                "word": "お盆",
                "reading": "おぼん",
                "meaning": "tray, Obon festival",
                "sentence": {
                    "japanese": "お盆を運びました。",
                    "romaji": "Obon o hakobimashita.",
                    "english": "I carried the tray.",
                    "uzbek": "Tarelkani ko'tardim."
                }
            }
        ]
    },
    {
        "id": "n3-316",
        "kanji": "麻",
        "readings": {"on": ["ま"], "kun": ["あさ"]},
        "meanings": ["hemp", "flax", "numbness"],
        "jlptLevel": "N3",
        "frequency": 316,
        "strokes": 11,
        "examples": [
            {
                "word": "麻痺",
                "reading": "まひ",
                "meaning": "paralysis, numbness",
                "sentence": {
                    "japanese": "麻痺しました。",
                    "romaji": "Mahi shimashita.",
                    "english": "I became paralyzed.",
                    "uzbek": "Falaj bo'ldim."
                }
            }
        ]
    },
    {
        "id": "n3-317",
        "kanji": "摩",
        "readings": {"on": ["ま"], "kun": ["する", "こする"]},
        "meanings": ["rub", "polish", "friction"],
        "jlptLevel": "N3",
        "frequency": 317,
        "strokes": 15,
        "examples": [
            {
                "word": "摩擦",
                "reading": "まさつ",
                "meaning": "friction",
                "sentence": {
                    "japanese": "摩擦が生じました。",
                    "romaji": "Masatsu ga shōjimashita.",
                    "english": "Friction occurred.",
                    "uzbek": "Ishqalanish yuz berdi."
                }
            }
        ]
    },
    {
        "id": "n3-318",
        "kanji": "磨",
        "readings": {"on": ["ま"], "kun": ["みがく"]},
        "meanings": ["polish", "grind", "refine"],
        "jlptLevel": "N3",
        "frequency": 318,
        "strokes": 16,
        "examples": [
            {
                "word": "研磨",
                "reading": "けんま",
                "meaning": "polishing, grinding",
                "sentence": {
                    "japanese": "研磨をしました。",
                    "romaji": "Kenma o shimashita.",
                    "english": "I polished it.",
                    "uzbek": "Jiloladim."
                }
            }
        ]
    },
    {
        "id": "n3-319",
        "kanji": "魔",
        "readings": {"on": ["ま"], "kun": []},
        "meanings": ["demon", "devil", "magic"],
        "jlptLevel": "N3",
        "frequency": 319,
        "strokes": 21,
        "examples": [
            {
                "word": "魔法",
                "reading": "まほう",
                "meaning": "magic",
                "sentence": {
                    "japanese": "魔法を使いました。",
                    "romaji": "Mahō o tsukaimashita.",
                    "english": "I used magic.",
                    "uzbek": "Sehr ishlatdim."
                }
            }
        ]
    },
    {
        "id": "n3-320",
        "kanji": "抹",
        "readings": {"on": ["まつ"], "kun": []},
        "meanings": ["wipe", "erase", "rub out"],
        "jlptLevel": "N3",
        "frequency": 320,
        "strokes": 8,
        "examples": [
            {
                "word": "抹消",
                "reading": "まっしょう",
                "meaning": "erasure, deletion",
                "sentence": {
                    "japanese": "抹消しました。",
                    "romaji": "Masshō shimashita.",
                    "english": "I erased it.",
                    "uzbek": "O'chirib tashladim."
                }
            }
        ]
    },
    {
        "id": "n3-321",
        "kanji": "末",
        "readings": {"on": ["まつ"], "kun": ["すえ"]},
        "meanings": ["end", "tip", "last"],
        "jlptLevel": "N3",
        "frequency": 321,
        "strokes": 5,
        "examples": [
            {
                "word": "年末",
                "reading": "ねんまつ",
                "meaning": "end of year",
                "sentence": {
                    "japanese": "年末になりました。",
                    "romaji": "Nenmatsu ni narimashita.",
                    "english": "It became the end of year.",
                    "uzbek": "Yil oxiri bo'ldi."
                }
            }
        ]
    },
    {
        "id": "n3-322",
        "kanji": "万",
        "readings": {"on": ["まん"], "kun": []},
        "meanings": ["ten thousand", "many", "all"],
        "jlptLevel": "N3",
        "frequency": 322,
        "strokes": 3,
        "examples": [
            {
                "word": "万歳",
                "reading": "ばんざい",
                "meaning": "hurrah, long live",
                "sentence": {
                    "japanese": "万歳を叫びました。",
                    "romaji": "Banzai o sakebimashita.",
                    "english": "I shouted hurrah.",
                    "uzbek": "Hurray deb baqirdim."
                }
            }
        ]
    },
    {
        "id": "n3-323",
        "kanji": "満",
        "readings": {"on": ["まん"], "kun": ["みちる", "みたす"]},
        "meanings": ["full", "satisfy", "complete"],
        "jlptLevel": "N3",
        "frequency": 323,
        "strokes": 12,
        "examples": [
            {
                "word": "満足",
                "reading": "まんぞく",
                "meaning": "satisfaction",
                "sentence": {
                    "japanese": "満足しました。",
                    "romaji": "Manzoku shimashita.",
                    "english": "I was satisfied.",
                    "uzbek": "Qoniqdim."
                }
            }
        ]
    },
    {
        "id": "n3-324",
        "kanji": "慢",
        "readings": {"on": ["まん"], "kun": []},
        "meanings": ["pride", "arrogance", "chronic"],
        "jlptLevel": "N3",
        "frequency": 324,
        "strokes": 14,
        "examples": [
            {
                "word": "慢性",
                "reading": "まんせい",
                "meaning": "chronic",
                "sentence": {
                    "japanese": "慢性の病気です。",
                    "romaji": "Mansei no byōki desu.",
                    "english": "It's a chronic disease.",
                    "uzbek": "Surunkali kasallik."
                }
            }
        ]
    },
    {
        "id": "n3-325",
        "kanji": "漫",
        "readings": {"on": ["まん"], "kun": []},
        "meanings": ["random", "wander", "comic"],
        "jlptLevel": "N3",
        "frequency": 325,
        "strokes": 14,
        "examples": [
            {
                "word": "漫画",
                "reading": "まんが",
                "meaning": "comic, manga",
                "sentence": {
                    "japanese": "漫画を読みました。",
                    "romaji": "Manga o yomimashita.",
                    "english": "I read manga.",
                    "uzbek": "Manga o'qidim."
                }
            }
        ]
    },
    {
        "id": "n3-326",
        "kanji": "未",
        "readings": {"on": ["み"], "kun": ["いまだ"]},
        "meanings": ["not yet", "un-", "future"],
        "jlptLevel": "N3",
        "frequency": 326,
        "strokes": 5,
        "examples": [
            {
                "word": "未来",
                "reading": "みらい",
                "meaning": "future",
                "sentence": {
                    "japanese": "未来を考えました。",
                    "romaji": "Mirai o kangaemashita.",
                    "english": "I thought about the future.",
                    "uzbek": "Kelajak haqida o'yladim."
                }
            }
        ]
    },
    {
        "id": "n3-327",
        "kanji": "味",
        "readings": {"on": ["み"], "kun": ["あじ", "あじわう"]},
        "meanings": ["taste", "flavor", "experience"],
        "jlptLevel": "N3",
        "frequency": 327,
        "strokes": 8,
        "examples": [
            {
                "word": "味覚",
                "reading": "みかく",
                "meaning": "sense of taste",
                "sentence": {
                    "japanese": "味覚を楽しみました。",
                    "romaji": "Mikaku o tanoshimimashita.",
                    "english": "I enjoyed the taste.",
                    "uzbek": "Ta'mdan zavqlandim."
                }
            }
        ]
    },
    {
        "id": "n3-328",
        "kanji": "魅",
        "readings": {"on": ["み"], "kun": []},
        "meanings": ["charm", "fascinate", "attract"],
        "jlptLevel": "N3",
        "frequency": 328,
        "strokes": 15,
        "examples": [
            {
                "word": "魅力",
                "reading": "みりょく",
                "meaning": "charm, appeal",
                "sentence": {
                    "japanese": "魅力があります。",
                    "romaji": "Miryoku ga arimasu.",
                    "english": "It has charm.",
                    "uzbek": "Jozibasi bor."
                }
            }
        ]
    },
    {
        "id": "n3-329",
        "kanji": "密",
        "readings": {"on": ["みつ"], "kun": []},
        "meanings": ["dense", "secret", "intimate"],
        "jlptLevel": "N3",
        "frequency": 329,
        "strokes": 11,
        "examples": [
            {
                "word": "秘密",
                "reading": "ひみつ",
                "meaning": "secret",
                "sentence": {
                    "japanese": "秘密を守りました。",
                    "romaji": "Himitsu o mamorimashita.",
                    "english": "I kept the secret.",
                    "uzbek": "Sirni saqladim."
                }
            }
        ]
    },
    {
        "id": "n3-330",
        "kanji": "脈",
        "readings": {"on": ["みゃく"], "kun": []},
        "meanings": ["pulse", "vein", "connection"],
        "jlptLevel": "N3",
        "frequency": 330,
        "strokes": 10,
        "examples": [
            {
                "word": "脈拍",
                "reading": "みゃくはく",
                "meaning": "pulse",
                "sentence": {
                    "japanese": "脈拍を測りました。",
                    "romaji": "Myakuhaku o hakari mashita.",
                    "english": "I measured the pulse.",
                    "uzbek": "Nabzni o'lchadim."
                }
            }
        ]
    },
    {
        "id": "n3-331",
        "kanji": "妙",
        "readings": {"on": ["みょう"], "kun": []},
        "meanings": ["strange", "wonderful", "mysterious"],
        "jlptLevel": "N3",
        "frequency": 331,
        "strokes": 7,
        "examples": [
            {
                "word": "奇妙",
                "reading": "きみょう",
                "meaning": "strange, odd",
                "sentence": {
                    "japanese": "奇妙な現象です。",
                    "romaji": "Kimyō na genshō desu.",
                    "english": "It's a strange phenomenon.",
                    "uzbek": "G'alati hodisa."
                }
            }
        ]
    },
    {
        "id": "n3-332",
        "kanji": "民",
        "readings": {"on": ["みん"], "kun": ["たみ"]},
        "meanings": ["people", "citizens", "nation"],
        "jlptLevel": "N3",
        "frequency": 332,
        "strokes": 5,
        "examples": [
            {
                "word": "国民",
                "reading": "こくみん",
                "meaning": "citizens, people",
                "sentence": {
                    "japanese": "国民の義務です。",
                    "romaji": "Kokumin no gimu desu.",
                    "english": "It's a citizen's duty.",
                    "uzbek": "Fuqaroning vazifasi."
                }
            }
        ]
    },
    {
        "id": "n3-333",
        "kanji": "眠",
        "readings": {"on": ["みん"], "kun": ["ねむる", "ねむい"]},
        "meanings": ["sleep", "drowsy"],
        "jlptLevel": "N3",
        "frequency": 333,
        "strokes": 10,
        "examples": [
            {
                "word": "睡眠",
                "reading": "すいみん",
                "meaning": "sleep",
                "sentence": {
                    "japanese": "睡眠を取りました。",
                    "romaji": "Suimin o torimashita.",
                    "english": "I got sleep.",
                    "uzbek": "Uxladim."
                }
            }
        ]
    },
    {
        "id": "n3-334",
        "kanji": "無",
        "readings": {"on": ["む"], "kun": ["ない"]},
        "meanings": ["nothing", "none", "without"],
        "jlptLevel": "N3",
        "frequency": 334,
        "strokes": 12,
        "examples": [
            {
                "word": "無理",
                "reading": "むり",
                "meaning": "impossible, unreasonable",
                "sentence": {
                    "japanese": "無理をしました。",
                    "romaji": "Muri o shimashita.",
                    "english": "I overdid it.",
                    "uzbek": "O'z kuchimdan oshib ishladim."
                }
            }
        ]
    },
    {
        "id": "n3-335",
        "kanji": "夢",
        "readings": {"on": ["む"], "kun": ["ゆめ"]},
        "meanings": ["dream", "vision"],
        "jlptLevel": "N3",
        "frequency": 335,
        "strokes": 13,
        "examples": [
            {
                "word": "夢中",
                "reading": "むちゅう",
                "meaning": "absorbed, engrossed",
                "sentence": {
                    "japanese": "夢中になりました。",
                    "romaji": "Muchū ni narimashita.",
                    "english": "I became absorbed.",
                    "uzbek": "Jalb qildim."
                }
            }
        ]
    },
    {
        "id": "n3-336",
        "kanji": "霧",
        "readings": {"on": ["む"], "kun": ["きり"]},
        "meanings": ["fog", "mist"],
        "jlptLevel": "N3",
        "frequency": 336,
        "strokes": 19,
        "examples": [
            {
                "word": "濃霧",
                "reading": "のうむ",
                "meaning": "thick fog",
                "sentence": {
                    "japanese": "濃霧が立ち込めました。",
                    "romaji": "Nōmu ga tachikomemashita.",
                    "english": "Thick fog settled in.",
                    "uzbek": "Qalin tuman tushdi."
                }
            }
        ]
    },
    {
        "id": "n3-337",
        "kanji": "娘",
        "readings": {"on": ["じょう"], "kun": ["むすめ"]},
        "meanings": ["daughter", "girl"],
        "jlptLevel": "N3",
        "frequency": 337,
        "strokes": 10,
        "examples": [
            {
                "word": "娘さん",
                "reading": "むすめさん",
                "meaning": "daughter (polite)",
                "sentence": {
                    "japanese": "娘さんがいます。",
                    "romaji": "Musume-san ga imasu.",
                    "english": "I have a daughter.",
                    "uzbek": "Qizim bor."
                }
            }
        ]
    },
    {
        "id": "n3-338",
        "kanji": "名",
        "readings": {"on": ["めい"], "kun": ["な"]},
        "meanings": ["name", "famous", "reputation"],
        "jlptLevel": "N3",
        "frequency": 338,
        "strokes": 6,
        "examples": [
            {
                "word": "名前",
                "reading": "なまえ",
                "meaning": "name",
                "sentence": {
                    "japanese": "名前を教えました。",
                    "romaji": "Namae o oshiemashita.",
                    "english": "I told my name.",
                    "uzbek": "Ismimni aytdim."
                }
            }
        ]
    },
    {
        "id": "n3-339",
        "kanji": "命",
        "readings": {"on": ["めい"], "kun": ["いのち"]},
        "meanings": ["life", "fate", "command"],
        "jlptLevel": "N3",
        "frequency": 339,
        "strokes": 8,
        "examples": [
            {
                "word": "生命",
                "reading": "せいめい",
                "meaning": "life",
                "sentence": {
                    "japanese": "生命を大切にしました。",
                    "romaji": "Seimei o taisetsu ni shimashita.",
                    "english": "I valued life.",
                    "uzbek": "Hayotni qadrladim."
                }
            }
        ]
    },
    {
        "id": "n3-340",
        "kanji": "明",
        "readings": {"on": ["めい"], "kun": ["あかるい", "あきらか"]},
        "meanings": ["bright", "clear", "next"],
        "jlptLevel": "N3",
        "frequency": 340,
        "strokes": 8,
        "examples": [
            {
                "word": "明日",
                "reading": "あした",
                "meaning": "tomorrow",
                "sentence": {
                    "japanese": "明日会いましょう。",
                    "romaji": "Ashita aimashō.",
                    "english": "Let's meet tomorrow.",
                    "uzbek": "Ertaga ko'rishamiz."
                }
            }
        ]
    },
    {
        "id": "n3-341",
        "kanji": "迷",
        "readings": {"on": ["めい"], "kun": ["まよう"]},
        "meanings": ["lost", "confused", "wander"],
        "jlptLevel": "N3",
        "frequency": 341,
        "strokes": 9,
        "examples": [
            {
                "word": "迷子",
                "reading": "まいご",
                "meaning": "lost child",
                "sentence": {
                    "japanese": "迷子になりました。",
                    "romaji": "Maigo ni narimashita.",
                    "english": "I got lost.",
                    "uzbek": "Yo'qoldim."
                }
            }
        ]
    },
    {
        "id": "n3-342",
        "kanji": "盟",
        "readings": {"on": ["めい"], "kun": []},
        "meanings": ["alliance", "pledge", "oath"],
        "jlptLevel": "N3",
        "frequency": 342,
        "strokes": 13,
        "examples": [
            {
                "word": "同盟",
                "reading": "どうめい",
                "meaning": "alliance, union",
                "sentence": {
                    "japanese": "同盟を結びました。",
                    "romaji": "Dōmei o musubimashita.",
                    "english": "I formed an alliance.",
                    "uzbek": "Ittifoq tuzdim."
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
