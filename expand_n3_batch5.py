#!/usr/bin/env python3
import json

# Read existing N3 data
with open('src/data/kanji/n3-complete.json', 'r', encoding='utf-8') as f:
    n3_data = json.load(f)

print(f'Current N3 kanji count: {len(n3_data)}')

# Additional N3 kanji data (243-292)
additional_kanji = [
    {
        "id": "n3-243",
        "kanji": "白",
        "readings": {"on": ["はく"], "kun": ["しろ", "しろい"]},
        "meanings": ["white", "blank"],
        "jlptLevel": "N3",
        "frequency": 243,
        "strokes": 5,
        "examples": [
            {
                "word": "白紙",
                "reading": "はくし",
                "meaning": "blank paper",
                "sentence": {
                    "japanese": "白紙に書きました。",
                    "romaji": "Hakushi ni kakimashita.",
                    "english": "I wrote on blank paper.",
                    "uzbek": "Oq qog'ozga yozdim."
                }
            }
        ]
    },
    {
        "id": "n3-244",
        "kanji": "百",
        "readings": {"on": ["ひゃく"], "kun": []},
        "meanings": ["hundred", "100"],
        "jlptLevel": "N3",
        "frequency": 244,
        "strokes": 6,
        "examples": [
            {
                "word": "百円",
                "reading": "ひゃくえん",
                "meaning": "100 yen",
                "sentence": {
                    "japanese": "百円を払いました。",
                    "romaji": "Hyaku-en o haraimashita.",
                    "english": "I paid 100 yen.",
                    "uzbek": "100 yenni to'ladim."
                }
            }
        ]
    },
    {
        "id": "n3-245",
        "kanji": "発",
        "readings": {"on": ["はつ"], "kun": ["はつ"]},
        "meanings": ["departure", "start", "emit"],
        "jlptLevel": "N3",
        "frequency": 245,
        "strokes": 9,
        "examples": [
            {
                "word": "出発",
                "reading": "しゅっぱつ",
                "meaning": "departure",
                "sentence": {
                    "japanese": "出発しました。",
                    "romaji": "Shuppatsu shimashita.",
                    "english": "I departed.",
                    "uzbek": "Yo'lga chiqdim."
                }
            }
        ]
    },
    {
        "id": "n3-246",
        "kanji": "反",
        "readings": {"on": ["はん"], "kun": ["そる"]},
        "meanings": ["opposite", "against", "reverse"],
        "jlptLevel": "N3",
        "frequency": 246,
        "strokes": 4,
        "examples": [
            {
                "word": "反対",
                "reading": "はんたい",
                "meaning": "opposition, against",
                "sentence": {
                    "japanese": "反対しました。",
                    "romaji": "Hantai shimashita.",
                    "english": "I opposed.",
                    "uzbek": "Qarshi chiqdim."
                }
            }
        ]
    },
    {
        "id": "n3-247",
        "kanji": "半",
        "readings": {"on": ["はん"], "kun": ["なかば"]},
        "meanings": ["half", "middle"],
        "jlptLevel": "N3",
        "frequency": 247,
        "strokes": 5,
        "examples": [
            {
                "word": "半分",
                "reading": "はんぶん",
                "meaning": "half",
                "sentence": {
                    "japanese": "半分食べました。",
                    "romaji": "Hanbun tabemashita.",
                    "english": "I ate half.",
                    "uzbek": "Yarmini yedim."
                }
            }
        ]
    },
    {
        "id": "n3-248",
        "kanji": "判",
        "readings": {"on": ["はん"], "kun": ["わかる"]},
        "meanings": ["judge", "decide", "seal"],
        "jlptLevel": "N3",
        "frequency": 248,
        "strokes": 7,
        "examples": [
            {
                "word": "判断",
                "reading": "はんだん",
                "meaning": "judgment, decision",
                "sentence": {
                    "japanese": "判断を下しました。",
                    "romaji": "Handan o kudashimashita.",
                    "english": "I made a judgment.",
                    "uzbek": "Hukm chiqardim."
                }
            }
        ]
    },
    {
        "id": "n3-249",
        "kanji": "版",
        "readings": {"on": ["はん"], "kun": []},
        "meanings": ["edition", "version", "printing"],
        "jlptLevel": "N3",
        "frequency": 249,
        "strokes": 8,
        "examples": [
            {
                "word": "新版",
                "reading": "しんぱん",
                "meaning": "new edition",
                "sentence": {
                    "japanese": "新版を買いました。",
                    "romaji": "Shinpan o kaimashita.",
                    "english": "I bought the new edition.",
                    "uzbek": "Yangi nashrni sotib oldim."
                }
            }
        ]
    },
    {
        "id": "n3-250",
        "kanji": "犯",
        "readings": {"on": ["はん"], "kun": ["おかす"]},
        "meanings": ["crime", "offense", "commit"],
        "jlptLevel": "N3",
        "frequency": 250,
        "strokes": 5,
        "examples": [
            {
                "word": "犯罪",
                "reading": "はんざい",
                "meaning": "crime",
                "sentence": {
                    "japanese": "犯罪を防ぎました。",
                    "romaji": "Hanzai o fusagimashita.",
                    "english": "I prevented crime.",
                    "uzbek": "Jinoyatni oldini oldim."
                }
            }
        ]
    },
    {
        "id": "n3-251",
        "kanji": "飯",
        "readings": {"on": ["はん"], "kun": ["めし"]},
        "meanings": ["meal", "rice", "food"],
        "jlptLevel": "N3",
        "frequency": 251,
        "strokes": 12,
        "examples": [
            {
                "word": "朝飯",
                "reading": "あさめし",
                "meaning": "breakfast",
                "sentence": {
                    "japanese": "朝飯を食べました。",
                    "romaji": "Asameshi o tabemashita.",
                    "english": "I ate breakfast.",
                    "uzbek": "Nonushtani yedim."
                }
            }
        ]
    },
    {
        "id": "n3-252",
        "kanji": "晩",
        "readings": {"on": ["ばん"], "kun": []},
        "meanings": ["evening", "night"],
        "jlptLevel": "N3",
        "frequency": 252,
        "strokes": 12,
        "examples": [
            {
                "word": "晩飯",
                "reading": "ばんめし",
                "meaning": "dinner",
                "sentence": {
                    "japanese": "晩飯を食べました。",
                    "romaji": "Banmeshi o tabemashita.",
                    "english": "I ate dinner.",
                    "uzbek": "Kechki ovqatni yedim."
                }
            }
        ]
    },
    {
        "id": "n3-253",
        "kanji": "番",
        "readings": {"on": ["ばん"], "kun": []},
        "meanings": ["number", "turn", "guard"],
        "jlptLevel": "N3",
        "frequency": 253,
        "strokes": 12,
        "examples": [
            {
                "word": "番号",
                "reading": "ばんごう",
                "meaning": "number",
                "sentence": {
                    "japanese": "番号を覚えました。",
                    "romaji": "Bangō o oboemashita.",
                    "english": "I memorized the number.",
                    "uzbek": "Raqamni yodladim."
                }
            }
        ]
    },
    {
        "id": "n3-254",
        "kanji": "美",
        "readings": {"on": ["び"], "kun": ["うつくしい"]},
        "meanings": ["beautiful", "beauty"],
        "jlptLevel": "N3",
        "frequency": 254,
        "strokes": 9,
        "examples": [
            {
                "word": "美人",
                "reading": "びじん",
                "meaning": "beautiful woman",
                "sentence": {
                    "japanese": "美人を見ました。",
                    "romaji": "Bijin o mimashita.",
                    "english": "I saw a beautiful woman.",
                    "uzbek": "Chiroyli ayolni ko'rdim."
                }
            }
        ]
    },
    {
        "id": "n3-255",
        "kanji": "備",
        "readings": {"on": ["び"], "kun": ["そなえる"]},
        "meanings": ["prepare", "equip", "provide"],
        "jlptLevel": "N3",
        "frequency": 255,
        "strokes": 12,
        "examples": [
            {
                "word": "準備",
                "reading": "じゅんび",
                "meaning": "preparation",
                "sentence": {
                    "japanese": "準備をしました。",
                    "romaji": "Junbi o shimashita.",
                    "english": "I prepared.",
                    "uzbek": "Tayyorlandim."
                }
            }
        ]
    },
    {
        "id": "n3-256",
        "kanji": "尾",
        "readings": {"on": ["び"], "kun": ["お"]},
        "meanings": ["tail", "end"],
        "jlptLevel": "N3",
        "frequency": 256,
        "strokes": 7,
        "examples": [
            {
                "word": "尻尾",
                "reading": "しっぽ",
                "meaning": "tail",
                "sentence": {
                    "japanese": "尻尾を振りました。",
                    "romaji": "Shippo o furimashita.",
                    "english": "I wagged my tail.",
                    "uzbek": "Dumimni silkitdim."
                }
            }
        ]
    },
    {
        "id": "n3-257",
        "kanji": "微",
        "readings": {"on": ["び"], "kun": []},
        "meanings": ["minute", "subtle", "micro"],
        "jlptLevel": "N3",
        "frequency": 257,
        "strokes": 13,
        "examples": [
            {
                "word": "微細",
                "reading": "びさい",
                "meaning": "minute, fine",
                "sentence": {
                    "japanese": "微細な違いです。",
                    "romaji": "Bisai na chigai desu.",
                    "english": "It's a minute difference.",
                    "uzbek": "Juda kichik farq."
                }
            }
        ]
    },
    {
        "id": "n3-258",
        "kanji": "鼻",
        "readings": {"on": ["び"], "kun": ["はな"]},
        "meanings": ["nose"],
        "jlptLevel": "N3",
        "frequency": 258,
        "strokes": 14,
        "examples": [
            {
                "word": "鼻水",
                "reading": "はなみず",
                "meaning": "runny nose",
                "sentence": {
                    "japanese": "鼻水が出ました。",
                    "romaji": "Hanamizu ga demashita.",
                    "english": "My nose is running.",
                    "uzbek": "Burundan suv oqdi."
                }
            }
        ]
    },
    {
        "id": "n3-259",
        "kanji": "比",
        "readings": {"on": ["ひ"], "kun": ["くらべる"]},
        "meanings": ["compare", "ratio", "proportion"],
        "jlptLevel": "N3",
        "frequency": 259,
        "strokes": 4,
        "examples": [
            {
                "word": "比較",
                "reading": "ひかく",
                "meaning": "comparison",
                "sentence": {
                    "japanese": "比較しました。",
                    "romaji": "Hikaku shimashita.",
                    "english": "I compared.",
                    "uzbek": "Solishtirdim."
                }
            }
        ]
    },
    {
        "id": "n3-260",
        "kanji": "皮",
        "readings": {"on": ["ひ"], "kun": ["かわ"]},
        "meanings": ["skin", "leather", "peel"],
        "jlptLevel": "N3",
        "frequency": 260,
        "strokes": 5,
        "examples": [
            {
                "word": "皮膚",
                "reading": "ひふ",
                "meaning": "skin",
                "sentence": {
                    "japanese": "皮膚をケアしました。",
                    "romaji": "Hifu o kea shimashita.",
                    "english": "I took care of my skin.",
                    "uzbek": "Terimni parvarish qildim."
                }
            }
        ]
    },
    {
        "id": "n3-261",
        "kanji": "疲",
        "readings": {"on": ["ひ"], "kun": ["つかれる"]},
        "meanings": ["tired", "exhausted"],
        "jlptLevel": "N3",
        "frequency": 261,
        "strokes": 10,
        "examples": [
            {
                "word": "疲労",
                "reading": "ひろう",
                "meaning": "fatigue, tiredness",
                "sentence": {
                    "japanese": "疲労を感じました。",
                    "romaji": "Hirō o kanjimashita.",
                    "english": "I felt fatigue.",
                    "uzbek": "Charchoqni his qildim."
                }
            }
        ]
    },
    {
        "id": "n3-262",
        "kanji": "被",
        "readings": {"on": ["ひ"], "kun": ["こうむる"]},
        "meanings": ["suffer", "receive", "wear"],
        "jlptLevel": "N3",
        "frequency": 262,
        "strokes": 10,
        "examples": [
            {
                "word": "被害",
                "reading": "ひがい",
                "meaning": "damage, harm",
                "sentence": {
                    "japanese": "被害を受けました。",
                    "romaji": "Higai o ukemashita.",
                    "english": "I suffered damage.",
                    "uzbek": "Zarar ko'rdim."
                }
            }
        ]
    },
    {
        "id": "n3-263",
        "kanji": "費",
        "readings": {"on": ["ひ"], "kun": ["ついやす"]},
        "meanings": ["expense", "cost", "spend"],
        "jlptLevel": "N3",
        "frequency": 263,
        "strokes": 12,
        "examples": [
            {
                "word": "費用",
                "reading": "ひよう",
                "meaning": "expense, cost",
                "sentence": {
                    "japanese": "費用を計算しました。",
                    "romaji": "Hiyō o keisan shimashita.",
                    "english": "I calculated the cost.",
                    "uzbek": "Xarajatni hisobladim."
                }
            }
        ]
    },
    {
        "id": "n3-264",
        "kanji": "避",
        "readings": {"on": ["ひ"], "kun": ["さける"]},
        "meanings": ["avoid", "evade", "escape"],
        "jlptLevel": "N3",
        "frequency": 264,
        "strokes": 16,
        "examples": [
            {
                "word": "回避",
                "reading": "かいひ",
                "meaning": "avoidance, evasion",
                "sentence": {
                    "japanese": "回避しました。",
                    "romaji": "Kaihi shimashita.",
                    "english": "I avoided it.",
                    "uzbek": "Qochib o'tdim."
                }
            }
        ]
    },
    {
        "id": "n3-265",
        "kanji": "非",
        "readings": {"on": ["ひ"], "kun": []},
        "meanings": ["not", "non-", "un-"],
        "jlptLevel": "N3",
        "frequency": 265,
        "strokes": 8,
        "examples": [
            {
                "word": "非常",
                "reading": "ひじょう",
                "meaning": "emergency, unusual",
                "sentence": {
                    "japanese": "非常事態です。",
                    "romaji": "Hijō jitai desu.",
                    "english": "It's an emergency.",
                    "uzbek": "Favqulodda vaziyat."
                }
            }
        ]
    },
    {
        "id": "n3-266",
        "kanji": "飛",
        "readings": {"on": ["ひ"], "kun": ["とぶ"]},
        "meanings": ["fly", "jump", "leap"],
        "jlptLevel": "N3",
        "frequency": 266,
        "strokes": 9,
        "examples": [
            {
                "word": "飛行",
                "reading": "ひこう",
                "meaning": "flight, flying",
                "sentence": {
                    "japanese": "飛行機で飛びました。",
                    "romaji": "Hikōki de tobimashita.",
                    "english": "I flew by plane.",
                    "uzbek": "Samolyotda uchdim."
                }
            }
        ]
    },
    {
        "id": "n3-267",
        "kanji": "表",
        "readings": {"on": ["ひょう"], "kun": ["おもて", "あらわす"]},
        "meanings": ["surface", "table", "express"],
        "jlptLevel": "N3",
        "frequency": 267,
        "strokes": 8,
        "examples": [
            {
                "word": "表現",
                "reading": "ひょうげん",
                "meaning": "expression",
                "sentence": {
                    "japanese": "表現しました。",
                    "romaji": "Hyōgen shimashita.",
                    "english": "I expressed it.",
                    "uzbek": "Ifoda qildim."
                }
            }
        ]
    },
    {
        "id": "n3-268",
        "kanji": "評",
        "readings": {"on": ["ひょう"], "kun": []},
        "meanings": ["evaluate", "comment", "criticism"],
        "jlptLevel": "N3",
        "frequency": 268,
        "strokes": 12,
        "examples": [
            {
                "word": "評価",
                "reading": "ひょうか",
                "meaning": "evaluation, assessment",
                "sentence": {
                    "japanese": "評価をしました。",
                    "romaji": "Hyōka o shimashita.",
                    "english": "I evaluated it.",
                    "uzbek": "Baholadim."
                }
            }
        ]
    },
    {
        "id": "n3-269",
        "kanji": "標",
        "readings": {"on": ["ひょう"], "kun": ["しるし"]},
        "meanings": ["mark", "sign", "target"],
        "jlptLevel": "N3",
        "frequency": 269,
        "strokes": 15,
        "examples": [
            {
                "word": "目標",
                "reading": "もくひょう",
                "meaning": "goal, target",
                "sentence": {
                    "japanese": "目標を設定しました。",
                    "romaji": "Mokuhyō o settei shimashita.",
                    "english": "I set a goal.",
                    "uzbek": "Maqsadni belgiladim."
                }
            }
        ]
    },
    {
        "id": "n3-270",
        "kanji": "病",
        "readings": {"on": ["びょう"], "kun": ["やまい"]},
        "meanings": ["illness", "disease", "sick"],
        "jlptLevel": "N3",
        "frequency": 270,
        "strokes": 10,
        "examples": [
            {
                "word": "病気",
                "reading": "びょうき",
                "meaning": "illness, disease",
                "sentence": {
                    "japanese": "病気になりました。",
                    "romaji": "Byōki ni narimashita.",
                    "english": "I became ill.",
                    "uzbek": "Kasallandim."
                }
            }
        ]
    },
    {
        "id": "n3-271",
        "kanji": "秒",
        "readings": {"on": ["びょう"], "kun": []},
        "meanings": ["second", "moment"],
        "jlptLevel": "N3",
        "frequency": 271,
        "strokes": 9,
        "examples": [
            {
                "word": "秒速",
                "reading": "びょうそく",
                "meaning": "speed per second",
                "sentence": {
                    "japanese": "秒速を測りました。",
                    "romaji": "Byōsoku o hakari mashita.",
                    "english": "I measured the speed per second.",
                    "uzbek": "Soniyada tezlikni o'lchadim."
                }
            }
        ]
    },
    {
        "id": "n3-272",
        "kanji": "氷",
        "readings": {"on": ["ひょう"], "kun": ["こおり"]},
        "meanings": ["ice"],
        "jlptLevel": "N3",
        "frequency": 272,
        "strokes": 5,
        "examples": [
            {
                "word": "氷水",
                "reading": "こおりみず",
                "meaning": "ice water",
                "sentence": {
                    "japanese": "氷水を飲みました。",
                    "romaji": "Kōrimizu o nomimashita.",
                    "english": "I drank ice water.",
                    "uzbek": "Muzli suvni ichdim."
                }
            }
        ]
    },
    {
        "id": "n3-273",
        "kanji": "平",
        "readings": {"on": ["へい"], "kun": ["たいら", "ひら"]},
        "meanings": ["flat", "peace", "level"],
        "jlptLevel": "N3",
        "frequency": 273,
        "strokes": 5,
        "examples": [
            {
                "word": "平和",
                "reading": "へいわ",
                "meaning": "peace",
                "sentence": {
                    "japanese": "平和を願います。",
                    "romaji": "Heiwa o negaimasu.",
                    "english": "I wish for peace.",
                    "uzbek": "Tinchlikni tilayman."
                }
            }
        ]
    },
    {
        "id": "n3-274",
        "kanji": "兵",
        "readings": {"on": ["へい"], "kun": []},
        "meanings": ["soldier", "army", "war"],
        "jlptLevel": "N3",
        "frequency": 274,
        "strokes": 7,
        "examples": [
            {
                "word": "兵士",
                "reading": "へいし",
                "meaning": "soldier",
                "sentence": {
                    "japanese": "兵士になりました。",
                    "romaji": "Heishi ni narimashita.",
                    "english": "I became a soldier.",
                    "uzbek": "Askar bo'ldim."
                }
            }
        ]
    },
    {
        "id": "n3-275",
        "kanji": "閉",
        "readings": {"on": ["へい"], "kun": ["とじる", "しめる"]},
        "meanings": ["close", "shut", "end"],
        "jlptLevel": "N3",
        "frequency": 275,
        "strokes": 11,
        "examples": [
            {
                "word": "閉店",
                "reading": "へいてん",
                "meaning": "closing, closed",
                "sentence": {
                    "japanese": "閉店しました。",
                    "romaji": "Heiten shimashita.",
                    "english": "The store closed.",
                    "uzbek": "Do'kon yopildi."
                }
            }
        ]
    },
    {
        "id": "n3-276",
        "kanji": "辺",
        "readings": {"on": ["へん"], "kun": ["あたり"]},
        "meanings": ["area", "vicinity", "side"],
        "jlptLevel": "N3",
        "frequency": 276,
        "strokes": 5,
        "examples": [
            {
                "word": "周辺",
                "reading": "しゅうへん",
                "meaning": "surroundings, vicinity",
                "sentence": {
                    "japanese": "周辺を調べました。",
                    "romaji": "Shūhen o shirabemashita.",
                    "english": "I investigated the surroundings.",
                    "uzbek": "Atroflarni tekshirdim."
                }
            }
        ]
    },
    {
        "id": "n3-277",
        "kanji": "変",
        "readings": {"on": ["へん"], "kun": ["かわる", "かえる"]},
        "meanings": ["change", "strange", "different"],
        "jlptLevel": "N3",
        "frequency": 277,
        "strokes": 9,
        "examples": [
            {
                "word": "変化",
                "reading": "へんか",
                "meaning": "change, variation",
                "sentence": {
                    "japanese": "変化がありました。",
                    "romaji": "Henka ga arimashita.",
                    "english": "There was a change.",
                    "uzbek": "O'zgarish bo'ldi."
                }
            }
        ]
    },
    {
        "id": "n3-278",
        "kanji": "片",
        "readings": {"on": ["へん"], "kun": ["かた"]},
        "meanings": ["one side", "piece", "fragment"],
        "jlptLevel": "N3",
        "frequency": 278,
        "strokes": 4,
        "examples": [
            {
                "word": "片方",
                "reading": "かたほう",
                "meaning": "one side",
                "sentence": {
                    "japanese": "片方を見ました。",
                    "romaji": "Katahō o mimashita.",
                    "english": "I looked at one side.",
                    "uzbek": "Bir tomonni ko'rdim."
                }
            }
        ]
    },
    {
        "id": "n3-279",
        "kanji": "編",
        "readings": {"on": ["へん"], "kun": ["あむ"]},
        "meanings": ["compile", "edit", "weave"],
        "jlptLevel": "N3",
        "frequency": 279,
        "strokes": 15,
        "examples": [
            {
                "word": "編集",
                "reading": "へんしゅう",
                "meaning": "editing, compilation",
                "sentence": {
                    "japanese": "編集をしました。",
                    "romaji": "Henshū o shimashita.",
                    "english": "I edited it.",
                    "uzbek": "Tahrir qildim."
                }
            }
        ]
    },
    {
        "id": "n3-280",
        "kanji": "返",
        "readings": {"on": ["へん"], "kun": ["かえる", "かえす"]},
        "meanings": ["return", "give back", "reply"],
        "jlptLevel": "N3",
        "frequency": 280,
        "strokes": 7,
        "examples": [
            {
                "word": "返事",
                "reading": "へんじ",
                "meaning": "reply, response",
                "sentence": {
                    "japanese": "返事をしました。",
                    "romaji": "Henji o shimashita.",
                    "english": "I replied.",
                    "uzbek": "Javob berdim."
                }
            }
        ]
    },
    {
        "id": "n3-281",
        "kanji": "便",
        "readings": {"on": ["べん"], "kun": ["たより"]},
        "meanings": ["convenience", "mail", "news"],
        "jlptLevel": "N3",
        "frequency": 281,
        "strokes": 9,
        "examples": [
            {
                "word": "便利",
                "reading": "べんり",
                "meaning": "convenient, useful",
                "sentence": {
                    "japanese": "便利な道具です。",
                    "romaji": "Benri na dōgu desu.",
                    "english": "It's a convenient tool.",
                    "uzbek": "Qulay asbob."
                }
            }
        ]
    },
    {
        "id": "n3-282",
        "kanji": "勉",
        "readings": {"on": ["べん"], "kun": []},
        "meanings": ["study", "diligent"],
        "jlptLevel": "N3",
        "frequency": 282,
        "strokes": 10,
        "examples": [
            {
                "word": "勉強",
                "reading": "べんきょう",
                "meaning": "study, learning",
                "sentence": {
                    "japanese": "勉強をしました。",
                    "romaji": "Benkyō o shimashita.",
                    "english": "I studied.",
                    "uzbek": "O'qidim."
                }
            }
        ]
    },
    {
        "id": "n3-283",
        "kanji": "歩",
        "readings": {"on": ["ほ"], "kun": ["あるく", "あゆむ"]},
        "meanings": ["walk", "step", "progress"],
        "jlptLevel": "N3",
        "frequency": 283,
        "strokes": 8,
        "examples": [
            {
                "word": "散歩",
                "reading": "さんぽ",
                "meaning": "walk, stroll",
                "sentence": {
                    "japanese": "散歩をしました。",
                    "romaji": "Sanpo o shimashita.",
                    "english": "I took a walk.",
                    "uzbek": "Sayr qildim."
                }
            }
        ]
    },
    {
        "id": "n3-284",
        "kanji": "保",
        "readings": {"on": ["ほ"], "kun": ["たもつ"]},
        "meanings": ["maintain", "preserve", "guarantee"],
        "jlptLevel": "N3",
        "frequency": 284,
        "strokes": 9,
        "examples": [
            {
                "word": "保持",
                "reading": "ほじ",
                "meaning": "maintenance, preservation",
                "sentence": {
                    "japanese": "保持しました。",
                    "romaji": "Hoji shimashita.",
                    "english": "I maintained it.",
                    "uzbek": "Saqladim."
                }
            }
        ]
    },
    {
        "id": "n3-285",
        "kanji": "補",
        "readings": {"on": ["ほ"], "kun": ["おぎなう"]},
        "meanings": ["supplement", "compensate", "repair"],
        "jlptLevel": "N3",
        "frequency": 285,
        "strokes": 12,
        "examples": [
            {
                "word": "補充",
                "reading": "ほじゅう",
                "meaning": "supplement, replenishment",
                "sentence": {
                    "japanese": "補充しました。",
                    "romaji": "Hojū shimashita.",
                    "english": "I replenished it.",
                    "uzbek": "To'ldirdim."
                }
            }
        ]
    },
    {
        "id": "n3-286",
        "kanji": "報",
        "readings": {"on": ["ほう"], "kun": ["むくいる"]},
        "meanings": ["report", "news", "reward"],
        "jlptLevel": "N3",
        "frequency": 286,
        "strokes": 12,
        "examples": [
            {
                "word": "報告",
                "reading": "ほうこく",
                "meaning": "report",
                "sentence": {
                    "japanese": "報告をしました。",
                    "romaji": "Hōkoku o shimashita.",
                    "english": "I made a report.",
                    "uzbek": "Hisobot berdim."
                }
            }
        ]
    },
    {
        "id": "n3-287",
        "kanji": "放",
        "readings": {"on": ["ほう"], "kun": ["はなす", "はなつ"]},
        "meanings": ["release", "let go", "broadcast"],
        "jlptLevel": "N3",
        "frequency": 287,
        "strokes": 8,
        "examples": [
            {
                "word": "放送",
                "reading": "ほうそう",
                "meaning": "broadcast, transmission",
                "sentence": {
                    "japanese": "放送を聞きました。",
                    "romaji": "Hōsō o kikimashita.",
                    "english": "I listened to the broadcast.",
                    "uzbek": "Eshitdim."
                }
            }
        ]
    },
    {
        "id": "n3-288",
        "kanji": "法",
        "readings": {"on": ["ほう"], "kun": []},
        "meanings": ["law", "method", "way"],
        "jlptLevel": "N3",
        "frequency": 288,
        "strokes": 8,
        "examples": [
            {
                "word": "法律",
                "reading": "ほうりつ",
                "meaning": "law, legislation",
                "sentence": {
                    "japanese": "法律を守りました。",
                    "romaji": "Hōritsu o mamorimashita.",
                    "english": "I obeyed the law.",
                    "uzbek": "Qonunni buzmadim."
                }
            }
        ]
    },
    {
        "id": "n3-289",
        "kanji": "訪",
        "readings": {"on": ["ほう"], "kun": ["おとずれる", "たずねる"]},
        "meanings": ["visit", "call on"],
        "jlptLevel": "N3",
        "frequency": 289,
        "strokes": 11,
        "examples": [
            {
                "word": "訪問",
                "reading": "ほうもん",
                "meaning": "visit",
                "sentence": {
                    "japanese": "訪問しました。",
                    "romaji": "Hōmon shimashita.",
                    "english": "I visited.",
                    "uzbek": "Tashrif buyurdim."
                }
            }
        ]
    },
    {
        "id": "n3-290",
        "kanji": "豊",
        "readings": {"on": ["ほう"], "kun": ["ゆたか"]},
        "meanings": ["abundant", "rich", "fertile"],
        "jlptLevel": "N3",
        "frequency": 290,
        "strokes": 13,
        "examples": [
            {
                "word": "豊富",
                "reading": "ほうふ",
                "meaning": "abundant, rich",
                "sentence": {
                    "japanese": "豊富な資源です。",
                    "romaji": "Hōfu na shigen desu.",
                    "english": "It's abundant resources.",
                    "uzbek": "Boy resurslar."
                }
            }
        ]
    },
    {
        "id": "n3-291",
        "kanji": "防",
        "readings": {"on": ["ぼう"], "kun": ["ふせぐ"]},
        "meanings": ["prevent", "defend", "protect"],
        "jlptLevel": "N3",
        "frequency": 291,
        "strokes": 7,
        "examples": [
            {
                "word": "防止",
                "reading": "ぼうし",
                "meaning": "prevention",
                "sentence": {
                    "japanese": "防止しました。",
                    "romaji": "Bōshi shimashita.",
                    "english": "I prevented it.",
                    "uzbek": "Oldini oldim."
                }
            }
        ]
    },
    {
        "id": "n3-292",
        "kanji": "忘",
        "readings": {"on": ["ぼう"], "kun": ["わすれる"]},
        "meanings": ["forget", "leave behind"],
        "jlptLevel": "N3",
        "frequency": 292,
        "strokes": 7,
        "examples": [
            {
                "word": "忘却",
                "reading": "ぼうきゃく",
                "meaning": "forgetting, oblivion",
                "sentence": {
                    "japanese": "忘却しました。",
                    "romaji": "Bōkyaku shimashita.",
                    "english": "I forgot.",
                    "uzbek": "Unutdim."
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
