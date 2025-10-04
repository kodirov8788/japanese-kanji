#!/usr/bin/env python3
import json

# Read existing N3 data
with open('src/data/kanji/n3-complete.json', 'r', encoding='utf-8') as f:
    n3_data = json.load(f)

print(f'Current N3 kanji count: {len(n3_data)}')

# Additional N3 kanji data (343-370) - Final N3 batch
additional_kanji = [
    {
        "id": "n3-343",
        "kanji": "毛",
        "readings": {"on": ["もう"], "kun": ["け"]},
        "meanings": ["hair", "fur", "wool"],
        "jlptLevel": "N3",
        "frequency": 343,
        "strokes": 4,
        "examples": [
            {
                "word": "毛髪",
                "reading": "もうはつ",
                "meaning": "hair",
                "sentence": {
                    "japanese": "毛髪を切りました。",
                    "romaji": "Mōhatsu o kirimashita.",
                    "english": "I cut my hair.",
                    "uzbek": "Sochimni qirqib tashladim."
                }
            }
        ]
    },
    {
        "id": "n3-344",
        "kanji": "猛",
        "readings": {"on": ["もう"], "kun": []},
        "meanings": ["fierce", "violent", "intense"],
        "jlptLevel": "N3",
        "frequency": 344,
        "strokes": 11,
        "examples": [
            {
                "word": "猛烈",
                "reading": "もうれつ",
                "meaning": "fierce, violent",
                "sentence": {
                    "japanese": "猛烈な暑さです。",
                    "romaji": "Mōretsu na atsusa desu.",
                    "english": "It's extremely hot.",
                    "uzbek": "Juda issiq."
                }
            }
        ]
    },
    {
        "id": "n3-345",
        "kanji": "盲",
        "readings": {"on": ["もう"], "kun": ["めくら"]},
        "meanings": ["blind", "blindness"],
        "jlptLevel": "N3",
        "frequency": 345,
        "strokes": 8,
        "examples": [
            {
                "word": "盲目",
                "reading": "もうもく",
                "meaning": "blindness",
                "sentence": {
                    "japanese": "盲目になりました。",
                    "romaji": "Mōmoku ni narimashita.",
                    "english": "I became blind.",
                    "uzbek": "Ko'r bo'ldim."
                }
            }
        ]
    },
    {
        "id": "n3-346",
        "kanji": "網",
        "readings": {"on": ["もう"], "kun": ["あみ"]},
        "meanings": ["net", "network", "web"],
        "jlptLevel": "N3",
        "frequency": 346,
        "strokes": 14,
        "examples": [
            {
                "word": "漁網",
                "reading": "ぎょもう",
                "meaning": "fishing net",
                "sentence": {
                    "japanese": "漁網を投げました。",
                    "romaji": "Gyomō o nagemashita.",
                    "english": "I threw the fishing net.",
                    "uzbek": "Baliq tarmog'ini tashladim."
                }
            }
        ]
    },
    {
        "id": "n3-347",
        "kanji": "耗",
        "readings": {"on": ["もう"], "kun": []},
        "meanings": ["wear out", "consume", "waste"],
        "jlptLevel": "N3",
        "frequency": 347,
        "strokes": 10,
        "examples": [
            {
                "word": "消耗",
                "reading": "しょうもう",
                "meaning": "consumption, waste",
                "sentence": {
                    "japanese": "消耗しました。",
                    "romaji": "Shōmō shimashita.",
                    "english": "I consumed it.",
                    "uzbek": "Iste'mol qildim."
                }
            }
        ]
    },
    {
        "id": "n3-348",
        "kanji": "木",
        "readings": {"on": ["もく"], "kun": ["き"]},
        "meanings": ["tree", "wood", "Thursday"],
        "jlptLevel": "N3",
        "frequency": 348,
        "strokes": 4,
        "examples": [
            {
                "word": "木曜日",
                "reading": "もくようび",
                "meaning": "Thursday",
                "sentence": {
                    "japanese": "木曜日に会いましょう。",
                    "romaji": "Mokuyōbi ni aimashō.",
                    "english": "Let's meet on Thursday.",
                    "uzbek": "Payshanba kuni ko'rishamiz."
                }
            }
        ]
    },
    {
        "id": "n3-349",
        "kanji": "目",
        "readings": {"on": ["もく"], "kun": ["め"]},
        "meanings": ["eye", "look", "point"],
        "jlptLevel": "N3",
        "frequency": 349,
        "strokes": 5,
        "examples": [
            {
                "word": "目的",
                "reading": "もくてき",
                "meaning": "purpose, aim",
                "sentence": {
                    "japanese": "目的を達成しました。",
                    "romaji": "Mokuteki o tassei shimashita.",
                    "english": "I achieved my purpose.",
                    "uzbek": "Maqsadimga erishdim."
                }
            }
        ]
    },
    {
        "id": "n3-350",
        "kanji": "牧",
        "readings": {"on": ["ぼく"], "kun": ["まき"]},
        "meanings": ["pasture", "graze", "shepherd"],
        "jlptLevel": "N3",
        "frequency": 350,
        "strokes": 8,
        "examples": [
            {
                "word": "牧場",
                "reading": "ぼくじょう",
                "meaning": "pasture, ranch",
                "sentence": {
                    "japanese": "牧場に行きました。",
                    "romaji": "Bokujō ni ikimashita.",
                    "english": "I went to the ranch.",
                    "uzbek": "Chorvachilik fermasiga bordim."
                }
            }
        ]
    },
    {
        "id": "n3-351",
        "kanji": "模",
        "readings": {"on": ["も"], "kun": []},
        "meanings": ["model", "pattern", "imitate"],
        "jlptLevel": "N3",
        "frequency": 351,
        "strokes": 14,
        "examples": [
            {
                "word": "模倣",
                "reading": "もほう",
                "meaning": "imitation, mimicry",
                "sentence": {
                    "japanese": "模倣しました。",
                    "romaji": "Mohō shimashita.",
                    "english": "I imitated it.",
                    "uzbek": "Taqlid qildim."
                }
            }
        ]
    },
    {
        "id": "n3-352",
        "kanji": "膜",
        "readings": {"on": ["まく"], "kun": []},
        "meanings": ["membrane", "film"],
        "jlptLevel": "N3",
        "frequency": 352,
        "strokes": 14,
        "examples": [
            {
                "word": "細胞膜",
                "reading": "さいぼうまく",
                "meaning": "cell membrane",
                "sentence": {
                    "japanese": "細胞膜を観察しました。",
                    "romaji": "Saibōmaku o kansatsu shimashita.",
                    "english": "I observed the cell membrane.",
                    "uzbek": "Hujayra membranasini kuzatdim."
                }
            }
        ]
    },
    {
        "id": "n3-353",
        "kanji": "抹",
        "readings": {"on": ["まつ"], "kun": []},
        "meanings": ["wipe", "erase", "rub out"],
        "jlptLevel": "N3",
        "frequency": 353,
        "strokes": 8,
        "examples": [
            {
                "word": "抹茶",
                "reading": "まっちゃ",
                "meaning": "matcha tea",
                "sentence": {
                    "japanese": "抹茶を飲みました。",
                    "romaji": "Matcha o nomimashita.",
                    "english": "I drank matcha tea.",
                    "uzbek": "Matcha choyni ichdim."
                }
            }
        ]
    },
    {
        "id": "n3-354",
        "kanji": "末",
        "readings": {"on": ["まつ"], "kun": ["すえ"]},
        "meanings": ["end", "tip", "last"],
        "jlptLevel": "N3",
        "frequency": 354,
        "strokes": 5,
        "examples": [
            {
                "word": "月末",
                "reading": "げつまつ",
                "meaning": "end of month",
                "sentence": {
                    "japanese": "月末になりました。",
                    "romaji": "Getsumatsu ni narimashita.",
                    "english": "It became the end of month.",
                    "uzbek": "Oy oxiri bo'ldi."
                }
            }
        ]
    },
    {
        "id": "n3-355",
        "kanji": "万",
        "readings": {"on": ["まん"], "kun": []},
        "meanings": ["ten thousand", "many", "all"],
        "jlptLevel": "N3",
        "frequency": 355,
        "strokes": 3,
        "examples": [
            {
                "word": "万国",
                "reading": "ばんこく",
                "meaning": "all nations, international",
                "sentence": {
                    "japanese": "万国博覧会です。",
                    "romaji": "Bankoku hakurankai desu.",
                    "english": "It's a world exposition.",
                    "uzbek": "Xalqaro ko'rgazma."
                }
            }
        ]
    },
    {
        "id": "n3-356",
        "kanji": "満",
        "readings": {"on": ["まん"], "kun": ["みちる", "みたす"]},
        "meanings": ["full", "satisfy", "complete"],
        "jlptLevel": "N3",
        "frequency": 356,
        "strokes": 12,
        "examples": [
            {
                "word": "満員",
                "reading": "まんいん",
                "meaning": "full house, packed",
                "sentence": {
                    "japanese": "満員でした。",
                    "romaji": "Man'in deshita.",
                    "english": "It was packed.",
                    "uzbek": "To'la edi."
                }
            }
        ]
    },
    {
        "id": "n3-357",
        "kanji": "慢",
        "readings": {"on": ["まん"], "kun": []},
        "meanings": ["pride", "arrogance", "chronic"],
        "jlptLevel": "N3",
        "frequency": 357,
        "strokes": 14,
        "examples": [
            {
                "word": "自慢",
                "reading": "じまん",
                "meaning": "pride, boast",
                "sentence": {
                    "japanese": "自慢しました。",
                    "romaji": "Jiman shimashita.",
                    "english": "I boasted.",
                    "uzbek": "Maqtanib gapirdim."
                }
            }
        ]
    },
    {
        "id": "n3-358",
        "kanji": "漫",
        "readings": {"on": ["まん"], "kun": []},
        "meanings": ["random", "wander", "comic"],
        "jlptLevel": "N3",
        "frequency": 358,
        "strokes": 14,
        "examples": [
            {
                "word": "漫画",
                "reading": "まんが",
                "meaning": "comic, manga",
                "sentence": {
                    "japanese": "漫画を描きました。",
                    "romaji": "Manga o kakimashita.",
                    "english": "I drew manga.",
                    "uzbek": "Manga chizdim."
                }
            }
        ]
    },
    {
        "id": "n3-359",
        "kanji": "未",
        "readings": {"on": ["み"], "kun": ["いまだ"]},
        "meanings": ["not yet", "un-", "future"],
        "jlptLevel": "N3",
        "frequency": 359,
        "strokes": 5,
        "examples": [
            {
                "word": "未知",
                "reading": "みち",
                "meaning": "unknown, unfamiliar",
                "sentence": {
                    "japanese": "未知の世界です。",
                    "romaji": "Michi no sekai desu.",
                    "english": "It's an unknown world.",
                    "uzbek": "Noma'lum dunyo."
                }
            }
        ]
    },
    {
        "id": "n3-360",
        "kanji": "味",
        "readings": {"on": ["み"], "kun": ["あじ", "あじわう"]},
        "meanings": ["taste", "flavor", "experience"],
        "jlptLevel": "N3",
        "frequency": 360,
        "strokes": 8,
        "examples": [
            {
                "word": "味方",
                "reading": "みかた",
                "meaning": "ally, supporter",
                "sentence": {
                    "japanese": "味方になりました。",
                    "romaji": "Mikata ni narimashita.",
                    "english": "I became an ally.",
                    "uzbek": "Ittifoqchi bo'ldim."
                }
            }
        ]
    },
    {
        "id": "n3-361",
        "kanji": "魅",
        "readings": {"on": ["み"], "kun": []},
        "meanings": ["charm", "fascinate", "attract"],
        "jlptLevel": "N3",
        "frequency": 361,
        "strokes": 15,
        "examples": [
            {
                "word": "魅了",
                "reading": "みりょう",
                "meaning": "fascination, charm",
                "sentence": {
                    "japanese": "魅了されました。",
                    "romaji": "Miryō saremashita.",
                    "english": "I was fascinated.",
                    "uzbek": "Jalb qildim."
                }
            }
        ]
    },
    {
        "id": "n3-362",
        "kanji": "密",
        "readings": {"on": ["みつ"], "kun": []},
        "meanings": ["dense", "secret", "intimate"],
        "jlptLevel": "N3",
        "frequency": 362,
        "strokes": 11,
        "examples": [
            {
                "word": "密度",
                "reading": "みつど",
                "meaning": "density",
                "sentence": {
                    "japanese": "密度を測りました。",
                    "romaji": "Mitsudo o hakari mashita.",
                    "english": "I measured the density.",
                    "uzbek": "Zichlikni o'lchadim."
                }
            }
        ]
    },
    {
        "id": "n3-363",
        "kanji": "脈",
        "readings": {"on": ["みゃく"], "kun": []},
        "meanings": ["pulse", "vein", "connection"],
        "jlptLevel": "N3",
        "frequency": 363,
        "strokes": 10,
        "examples": [
            {
                "word": "静脈",
                "reading": "じょうみゃく",
                "meaning": "vein",
                "sentence": {
                    "japanese": "静脈を調べました。",
                    "romaji": "Jōmyaku o shirabemashita.",
                    "english": "I examined the vein.",
                    "uzbek": "Venani tekshirdim."
                }
            }
        ]
    },
    {
        "id": "n3-364",
        "kanji": "妙",
        "readings": {"on": ["みょう"], "kun": []},
        "meanings": ["strange", "wonderful", "mysterious"],
        "jlptLevel": "N3",
        "frequency": 364,
        "strokes": 7,
        "examples": [
            {
                "word": "微妙",
                "reading": "びみょう",
                "meaning": "subtle, delicate",
                "sentence": {
                    "japanese": "微妙な違いです。",
                    "romaji": "Bimyō na chigai desu.",
                    "english": "It's a subtle difference.",
                    "uzbek": "Nozik farq."
                }
            }
        ]
    },
    {
        "id": "n3-365",
        "kanji": "民",
        "readings": {"on": ["みん"], "kun": ["たみ"]},
        "meanings": ["people", "citizens", "nation"],
        "jlptLevel": "N3",
        "frequency": 365,
        "strokes": 5,
        "examples": [
            {
                "word": "民主",
                "reading": "みんしゅ",
                "meaning": "democracy",
                "sentence": {
                    "japanese": "民主主義です。",
                    "romaji": "Minshu shugi desu.",
                    "english": "It's democracy.",
                    "uzbek": "Demokratiya."
                }
            }
        ]
    },
    {
        "id": "n3-366",
        "kanji": "眠",
        "readings": {"on": ["みん"], "kun": ["ねむる", "ねむい"]},
        "meanings": ["sleep", "drowsy"],
        "jlptLevel": "N3",
        "frequency": 366,
        "strokes": 10,
        "examples": [
            {
                "word": "不眠",
                "reading": "ふみん",
                "meaning": "insomnia, sleeplessness",
                "sentence": {
                    "japanese": "不眠症です。",
                    "romaji": "Fuminshō desu.",
                    "english": "I have insomnia.",
                    "uzbek": "Uyqusizlik kasalligi."
                }
            }
        ]
    },
    {
        "id": "n3-367",
        "kanji": "無",
        "readings": {"on": ["む"], "kun": ["ない"]},
        "meanings": ["nothing", "none", "without"],
        "jlptLevel": "N3",
        "frequency": 367,
        "strokes": 12,
        "examples": [
            {
                "word": "無料",
                "reading": "むりょう",
                "meaning": "free, no charge",
                "sentence": {
                    "japanese": "無料で使えます。",
                    "romaji": "Muryō de tsukaemasu.",
                    "english": "You can use it for free.",
                    "uzbek": "Bepul ishlatish mumkin."
                }
            }
        ]
    },
    {
        "id": "n3-368",
        "kanji": "夢",
        "readings": {"on": ["む"], "kun": ["ゆめ"]},
        "meanings": ["dream", "vision"],
        "jlptLevel": "N3",
        "frequency": 368,
        "strokes": 13,
        "examples": [
            {
                "word": "悪夢",
                "reading": "あくむ",
                "meaning": "nightmare",
                "sentence": {
                    "japanese": "悪夢を見ました。",
                    "romaji": "Akumu o mimashita.",
                    "english": "I had a nightmare.",
                    "uzbek": "Qo'rqinchli tush ko'rdim."
                }
            }
        ]
    },
    {
        "id": "n3-369",
        "kanji": "霧",
        "readings": {"on": ["む"], "kun": ["きり"]},
        "meanings": ["fog", "mist"],
        "jlptLevel": "N3",
        "frequency": 369,
        "strokes": 19,
        "examples": [
            {
                "word": "霧雨",
                "reading": "きりさめ",
                "meaning": "drizzle, misty rain",
                "sentence": {
                    "japanese": "霧雨が降りました。",
                    "romaji": "Kirisame ga furimashita.",
                    "english": "It drizzled.",
                    "uzbek": "Yengil yomg'ir yog'di."
                }
            }
        ]
    },
    {
        "id": "n3-370",
        "kanji": "娘",
        "readings": {"on": ["じょう"], "kun": ["むすめ"]},
        "meanings": ["daughter", "girl"],
        "jlptLevel": "N3",
        "frequency": 370,
        "strokes": 10,
        "examples": [
            {
                "word": "長女",
                "reading": "ちょうじょ",
                "meaning": "eldest daughter",
                "sentence": {
                    "japanese": "長女がいます。",
                    "romaji": "Chōjo ga imasu.",
                    "english": "I have an eldest daughter.",
                    "uzbek": "Katta qizim bor."
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
print('🎉 N3 LEVEL COMPLETE! All 370 kanji added!')
