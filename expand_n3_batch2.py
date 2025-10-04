#!/usr/bin/env python3
import json

# Read existing N3 data
with open('src/data/kanji/n3-complete.json', 'r', encoding='utf-8') as f:
    n3_data = json.load(f)

print(f'Current N3 kanji count: {len(n3_data)}')

# Additional N3 kanji data (93-142)
additional_kanji = [
    {
        "id": "n3-093",
        "kanji": "始",
        "readings": {"on": ["し"], "kun": ["はじめる", "はじまる"]},
        "meanings": ["begin", "start", "commence"],
        "jlptLevel": "N3",
        "frequency": 93,
        "strokes": 8,
        "examples": [
            {
                "word": "開始",
                "reading": "かいし",
                "meaning": "start, beginning",
                "sentence": {
                    "japanese": "会議を開始しました。",
                    "romaji": "Kaigi o kaishi shimashita.",
                    "english": "We started the meeting.",
                    "uzbek": "Yig'ilishni boshladik."
                }
            }
        ]
    },
    {
        "id": "n3-094",
        "kanji": "指",
        "readings": {"on": ["し"], "kun": ["ゆび", "さす"]},
        "meanings": ["finger", "point", "indicate"],
        "jlptLevel": "N3",
        "frequency": 94,
        "strokes": 9,
        "examples": [
            {
                "word": "指示",
                "reading": "しじ",
                "meaning": "instruction, direction",
                "sentence": {
                    "japanese": "指示に従いました。",
                    "romaji": "Shiji ni shitagaimashita.",
                    "english": "I followed the instructions.",
                    "uzbek": "Ko'rsatmalarga amal qildim."
                }
            }
        ]
    },
    {
        "id": "n3-095",
        "kanji": "歯",
        "readings": {"on": ["し"], "kun": ["は"]},
        "meanings": ["tooth", "teeth"],
        "jlptLevel": "N3",
        "frequency": 95,
        "strokes": 12,
        "examples": [
            {
                "word": "歯医者",
                "reading": "はいしゃ",
                "meaning": "dentist",
                "sentence": {
                    "japanese": "歯医者に行きました。",
                    "romaji": "Haisha ni ikimashita.",
                    "english": "I went to the dentist.",
                    "uzbek": "Tish shifokoriga bordim."
                }
            }
        ]
    },
    {
        "id": "n3-096",
        "kanji": "次",
        "readings": {"on": ["じ"], "kun": ["つぎ", "つぐ"]},
        "meanings": ["next", "following", "second"],
        "jlptLevel": "N3",
        "frequency": 96,
        "strokes": 6,
        "examples": [
            {
                "word": "次回",
                "reading": "じかい",
                "meaning": "next time",
                "sentence": {
                    "japanese": "次回また来ます。",
                    "romaji": "Jikai mata kimasu.",
                    "english": "I'll come again next time.",
                    "uzbek": "Keyingi safar yana kelaman."
                }
            }
        ]
    },
    {
        "id": "n3-097",
        "kanji": "治",
        "readings": {"on": ["じ", "ち"], "kun": ["なおる", "なおす"]},
        "meanings": ["cure", "heal", "govern"],
        "jlptLevel": "N3",
        "frequency": 97,
        "strokes": 8,
        "examples": [
            {
                "word": "治療",
                "reading": "ちりょう",
                "meaning": "treatment, therapy",
                "sentence": {
                    "japanese": "治療を受けました。",
                    "romaji": "Chiryō o ukemashita.",
                    "english": "I received treatment.",
                    "uzbek": "Davolanishni oldim."
                }
            }
        ]
    },
    {
        "id": "n3-098",
        "kanji": "辞",
        "readings": {"on": ["じ"], "kun": ["やめる", "ことば"]},
        "meanings": ["resign", "quit", "word"],
        "jlptLevel": "N3",
        "frequency": 98,
        "strokes": 13,
        "examples": [
            {
                "word": "辞書",
                "reading": "じしょ",
                "meaning": "dictionary",
                "sentence": {
                    "japanese": "辞書で調べました。",
                    "romaji": "Jisho de shirabemashita.",
                    "english": "I looked it up in the dictionary.",
                    "uzbek": "Lug'atda qidirdim."
                }
            }
        ]
    },
    {
        "id": "n3-099",
        "kanji": "式",
        "readings": {"on": ["しき"], "kun": []},
        "meanings": ["ceremony", "formula", "style"],
        "jlptLevel": "N3",
        "frequency": 99,
        "strokes": 6,
        "examples": [
            {
                "word": "結婚式",
                "reading": "けっこんしき",
                "meaning": "wedding ceremony",
                "sentence": {
                    "japanese": "結婚式に参加しました。",
                    "romaji": "Kekkonshiki ni sanka shimashita.",
                    "english": "I attended the wedding ceremony.",
                    "uzbek": "To'y marosimida qatnashdim."
                }
            }
        ]
    },
    {
        "id": "n3-100",
        "kanji": "識",
        "readings": {"on": ["しき"], "kun": []},
        "meanings": ["knowledge", "consciousness", "discriminate"],
        "jlptLevel": "N3",
        "frequency": 100,
        "strokes": 19,
        "examples": [
            {
                "word": "知識",
                "reading": "ちしき",
                "meaning": "knowledge",
                "sentence": {
                    "japanese": "知識を深めました。",
                    "romaji": "Chishiki o fukamemashita.",
                    "english": "I deepened my knowledge.",
                    "uzbek": "Bilimimni chuqurlashtirdim."
                }
            }
        ]
    },
    {
        "id": "n3-101",
        "kanji": "質",
        "readings": {"on": ["しつ"], "kun": ["たち"]},
        "meanings": ["quality", "substance", "nature"],
        "jlptLevel": "N3",
        "frequency": 101,
        "strokes": 15,
        "examples": [
            {
                "word": "品質",
                "reading": "ひんしつ",
                "meaning": "quality",
                "sentence": {
                    "japanese": "品質が良いです。",
                    "romaji": "Hinshitsu ga ii desu.",
                    "english": "The quality is good.",
                    "uzbek": "Sifat yaxshi."
                }
            }
        ]
    },
    {
        "id": "n3-102",
        "kanji": "実",
        "readings": {"on": ["じつ"], "kun": ["み", "みのる"]},
        "meanings": ["reality", "fruit", "actual"],
        "jlptLevel": "N3",
        "frequency": 102,
        "strokes": 8,
        "examples": [
            {
                "word": "実際",
                "reading": "じっさい",
                "meaning": "actually, in reality",
                "sentence": {
                    "japanese": "実際に試してみました。",
                    "romaji": "Jissai ni tameshite mimashita.",
                    "english": "I actually tried it.",
                    "uzbek": "Haqiqatda sinab ko'rdim."
                }
            }
        ]
    },
    {
        "id": "n3-103",
        "kanji": "写",
        "readings": {"on": ["しゃ"], "kun": ["うつす", "うつる"]},
        "meanings": ["copy", "photograph", "reflect"],
        "jlptLevel": "N3",
        "frequency": 103,
        "strokes": 5,
        "examples": [
            {
                "word": "写真",
                "reading": "しゃしん",
                "meaning": "photograph, picture",
                "sentence": {
                    "japanese": "写真を撮りました。",
                    "romaji": "Shashin o torimashita.",
                    "english": "I took a photograph.",
                    "uzbek": "Rasm oldim."
                }
            }
        ]
    },
    {
        "id": "n3-104",
        "kanji": "車",
        "readings": {"on": ["しゃ"], "kun": ["くるま"]},
        "meanings": ["car", "vehicle", "wheel"],
        "jlptLevel": "N3",
        "frequency": 104,
        "strokes": 7,
        "examples": [
            {
                "word": "電車",
                "reading": "でんしゃ",
                "meaning": "train",
                "sentence": {
                    "japanese": "電車で通勤しています。",
                    "romaji": "Densha de tsūkin shite imasu.",
                    "english": "I commute by train.",
                    "uzbek": "Poyezdda ishga boraman."
                }
            }
        ]
    },
    {
        "id": "n3-105",
        "kanji": "社",
        "readings": {"on": ["しゃ"], "kun": ["やしろ"]},
        "meanings": ["company", "society", "shrine"],
        "jlptLevel": "N3",
        "frequency": 105,
        "strokes": 7,
        "examples": [
            {
                "word": "会社",
                "reading": "かいしゃ",
                "meaning": "company, corporation",
                "sentence": {
                    "japanese": "会社で働いています。",
                    "romaji": "Kaisha de hataraite imasu.",
                    "english": "I work at a company.",
                    "uzbek": "Kompaniyada ishlayman."
                }
            }
        ]
    },
    {
        "id": "n3-106",
        "kanji": "者",
        "readings": {"on": ["しゃ"], "kun": ["もの"]},
        "meanings": ["person", "someone", "thing"],
        "jlptLevel": "N3",
        "frequency": 106,
        "strokes": 8,
        "examples": [
            {
                "word": "学者",
                "reading": "がくしゃ",
                "meaning": "scholar, academic",
                "sentence": {
                    "japanese": "学者になりたいです。",
                    "romaji": "Gakusha ni naritai desu.",
                    "english": "I want to become a scholar.",
                    "uzbek": "Olim bo'lishni xohlayman."
                }
            }
        ]
    },
    {
        "id": "n3-107",
        "kanji": "主",
        "readings": {"on": ["しゅ"], "kun": ["ぬし", "おも"]},
        "meanings": ["main", "master", "owner"],
        "jlptLevel": "N3",
        "frequency": 107,
        "strokes": 5,
        "examples": [
            {
                "word": "主人",
                "reading": "しゅじん",
                "meaning": "master, husband",
                "sentence": {
                    "japanese": "主人は医者です。",
                    "romaji": "Shujin wa isha desu.",
                    "english": "My husband is a doctor.",
                    "uzbek": "Er-im shifokor."
                }
            }
        ]
    },
    {
        "id": "n3-108",
        "kanji": "取",
        "readings": {"on": ["しゅ"], "kun": ["とる"]},
        "meanings": ["take", "get", "obtain"],
        "jlptLevel": "N3",
        "frequency": 108,
        "strokes": 8,
        "examples": [
            {
                "word": "取得",
                "reading": "しゅとく",
                "meaning": "acquisition, obtaining",
                "sentence": {
                    "japanese": "資格を取得しました。",
                    "romaji": "Shikaku o shutoku shimashita.",
                    "english": "I obtained a qualification.",
                    "uzbek": "Malakani oldim."
                }
            }
        ]
    },
    {
        "id": "n3-109",
        "kanji": "手",
        "readings": {"on": ["しゅ"], "kun": ["て"]},
        "meanings": ["hand", "method", "skill"],
        "jlptLevel": "N3",
        "frequency": 109,
        "strokes": 4,
        "examples": [
            {
                "word": "手段",
                "reading": "しゅだん",
                "meaning": "means, method",
                "sentence": {
                    "japanese": "手段を考えました。",
                    "romaji": "Shudan o kangaemashita.",
                    "english": "I thought about the means.",
                    "uzbek": "Usulni o'yladim."
                }
            }
        ]
    },
    {
        "id": "n3-110",
        "kanji": "守",
        "readings": {"on": ["しゅ"], "kun": ["まもる"]},
        "meanings": ["protect", "guard", "keep"],
        "jlptLevel": "N3",
        "frequency": 110,
        "strokes": 6,
        "examples": [
            {
                "word": "守衛",
                "reading": "しゅえい",
                "meaning": "guard, security",
                "sentence": {
                    "japanese": "守衛がいます。",
                    "romaji": "Shuei ga imasu.",
                    "english": "There is a guard.",
                    "uzbek": "Qo'riqchi bor."
                }
            }
        ]
    },
    {
        "id": "n3-111",
        "kanji": "首",
        "readings": {"on": ["しゅ"], "kun": ["くび"]},
        "meanings": ["neck", "head", "chief"],
        "jlptLevel": "N3",
        "frequency": 111,
        "strokes": 9,
        "examples": [
            {
                "word": "首相",
                "reading": "しゅしょう",
                "meaning": "prime minister",
                "sentence": {
                    "japanese": "首相が演説しました。",
                    "romaji": "Shushō ga enzetsu shimashita.",
                    "english": "The prime minister gave a speech.",
                    "uzbek": "Bosh vazir nutq so'zladi."
                }
            }
        ]
    },
    {
        "id": "n3-112",
        "kanji": "受",
        "readings": {"on": ["じゅ"], "kun": ["うける", "うかる"]},
        "meanings": ["receive", "accept", "pass"],
        "jlptLevel": "N3",
        "frequency": 112,
        "strokes": 8,
        "examples": [
            {
                "word": "受付",
                "reading": "うけつけ",
                "meaning": "reception, desk",
                "sentence": {
                    "japanese": "受付で手続きをしました。",
                    "romaji": "Uketsuke de tetsuzuki o shimashita.",
                    "english": "I completed procedures at the reception.",
                    "uzbek": "Qabulxonada ishlarni bajardim."
                }
            }
        ]
    },
    {
        "id": "n3-113",
        "kanji": "授",
        "readings": {"on": ["じゅ"], "kun": ["さずける"]},
        "meanings": ["give", "award", "teach"],
        "jlptLevel": "N3",
        "frequency": 113,
        "strokes": 11,
        "examples": [
            {
                "word": "授業",
                "reading": "じゅぎょう",
                "meaning": "lesson, class",
                "sentence": {
                    "japanese": "授業に参加しました。",
                    "romaji": "Jugyō ni sanka shimashita.",
                    "english": "I participated in the lesson.",
                    "uzbek": "Darsda qatnashdim."
                }
            }
        ]
    },
    {
        "id": "n3-114",
        "kanji": "準",
        "readings": {"on": ["じゅん"], "kun": []},
        "meanings": ["standard", "semi", "quasi"],
        "jlptLevel": "N3",
        "frequency": 114,
        "strokes": 13,
        "examples": [
            {
                "word": "準備",
                "reading": "じゅんび",
                "meaning": "preparation, readiness",
                "sentence": {
                    "japanese": "準備ができました。",
                    "romaji": "Junbi ga dekimashita.",
                    "english": "I'm ready.",
                    "uzbek": "Tayyor bo'ldim."
                }
            }
        ]
    },
    {
        "id": "n3-115",
        "kanji": "序",
        "readings": {"on": ["じょ"], "kun": []},
        "meanings": ["preface", "order", "sequence"],
        "jlptLevel": "N3",
        "frequency": 115,
        "strokes": 7,
        "examples": [
            {
                "word": "順序",
                "reading": "じゅんじょ",
                "meaning": "order, sequence",
                "sentence": {
                    "japanese": "順序を守りました。",
                    "romaji": "Junjo o mamorimashita.",
                    "english": "I followed the order.",
                    "uzbek": "Tartibni saqladim."
                }
            }
        ]
    },
    {
        "id": "n3-116",
        "kanji": "助",
        "readings": {"on": ["じょ"], "kun": ["たすける", "すけ"]},
        "meanings": ["help", "assist", "aid"],
        "jlptLevel": "N3",
        "frequency": 116,
        "strokes": 7,
        "examples": [
            {
                "word": "助言",
                "reading": "じょげん",
                "meaning": "advice, suggestion",
                "sentence": {
                    "japanese": "助言をもらいました。",
                    "romaji": "Jogen o moraimashita.",
                    "english": "I received advice.",
                    "uzbek": "Maslahat oldim."
                }
            }
        ]
    },
    {
        "id": "n3-117",
        "kanji": "女",
        "readings": {"on": ["じょ"], "kun": ["おんな", "め"]},
        "meanings": ["woman", "female", "daughter"],
        "jlptLevel": "N3",
        "frequency": 117,
        "strokes": 3,
        "examples": [
            {
                "word": "女性",
                "reading": "じょせい",
                "meaning": "woman, female",
                "sentence": {
                    "japanese": "女性の権利を守ります。",
                    "romaji": "Josei no kenri o mamorimasu.",
                    "english": "I protect women's rights.",
                    "uzbek": "Ayollar huquqlarini himoya qilaman."
                }
            }
        ]
    },
    {
        "id": "n3-118",
        "kanji": "小",
        "readings": {"on": ["しょう"], "kun": ["ちいさい", "こ"]},
        "meanings": ["small", "little", "minor"],
        "jlptLevel": "N3",
        "frequency": 118,
        "strokes": 3,
        "examples": [
            {
                "word": "小学生",
                "reading": "しょうがくせい",
                "meaning": "elementary school student",
                "sentence": {
                    "japanese": "小学生の時を思い出します。",
                    "romaji": "Shōgakusei no toki o omoidashimasu.",
                    "english": "I remember my elementary school days.",
                    "uzbek": "Boshlang'ich maktab davrini eslayman."
                }
            }
        ]
    },
    {
        "id": "n3-119",
        "kanji": "少",
        "readings": {"on": ["しょう"], "kun": ["すこし", "すくない"]},
        "meanings": ["few", "little", "less"],
        "jlptLevel": "N3",
        "frequency": 119,
        "strokes": 4,
        "examples": [
            {
                "word": "少年",
                "reading": "しょうねん",
                "meaning": "boy, youth",
                "sentence": {
                    "japanese": "少年は元気です。",
                    "romaji": "Shōnen wa genki desu.",
                    "english": "The boy is energetic.",
                    "uzbek": "Bola zo'r."
                }
            }
        ]
    },
    {
        "id": "n3-120",
        "kanji": "商",
        "readings": {"on": ["しょう"], "kun": ["あきなう"]},
        "meanings": ["commerce", "business", "trade"],
        "jlptLevel": "N3",
        "frequency": 120,
        "strokes": 11,
        "examples": [
            {
                "word": "商業",
                "reading": "しょうぎょう",
                "meaning": "commerce, business",
                "sentence": {
                    "japanese": "商業を学んでいます。",
                    "romaji": "Shōgyō o manande imasu.",
                    "english": "I'm studying commerce.",
                    "uzbek": "Savdo-sotiqni o'rganaman."
                }
            }
        ]
    },
    {
        "id": "n3-121",
        "kanji": "勝",
        "readings": {"on": ["しょう"], "kun": ["かつ", "まさる"]},
        "meanings": ["win", "victory", "excel"],
        "jlptLevel": "N3",
        "frequency": 121,
        "strokes": 12,
        "examples": [
            {
                "word": "勝利",
                "reading": "しょうり",
                "meaning": "victory, win",
                "sentence": {
                    "japanese": "勝利を収めました。",
                    "romaji": "Shōri o osamemashita.",
                    "english": "We achieved victory.",
                    "uzbek": "G'alabani qo'lga kiritdik."
                }
            }
        ]
    },
    {
        "id": "n3-122",
        "kanji": "消",
        "readings": {"on": ["しょう"], "kun": ["きえる", "けす"]},
        "meanings": ["extinguish", "disappear", "erase"],
        "jlptLevel": "N3",
        "frequency": 122,
        "strokes": 10,
        "examples": [
            {
                "word": "消火",
                "reading": "しょうか",
                "meaning": "fire extinguishing",
                "sentence": {
                    "japanese": "消火器を使いました。",
                    "romaji": "Shōkaki o tsukaimashita.",
                    "english": "I used a fire extinguisher.",
                    "uzbek": "O'chirgichni ishlatdim."
                }
            }
        ]
    },
    {
        "id": "n3-123",
        "kanji": "章",
        "readings": {"on": ["しょう"], "kun": []},
        "meanings": ["chapter", "section", "badge"],
        "jlptLevel": "N3",
        "frequency": 123,
        "strokes": 11,
        "examples": [
            {
                "word": "文章",
                "reading": "ぶんしょう",
                "meaning": "sentence, text",
                "sentence": {
                    "japanese": "文章を書きました。",
                    "romaji": "Bunshō o kakimashita.",
                    "english": "I wrote a sentence.",
                    "uzbek": "Jumla yozdim."
                }
            }
        ]
    },
    {
        "id": "n3-124",
        "kanji": "証",
        "readings": {"on": ["しょう"], "kun": ["あかし"]},
        "meanings": ["evidence", "proof", "certificate"],
        "jlptLevel": "N3",
        "frequency": 124,
        "strokes": 12,
        "examples": [
            {
                "word": "証明",
                "reading": "しょうめい",
                "meaning": "proof, certificate",
                "sentence": {
                    "japanese": "証明書をもらいました。",
                    "romaji": "Shōmeisho o moraimashita.",
                    "english": "I received a certificate.",
                    "uzbek": "Sertifikat oldim."
                }
            }
        ]
    },
    {
        "id": "n3-125",
        "kanji": "象",
        "readings": {"on": ["しょう"], "kun": ["ぞう"]},
        "meanings": ["elephant", "image", "phenomenon"],
        "jlptLevel": "N3",
        "frequency": 125,
        "strokes": 12,
        "examples": [
            {
                "word": "現象",
                "reading": "げんしょう",
                "meaning": "phenomenon",
                "sentence": {
                    "japanese": "現象を観察しました。",
                    "romaji": "Genshō o kansatsu shimashita.",
                    "english": "I observed the phenomenon.",
                    "uzbek": "Hodisani kuzatdim."
                }
            }
        ]
    },
    {
        "id": "n3-126",
        "kanji": "賞",
        "readings": {"on": ["しょう"], "kun": []},
        "meanings": ["prize", "award", "reward"],
        "jlptLevel": "N3",
        "frequency": 126,
        "strokes": 15,
        "examples": [
            {
                "word": "受賞",
                "reading": "じゅしょう",
                "meaning": "award, prize",
                "sentence": {
                    "japanese": "受賞しました。",
                    "romaji": "Jushō shimashita.",
                    "english": "I received an award.",
                    "uzbek": "Mukofot oldim."
                }
            }
        ]
    },
    {
        "id": "n3-127",
        "kanji": "上",
        "readings": {"on": ["じょう"], "kun": ["うえ", "うわ", "あがる"]},
        "meanings": ["up", "above", "upper"],
        "jlptLevel": "N3",
        "frequency": 127,
        "strokes": 3,
        "examples": [
            {
                "word": "上達",
                "reading": "じょうたつ",
                "meaning": "improvement, progress",
                "sentence": {
                    "japanese": "上達しました。",
                    "romaji": "Jōtatsu shimashita.",
                    "english": "I improved.",
                    "uzbek": "Yaxshiladim."
                }
            }
        ]
    },
    {
        "id": "n3-128",
        "kanji": "場",
        "readings": {"on": ["じょう"], "kun": ["ば"]},
        "meanings": ["place", "field", "scene"],
        "jlptLevel": "N3",
        "frequency": 128,
        "strokes": 12,
        "examples": [
            {
                "word": "場所",
                "reading": "ばしょ",
                "meaning": "place, location",
                "sentence": {
                    "japanese": "場所を教えてください。",
                    "romaji": "Basho o oshiete kudasai.",
                    "english": "Please tell me the place.",
                    "uzbek": "Joyni ayting."
                }
            }
        ]
    },
    {
        "id": "n3-129",
        "kanji": "常",
        "readings": {"on": ["じょう"], "kun": ["つね"]},
        "meanings": ["usual", "normal", "constant"],
        "jlptLevel": "N3",
        "frequency": 129,
        "strokes": 11,
        "examples": [
            {
                "word": "常識",
                "reading": "じょうしき",
                "meaning": "common sense",
                "sentence": {
                    "japanese": "常識を働かせました。",
                    "romaji": "Jōshiki o hatarakasemashita.",
                    "english": "I used common sense.",
                    "uzbek": "Saqlovchanlikni ishlatdim."
                }
            }
        ]
    },
    {
        "id": "n3-130",
        "kanji": "情",
        "readings": {"on": ["じょう"], "kun": ["なさけ"]},
        "meanings": ["emotion", "feeling", "sympathy"],
        "jlptLevel": "N3",
        "frequency": 130,
        "strokes": 11,
        "examples": [
            {
                "word": "感情",
                "reading": "かんじょう",
                "meaning": "emotion, feeling",
                "sentence": {
                    "japanese": "感情を表しました。",
                    "romaji": "Kanjō o arawashimashita.",
                    "english": "I expressed my feelings.",
                    "uzbek": "Hissiyotimni bildirdim."
                }
            }
        ]
    },
    {
        "id": "n3-131",
        "kanji": "条",
        "readings": {"on": ["じょう"], "kun": []},
        "meanings": ["article", "clause", "line"],
        "jlptLevel": "N3",
        "frequency": 131,
        "strokes": 7,
        "examples": [
            {
                "word": "条件",
                "reading": "じょうけん",
                "meaning": "condition, requirement",
                "sentence": {
                    "japanese": "条件を満たしました。",
                    "romaji": "Jōken o mitashimashita.",
                    "english": "I met the conditions.",
                    "uzbek": "Shartlarni bajardim."
                }
            }
        ]
    },
    {
        "id": "n3-132",
        "kanji": "状",
        "readings": {"on": ["じょう"], "kun": []},
        "meanings": ["condition", "state", "form"],
        "jlptLevel": "N3",
        "frequency": 132,
        "strokes": 7,
        "examples": [
            {
                "word": "状況",
                "reading": "じょうきょう",
                "meaning": "situation, condition",
                "sentence": {
                    "japanese": "状況を確認しました。",
                    "romaji": "Jōkyō o kakunin shimashita.",
                    "english": "I confirmed the situation.",
                    "uzbek": "Holatni tekshirdim."
                }
            }
        ]
    },
    {
        "id": "n3-133",
        "kanji": "職",
        "readings": {"on": ["しょく"], "kun": []},
        "meanings": ["job", "occupation", "work"],
        "jlptLevel": "N3",
        "frequency": 133,
        "strokes": 18,
        "examples": [
            {
                "word": "職業",
                "reading": "しょくぎょう",
                "meaning": "occupation, profession",
                "sentence": {
                    "japanese": "職業を選びました。",
                    "romaji": "Shokugyō o erabimashita.",
                    "english": "I chose an occupation.",
                    "uzbek": "Kasbni tanladim."
                }
            }
        ]
    },
    {
        "id": "n3-134",
        "kanji": "色",
        "readings": {"on": ["しょく"], "kun": ["いろ"]},
        "meanings": ["color", "complexion", "appearance"],
        "jlptLevel": "N3",
        "frequency": 134,
        "strokes": 6,
        "examples": [
            {
                "word": "色彩",
                "reading": "しきさい",
                "meaning": "color, coloring",
                "sentence": {
                    "japanese": "色彩が美しいです。",
                    "romaji": "Shikisai ga utsukushii desu.",
                    "english": "The colors are beautiful.",
                    "uzbek": "Ranglar chiroyli."
                }
            }
        ]
    },
    {
        "id": "n3-135",
        "kanji": "食",
        "readings": {"on": ["しょく"], "kun": ["たべる", "くう"]},
        "meanings": ["eat", "food", "meal"],
        "jlptLevel": "N3",
        "frequency": 135,
        "strokes": 9,
        "examples": [
            {
                "word": "食事",
                "reading": "しょくじ",
                "meaning": "meal, food",
                "sentence": {
                    "japanese": "食事をしました。",
                    "romaji": "Shokuji o shimashita.",
                    "english": "I had a meal.",
                    "uzbek": "Ovqatlandim."
                }
            }
        ]
    },
    {
        "id": "n3-136",
        "kanji": "心",
        "readings": {"on": ["しん"], "kun": ["こころ"]},
        "meanings": ["heart", "mind", "spirit"],
        "jlptLevel": "N3",
        "frequency": 136,
        "strokes": 4,
        "examples": [
            {
                "word": "心理",
                "reading": "しんり",
                "meaning": "psychology, mental state",
                "sentence": {
                    "japanese": "心理を理解しました。",
                    "romaji": "Shinri o rikai shimashita.",
                    "english": "I understood the psychology.",
                    "uzbek": "Psixologiyani tushundim."
                }
            }
        ]
    },
    {
        "id": "n3-137",
        "kanji": "新",
        "readings": {"on": ["しん"], "kun": ["あたらしい", "あらた"]},
        "meanings": ["new", "fresh", "recent"],
        "jlptLevel": "N3",
        "frequency": 137,
        "strokes": 13,
        "examples": [
            {
                "word": "新聞",
                "reading": "しんぶん",
                "meaning": "newspaper",
                "sentence": {
                    "japanese": "新聞を読みました。",
                    "romaji": "Shinbun o yomimashita.",
                    "english": "I read the newspaper.",
                    "uzbek": "Gazetani o'qidim."
                }
            }
        ]
    },
    {
        "id": "n3-138",
        "kanji": "親",
        "readings": {"on": ["しん"], "kun": ["おや", "したしい"]},
        "meanings": ["parent", "relative", "intimate"],
        "jlptLevel": "N3",
        "frequency": 138,
        "strokes": 16,
        "examples": [
            {
                "word": "親切",
                "reading": "しんせつ",
                "meaning": "kindness, gentle",
                "sentence": {
                    "japanese": "親切にしました。",
                    "romaji": "Shinsetsu ni shimashita.",
                    "english": "I was kind.",
                    "uzbek": "Mehribon bo'ldim."
                }
            }
        ]
    },
    {
        "id": "n3-139",
        "kanji": "信",
        "readings": {"on": ["しん"], "kun": []},
        "meanings": ["trust", "faith", "believe"],
        "jlptLevel": "N3",
        "frequency": 139,
        "strokes": 9,
        "examples": [
            {
                "word": "信用",
                "reading": "しんよう",
                "meaning": "trust, credit",
                "sentence": {
                    "japanese": "信用を得ました。",
                    "romaji": "Shin'yō o emashita.",
                    "english": "I gained trust.",
                    "uzbek": "Ishonch oldim."
                }
            }
        ]
    },
    {
        "id": "n3-140",
        "kanji": "進",
        "readings": {"on": ["しん"], "kun": ["すすむ", "すすめる"]},
        "meanings": ["advance", "progress", "proceed"],
        "jlptLevel": "N3",
        "frequency": 140,
        "strokes": 11,
        "examples": [
            {
                "word": "進歩",
                "reading": "しんぽ",
                "meaning": "progress, advancement",
                "sentence": {
                    "japanese": "進歩しました。",
                    "romaji": "Shinpo shimashita.",
                    "english": "I made progress.",
                    "uzbek": "Taraqqiy qildim."
                }
            }
        ]
    },
    {
        "id": "n3-141",
        "kanji": "深",
        "readings": {"on": ["しん"], "kun": ["ふかい", "ふかめる"]},
        "meanings": ["deep", "profound", "intense"],
        "jlptLevel": "N3",
        "frequency": 141,
        "strokes": 11,
        "examples": [
            {
                "word": "深刻",
                "reading": "しんこく",
                "meaning": "serious, severe",
                "sentence": {
                    "japanese": "深刻な問題です。",
                    "romaji": "Shinkoku na mondai desu.",
                    "english": "It's a serious problem.",
                    "uzbek": "Jiddiy muammo."
                }
            }
        ]
    },
    {
        "id": "n3-142",
        "kanji": "申",
        "readings": {"on": ["しん"], "kun": ["もうす", "もうし"]},
        "meanings": ["say", "tell", "report"],
        "jlptLevel": "N3",
        "frequency": 142,
        "strokes": 5,
        "examples": [
            {
                "word": "申し込み",
                "reading": "もうしこみ",
                "meaning": "application, registration",
                "sentence": {
                    "japanese": "申し込みをしました。",
                    "romaji": "Mōshikomi o shimashita.",
                    "english": "I submitted an application.",
                    "uzbek": "Ariza berdim."
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
