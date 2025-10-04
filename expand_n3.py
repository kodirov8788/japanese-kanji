#!/usr/bin/env python3
import json

# Read existing N3 data
with open('src/data/kanji/n3-complete.json', 'r', encoding='utf-8') as f:
    n3_data = json.load(f)

print(f'Current N3 kanji count: {len(n3_data)}')

# Additional N3 kanji data (43-92)
additional_kanji = [
    {
        "id": "n3-043",
        "kanji": "協",
        "readings": {"on": ["きょう"], "kun": []},
        "meanings": ["cooperation", "collaboration"],
        "jlptLevel": "N3",
        "frequency": 43,
        "strokes": 8,
        "examples": [
            {
                "word": "協力",
                "reading": "きょうりょく",
                "meaning": "cooperation",
                "sentence": {
                    "japanese": "協力して問題を解決しました。",
                    "romaji": "Kyōryoku shite mondai o kaiketsu shimashita.",
                    "english": "We solved the problem through cooperation.",
                    "uzbek": "Hamkorlik bilan muammoni hal qildik."
                }
            }
        ]
    },
    {
        "id": "n3-044",
        "kanji": "局",
        "readings": {"on": ["きょく"], "kun": []},
        "meanings": ["office", "bureau", "station"],
        "jlptLevel": "N3",
        "frequency": 44,
        "strokes": 7,
        "examples": [
            {
                "word": "郵便局",
                "reading": "ゆうびんきょく",
                "meaning": "post office",
                "sentence": {
                    "japanese": "郵便局で手紙を出しました。",
                    "romaji": "Yūbinkyoku de tegami o dashimashita.",
                    "english": "I sent a letter at the post office.",
                    "uzbek": "Pochta bo'limida xat yubordim."
                }
            }
        ]
    },
    {
        "id": "n3-045",
        "kanji": "極",
        "readings": {"on": ["きょく"], "kun": ["きわめる"]},
        "meanings": ["extreme", "pole", "ultimate"],
        "jlptLevel": "N3",
        "frequency": 45,
        "strokes": 12,
        "examples": [
            {
                "word": "北極",
                "reading": "ほっきょく",
                "meaning": "North Pole",
                "sentence": {
                    "japanese": "北極はとても寒いです。",
                    "romaji": "Hokkyoku wa totemo samui desu.",
                    "english": "The North Pole is very cold.",
                    "uzbek": "Shimoliy qutb juda sovuq."
                }
            }
        ]
    },
    {
        "id": "n3-046",
        "kanji": "禁",
        "readings": {"on": ["きん"], "kun": []},
        "meanings": ["prohibition", "ban", "forbid"],
        "jlptLevel": "N3",
        "frequency": 46,
        "strokes": 13,
        "examples": [
            {
                "word": "禁止",
                "reading": "きんし",
                "meaning": "prohibition, ban",
                "sentence": {
                    "japanese": "ここで喫煙は禁止です。",
                    "romaji": "Koko de kitsuen wa kinshi desu.",
                    "english": "Smoking is prohibited here.",
                    "uzbek": "Bu yerda chekish taqiqlangan."
                }
            }
        ]
    },
    {
        "id": "n3-047",
        "kanji": "均",
        "readings": {"on": ["きん"], "kun": ["ならす"]},
        "meanings": ["equal", "uniform", "average"],
        "jlptLevel": "N3",
        "frequency": 47,
        "strokes": 7,
        "examples": [
            {
                "word": "平均",
                "reading": "へいきん",
                "meaning": "average, mean",
                "sentence": {
                    "japanese": "平均点は80点でした。",
                    "romaji": "Heikin-ten wa hachijū-ten deshita.",
                    "english": "The average score was 80 points.",
                    "uzbek": "O'rtacha ball 80 edi."
                }
            }
        ]
    },
    {
        "id": "n3-048",
        "kanji": "勤",
        "readings": {"on": ["きん"], "kun": ["つとめる"]},
        "meanings": ["work", "serve", "diligent"],
        "jlptLevel": "N3",
        "frequency": 48,
        "strokes": 12,
        "examples": [
            {
                "word": "勤務",
                "reading": "きんむ",
                "meaning": "work, duty",
                "sentence": {
                    "japanese": "毎日勤務しています。",
                    "romaji": "Mainichi kinmu shite imasu.",
                    "english": "I work every day.",
                    "uzbek": "Har kuni ishlayman."
                }
            }
        ]
    },
    {
        "id": "n3-049",
        "kanji": "区",
        "readings": {"on": ["く"], "kun": []},
        "meanings": ["district", "ward", "section"],
        "jlptLevel": "N3",
        "frequency": 49,
        "strokes": 4,
        "examples": [
            {
                "word": "地区",
                "reading": "ちく",
                "meaning": "district, area",
                "sentence": {
                    "japanese": "この地区は静かです。",
                    "romaji": "Kono chiku wa shizuka desu.",
                    "english": "This district is quiet.",
                    "uzbek": "Bu hudud jimjit."
                }
            }
        ]
    },
    {
        "id": "n3-050",
        "kanji": "句",
        "readings": {"on": ["く"], "kun": []},
        "meanings": ["phrase", "clause", "haiku"],
        "jlptLevel": "N3",
        "frequency": 50,
        "strokes": 5,
        "examples": [
            {
                "word": "俳句",
                "reading": "はいく",
                "meaning": "haiku",
                "sentence": {
                    "japanese": "俳句を作りました。",
                    "romaji": "Haiku o tsukurimashita.",
                    "english": "I wrote a haiku.",
                    "uzbek": "Haiku yozdim."
                }
            }
        ]
    },
    {
        "id": "n3-051",
        "kanji": "苦",
        "readings": {"on": ["く"], "kun": ["くるしい", "にがい"]},
        "meanings": ["suffering", "pain", "bitter"],
        "jlptLevel": "N3",
        "frequency": 51,
        "strokes": 8,
        "examples": [
            {
                "word": "苦労",
                "reading": "くろう",
                "meaning": "hardship, trouble",
                "sentence": {
                    "japanese": "苦労して成功しました。",
                    "romaji": "Kurō shite seikō shimashita.",
                    "english": "I succeeded through hardship.",
                    "uzbek": "Qiyinchiliklar bilan muvaffaqiyatga erishdim."
                }
            }
        ]
    },
    {
        "id": "n3-052",
        "kanji": "具",
        "readings": {"on": ["ぐ"], "kun": ["そなえる"]},
        "meanings": ["tool", "equipment", "ingredient"],
        "jlptLevel": "N3",
        "frequency": 52,
        "strokes": 8,
        "examples": [
            {
                "word": "道具",
                "reading": "どうぐ",
                "meaning": "tool, implement",
                "sentence": {
                    "japanese": "道具を使って作業しました。",
                    "romaji": "Dōgu o tsukatte sagyō shimashita.",
                    "english": "I worked using tools.",
                    "uzbek": "Asboblar bilan ishladim."
                }
            }
        ]
    },
    {
        "id": "n3-053",
        "kanji": "組",
        "readings": {"on": ["そ"], "kun": ["くむ", "くみ"]},
        "meanings": ["group", "team", "assemble"],
        "jlptLevel": "N3",
        "frequency": 53,
        "strokes": 11,
        "examples": [
            {
                "word": "グループ",
                "reading": "グループ",
                "meaning": "group",
                "sentence": {
                    "japanese": "グループで活動しました。",
                    "romaji": "Gurūpu de katsudō shimashita.",
                    "english": "We worked as a group.",
                    "uzbek": "Guruh bo'lib faoliyat ko'rsatdik."
                }
            }
        ]
    },
    {
        "id": "n3-054",
        "kanji": "経",
        "readings": {"on": ["けい"], "kun": ["へる", "たつ"]},
        "meanings": ["pass", "experience", "manage"],
        "jlptLevel": "N3",
        "frequency": 54,
        "strokes": 11,
        "examples": [
            {
                "word": "経験",
                "reading": "けいけん",
                "meaning": "experience",
                "sentence": {
                    "japanese": "良い経験をしました。",
                    "romaji": "Ii keiken o shimashita.",
                    "english": "I had a good experience.",
                    "uzbek": "Yaxshi tajriba orttim."
                }
            }
        ]
    },
    {
        "id": "n3-055",
        "kanji": "計",
        "readings": {"on": ["けい"], "kun": ["はかる", "かぞえる"]},
        "meanings": ["plan", "calculate", "measure"],
        "jlptLevel": "N3",
        "frequency": 55,
        "strokes": 9,
        "examples": [
            {
                "word": "計画",
                "reading": "けいかく",
                "meaning": "plan, project",
                "sentence": {
                    "japanese": "計画を立てました。",
                    "romaji": "Keikaku o tatemashita.",
                    "english": "I made a plan.",
                    "uzbek": "Reja tuzdim."
                }
            }
        ]
    },
    {
        "id": "n3-056",
        "kanji": "係",
        "readings": {"on": ["けい"], "kun": ["かかり", "かかわる"]},
        "meanings": ["person in charge", "related", "connection"],
        "jlptLevel": "N3",
        "frequency": 56,
        "strokes": 9,
        "examples": [
            {
                "word": "関係",
                "reading": "かんけい",
                "meaning": "relationship, connection",
                "sentence": {
                    "japanese": "関係を深めました。",
                    "romaji": "Kankei o fukamemashita.",
                    "english": "We deepened our relationship.",
                    "uzbek": "Munosabatni chuqurlashtirdik."
                }
            }
        ]
    },
    {
        "id": "n3-057",
        "kanji": "結",
        "readings": {"on": ["けつ"], "kun": ["むすぶ", "ゆう"]},
        "meanings": ["tie", "bind", "conclude"],
        "jlptLevel": "N3",
        "frequency": 57,
        "strokes": 12,
        "examples": [
            {
                "word": "結果",
                "reading": "けっか",
                "meaning": "result, outcome",
                "sentence": {
                    "japanese": "結果を待っています。",
                    "romaji": "Kekka o matte imasu.",
                    "english": "I'm waiting for the result.",
                    "uzbek": "Natijani kutaman."
                }
            }
        ]
    },
    {
        "id": "n3-058",
        "kanji": "決",
        "readings": {"on": ["けつ"], "kun": ["きめる", "きまる"]},
        "meanings": ["decide", "determine", "settle"],
        "jlptLevel": "N3",
        "frequency": 58,
        "strokes": 7,
        "examples": [
            {
                "word": "決定",
                "reading": "けってい",
                "meaning": "decision, determination",
                "sentence": {
                    "japanese": "決定を下しました。",
                    "romaji": "Kettei o kudashimashita.",
                    "english": "I made a decision.",
                    "uzbek": "Qaror qabul qildim."
                }
            }
        ]
    },
    {
        "id": "n3-059",
        "kanji": "建",
        "readings": {"on": ["けん"], "kun": ["たてる", "たつ"]},
        "meanings": ["build", "construct", "establish"],
        "jlptLevel": "N3",
        "frequency": 59,
        "strokes": 9,
        "examples": [
            {
                "word": "建設",
                "reading": "けんせつ",
                "meaning": "construction, building",
                "sentence": {
                    "japanese": "新しい建物を建設しています。",
                    "romaji": "Atarashii tatemono o kensetsu shite imasu.",
                    "english": "We are constructing a new building.",
                    "uzbek": "Yangi bino qurmoqdamiz."
                }
            }
        ]
    },
    {
        "id": "n3-060",
        "kanji": "健",
        "readings": {"on": ["けん"], "kun": ["すこやか"]},
        "meanings": ["healthy", "strong", "robust"],
        "jlptLevel": "N3",
        "frequency": 60,
        "strokes": 11,
        "examples": [
            {
                "word": "健康",
                "reading": "けんこう",
                "meaning": "health",
                "sentence": {
                    "japanese": "健康に気をつけています。",
                    "romaji": "Kenkō ni ki o tsukete imasu.",
                    "english": "I'm taking care of my health.",
                    "uzbek": "Salomatligimga e'tibor beraman."
                }
            }
        ]
    },
    {
        "id": "n3-061",
        "kanji": "験",
        "readings": {"on": ["けん"], "kun": []},
        "meanings": ["test", "examination", "experience"],
        "jlptLevel": "N3",
        "frequency": 61,
        "strokes": 18,
        "examples": [
            {
                "word": "試験",
                "reading": "しけん",
                "meaning": "examination, test",
                "sentence": {
                    "japanese": "試験を受けました。",
                    "romaji": "Shiken o ukemashita.",
                    "english": "I took an exam.",
                    "uzbek": "Imtihon topshirdim."
                }
            }
        ]
    },
    {
        "id": "n3-062",
        "kanji": "現",
        "readings": {"on": ["げん"], "kun": ["あらわれる", "うつつ"]},
        "meanings": ["present", "current", "appear"],
        "jlptLevel": "N3",
        "frequency": 62,
        "strokes": 11,
        "examples": [
            {
                "word": "現在",
                "reading": "げんざい",
                "meaning": "present, current",
                "sentence": {
                    "japanese": "現在の状況を説明します。",
                    "romaji": "Genzai no jōkyō o setsumei shimasu.",
                    "english": "I will explain the current situation.",
                    "uzbek": "Hozirgi holatni tushuntirib beraman."
                }
            }
        ]
    },
    {
        "id": "n3-063",
        "kanji": "減",
        "readings": {"on": ["げん"], "kun": ["へる", "へらす"]},
        "meanings": ["decrease", "reduce", "diminish"],
        "jlptLevel": "N3",
        "frequency": 63,
        "strokes": 12,
        "examples": [
            {
                "word": "減少",
                "reading": "げんしょう",
                "meaning": "decrease, reduction",
                "sentence": {
                    "japanese": "人口が減少しています。",
                    "romaji": "Jinkō ga genshō shite imasu.",
                    "english": "The population is decreasing.",
                    "uzbek": "Aholi soni kamaymoqda."
                }
            }
        ]
    },
    {
        "id": "n3-064",
        "kanji": "個",
        "readings": {"on": ["こ"], "kun": []},
        "meanings": ["individual", "piece", "item"],
        "jlptLevel": "N3",
        "frequency": 64,
        "strokes": 10,
        "examples": [
            {
                "word": "個人",
                "reading": "こじん",
                "meaning": "individual, personal",
                "sentence": {
                    "japanese": "個人の意見を聞きました。",
                    "romaji": "Kojin no iken o kikimashita.",
                    "english": "I heard individual opinions.",
                    "uzbek": "Shaxsiy fikrlarni eshitdim."
                }
            }
        ]
    },
    {
        "id": "n3-065",
        "kanji": "故",
        "readings": {"on": ["こ"], "kun": ["ゆえ", "ふるい"]},
        "meanings": ["reason", "cause", "deceased"],
        "jlptLevel": "N3",
        "frequency": 65,
        "strokes": 9,
        "examples": [
            {
                "word": "事故",
                "reading": "じこ",
                "meaning": "accident, incident",
                "sentence": {
                    "japanese": "事故に遭いました。",
                    "romaji": "Jiko ni aimashita.",
                    "english": "I had an accident.",
                    "uzbek": "Baxtsiz hodisa yuz berdi."
                }
            }
        ]
    },
    {
        "id": "n3-066",
        "kanji": "固",
        "readings": {"on": ["こ"], "kun": ["かたい", "かたまる"]},
        "meanings": ["hard", "solid", "firm"],
        "jlptLevel": "N3",
        "frequency": 66,
        "strokes": 8,
        "examples": [
            {
                "word": "固定",
                "reading": "こてい",
                "meaning": "fixed, stationary",
                "sentence": {
                    "japanese": "固定電話を使っています。",
                    "romaji": "Kotei denwa o tsukatte imasu.",
                    "english": "I use a landline phone.",
                    "uzbek": "Statsionar telefon ishlataman."
                }
            }
        ]
    },
    {
        "id": "n3-067",
        "kanji": "雇",
        "readings": {"on": ["こ"], "kun": ["やとう"]},
        "meanings": ["employ", "hire", "engage"],
        "jlptLevel": "N3",
        "frequency": 67,
        "strokes": 12,
        "examples": [
            {
                "word": "雇用",
                "reading": "こよう",
                "meaning": "employment, hiring",
                "sentence": {
                    "japanese": "新しい人を雇用しました。",
                    "romaji": "Atarashii hito o koyō shimashita.",
                    "english": "We hired a new person.",
                    "uzbek": "Yangi odamni ishga oldik."
                }
            }
        ]
    },
    {
        "id": "n3-068",
        "kanji": "顧",
        "readings": {"on": ["こ"], "kun": ["かえりみる"]},
        "meanings": ["look back", "consider", "customer"],
        "jlptLevel": "N3",
        "frequency": 68,
        "strokes": 21,
        "examples": [
            {
                "word": "顧客",
                "reading": "こきゃく",
                "meaning": "customer, client",
                "sentence": {
                    "japanese": "顧客の満足度を調査しました。",
                    "romaji": "Kokyaku no manzoku-do o chōsa shimashita.",
                    "english": "We surveyed customer satisfaction.",
                    "uzbek": "Mijozlarning qoniqishini tekshirdik."
                }
            }
        ]
    },
    {
        "id": "n3-069",
        "kanji": "告",
        "readings": {"on": ["こく"], "kun": ["つげる"]},
        "meanings": ["tell", "announce", "declare"],
        "jlptLevel": "N3",
        "frequency": 69,
        "strokes": 7,
        "examples": [
            {
                "word": "報告",
                "reading": "ほうこく",
                "meaning": "report, announcement",
                "sentence": {
                    "japanese": "報告書を提出しました。",
                    "romaji": "Hōkokusho o teishutsu shimashita.",
                    "english": "I submitted a report.",
                    "uzbek": "Hisobotni topshirdim."
                }
            }
        ]
    },
    {
        "id": "n3-070",
        "kanji": "国",
        "readings": {"on": ["こく"], "kun": ["くに"]},
        "meanings": ["country", "nation", "state"],
        "jlptLevel": "N3",
        "frequency": 70,
        "strokes": 8,
        "examples": [
            {
                "word": "国際",
                "reading": "こくさい",
                "meaning": "international",
                "sentence": {
                    "japanese": "国際会議に参加しました。",
                    "romaji": "Kokusai kaigi ni sanka shimashita.",
                    "english": "I participated in an international conference.",
                    "uzbek": "Xalqaro konferentsiyada qatnashdim."
                }
            }
        ]
    },
    {
        "id": "n3-071",
        "kanji": "黒",
        "readings": {"on": ["こく"], "kun": ["くろ", "くろい"]},
        "meanings": ["black", "dark"],
        "jlptLevel": "N3",
        "frequency": 71,
        "strokes": 11,
        "examples": [
            {
                "word": "黒板",
                "reading": "こくばん",
                "meaning": "blackboard",
                "sentence": {
                    "japanese": "黒板に字を書きました。",
                    "romaji": "Kokuban ni ji o kakimashita.",
                    "english": "I wrote characters on the blackboard.",
                    "uzbek": "Doskaga harflar yozdim."
                }
            }
        ]
    },
    {
        "id": "n3-072",
        "kanji": "穀",
        "readings": {"on": ["こく"], "kun": []},
        "meanings": ["grain", "cereal", "crop"],
        "jlptLevel": "N3",
        "frequency": 72,
        "strokes": 14,
        "examples": [
            {
                "word": "穀物",
                "reading": "こくもつ",
                "meaning": "grain, cereal",
                "sentence": {
                    "japanese": "穀物を収穫しました。",
                    "romaji": "Kokumotsu o shūkaku shimashita.",
                    "english": "We harvested grain.",
                    "uzbek": "Don hosilini yig'dik."
                }
            }
        ]
    },
    {
        "id": "n3-073",
        "kanji": "困",
        "readings": {"on": ["こん"], "kun": ["こまる"]},
        "meanings": ["trouble", "difficulty", "worry"],
        "jlptLevel": "N3",
        "frequency": 73,
        "strokes": 7,
        "examples": [
            {
                "word": "困難",
                "reading": "こんなん",
                "meaning": "difficulty, hardship",
                "sentence": {
                    "japanese": "困難を乗り越えました。",
                    "romaji": "Konnan o norikoemashita.",
                    "english": "We overcame the difficulty.",
                    "uzbek": "Qiyinchilikni engib o'tdik."
                }
            }
        ]
    },
    {
        "id": "n3-074",
        "kanji": "混",
        "readings": {"on": ["こん"], "kun": ["まじる", "まぜる"]},
        "meanings": ["mix", "blend", "confuse"],
        "jlptLevel": "N3",
        "frequency": 74,
        "strokes": 11,
        "examples": [
            {
                "word": "混乱",
                "reading": "こんらん",
                "meaning": "confusion, chaos",
                "sentence": {
                    "japanese": "混乱を避けました。",
                    "romaji": "Konran o sakemashita.",
                    "english": "We avoided confusion.",
                    "uzbek": "Chalkashlikdan qochdik."
                }
            }
        ]
    },
    {
        "id": "n3-075",
        "kanji": "差",
        "readings": {"on": ["さ"], "kun": ["さす", "さし"]},
        "meanings": ["difference", "distinction", "gap"],
        "jlptLevel": "N3",
        "frequency": 75,
        "strokes": 10,
        "examples": [
            {
                "word": "差別",
                "reading": "さべつ",
                "meaning": "discrimination, distinction",
                "sentence": {
                    "japanese": "差別をなくしましょう。",
                    "romaji": "Sabetsu o nakushimashō.",
                    "english": "Let's eliminate discrimination.",
                    "uzbek": "Kamsitishni yo'qotaylik."
                }
            }
        ]
    },
    {
        "id": "n3-076",
        "kanji": "最",
        "readings": {"on": ["さい"], "kun": ["もっと"]},
        "meanings": ["most", "highest", "best"],
        "jlptLevel": "N3",
        "frequency": 76,
        "strokes": 12,
        "examples": [
            {
                "word": "最高",
                "reading": "さいこう",
                "meaning": "highest, best, maximum",
                "sentence": {
                    "japanese": "最高の結果でした。",
                    "romaji": "Saikō no kekka deshita.",
                    "english": "It was the best result.",
                    "uzbek": "Eng yaxshi natija edi."
                }
            }
        ]
    },
    {
        "id": "n3-077",
        "kanji": "財",
        "readings": {"on": ["ざい"], "kun": ["たから"]},
        "meanings": ["wealth", "property", "treasure"],
        "jlptLevel": "N3",
        "frequency": 77,
        "strokes": 10,
        "examples": [
            {
                "word": "財産",
                "reading": "ざいさん",
                "meaning": "property, assets",
                "sentence": {
                    "japanese": "財産を管理しています。",
                    "romaji": "Zaisan o kanri shite imasu.",
                    "english": "I manage the property.",
                    "uzbek": "Mulkni boshqaraman."
                }
            }
        ]
    },
    {
        "id": "n3-078",
        "kanji": "罪",
        "readings": {"on": ["ざい"], "kun": ["つみ"]},
        "meanings": ["crime", "sin", "guilt"],
        "jlptLevel": "N3",
        "frequency": 78,
        "strokes": 13,
        "examples": [
            {
                "word": "犯罪",
                "reading": "はんざい",
                "meaning": "crime",
                "sentence": {
                    "japanese": "犯罪を防ぎましょう。",
                    "romaji": "Hanzai o fusagimashō.",
                    "english": "Let's prevent crime.",
                    "uzbek": "Jinoyatni oldini olaylik."
                }
            }
        ]
    },
    {
        "id": "n3-079",
        "kanji": "策",
        "readings": {"on": ["さく"], "kun": []},
        "meanings": ["plan", "strategy", "policy"],
        "jlptLevel": "N3",
        "frequency": 79,
        "strokes": 12,
        "examples": [
            {
                "word": "政策",
                "reading": "せいさく",
                "meaning": "policy",
                "sentence": {
                    "japanese": "政策を実行しました。",
                    "romaji": "Seisaku o jikkō shimashita.",
                    "english": "We implemented the policy.",
                    "uzbek": "Siyosatni amalga oshirdik."
                }
            }
        ]
    },
    {
        "id": "n3-080",
        "kanji": "冊",
        "readings": {"on": ["さつ"], "kun": []},
        "meanings": ["volume", "book", "counter for books"],
        "jlptLevel": "N3",
        "frequency": 80,
        "strokes": 5,
        "examples": [
            {
                "word": "冊子",
                "reading": "さっし",
                "meaning": "booklet, pamphlet",
                "sentence": {
                    "japanese": "冊子を配布しました。",
                    "romaji": "Sasshi o haifu shimashita.",
                    "english": "We distributed booklets.",
                    "uzbek": "Bukletlarni tarqatdik."
                }
            }
        ]
    },
    {
        "id": "n3-081",
        "kanji": "雑",
        "readings": {"on": ["ざつ"], "kun": ["まじる"]},
        "meanings": ["miscellaneous", "mixed", "complex"],
        "jlptLevel": "N3",
        "frequency": 81,
        "strokes": 14,
        "examples": [
            {
                "word": "雑誌",
                "reading": "ざっし",
                "meaning": "magazine",
                "sentence": {
                    "japanese": "雑誌を読みました。",
                    "romaji": "Zasshi o yomimashita.",
                    "english": "I read a magazine.",
                    "uzbek": "Jurnalni o'qidim."
                }
            }
        ]
    },
    {
        "id": "n3-082",
        "kanji": "参",
        "readings": {"on": ["さん"], "kun": ["まいる", "さん"]},
        "meanings": ["participate", "visit", "go"],
        "jlptLevel": "N3",
        "frequency": 82,
        "strokes": 8,
        "examples": [
            {
                "word": "参加",
                "reading": "さんか",
                "meaning": "participation, joining",
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
        "id": "n3-083",
        "kanji": "産",
        "readings": {"on": ["さん"], "kun": ["うむ", "うまれる"]},
        "meanings": ["produce", "give birth", "product"],
        "jlptLevel": "N3",
        "frequency": 83,
        "strokes": 11,
        "examples": [
            {
                "word": "生産",
                "reading": "せいさん",
                "meaning": "production, manufacture",
                "sentence": {
                    "japanese": "生産量が増えました。",
                    "romaji": "Seisan-ryō ga fuemashita.",
                    "english": "Production increased.",
                    "uzbek": "Ishlab chiqarish ko'paydi."
                }
            }
        ]
    },
    {
        "id": "n3-084",
        "kanji": "算",
        "readings": {"on": ["さん"], "kun": ["かぞえる", "かんがえる"]},
        "meanings": ["calculate", "compute", "arithmetic"],
        "jlptLevel": "N3",
        "frequency": 84,
        "strokes": 14,
        "examples": [
            {
                "word": "計算",
                "reading": "けいさん",
                "meaning": "calculation, computation",
                "sentence": {
                    "japanese": "計算をしました。",
                    "romaji": "Keisan o shimashita.",
                    "english": "I did the calculation.",
                    "uzbek": "Hisoblashni bajardim."
                }
            }
        ]
    },
    {
        "id": "n3-085",
        "kanji": "残",
        "readings": {"on": ["ざん"], "kun": ["のこる", "のこす"]},
        "meanings": ["remain", "leftover", "residue"],
        "jlptLevel": "N3",
        "frequency": 85,
        "strokes": 10,
        "examples": [
            {
                "word": "残業",
                "reading": "ざんぎょう",
                "meaning": "overtime work",
                "sentence": {
                    "japanese": "残業をしました。",
                    "romaji": "Zangyō o shimashita.",
                    "english": "I worked overtime.",
                    "uzbek": "Qo'shimcha ishladim."
                }
            }
        ]
    },
    {
        "id": "n3-086",
        "kanji": "仕",
        "readings": {"on": ["し"], "kun": ["つかえる"]},
        "meanings": ["serve", "work", "do"],
        "jlptLevel": "N3",
        "frequency": 86,
        "strokes": 5,
        "examples": [
            {
                "word": "仕事",
                "reading": "しごと",
                "meaning": "work, job",
                "sentence": {
                    "japanese": "仕事を探しています。",
                    "romaji": "Shigoto o sagashite imasu.",
                    "english": "I'm looking for work.",
                    "uzbek": "Ish qidiraman."
                }
            }
        ]
    },
    {
        "id": "n3-087",
        "kanji": "死",
        "readings": {"on": ["し"], "kun": ["しぬ"]},
        "meanings": ["death", "die", "deceased"],
        "jlptLevel": "N3",
        "frequency": 87,
        "strokes": 6,
        "examples": [
            {
                "word": "死亡",
                "reading": "しぼう",
                "meaning": "death",
                "sentence": {
                    "japanese": "死亡事故が起きました。",
                    "romaji": "Shibō jiko ga okimashita.",
                    "english": "A fatal accident occurred.",
                    "uzbek": "O'limga olib kelgan baxtsiz hodisa yuz berdi."
                }
            }
        ]
    },
    {
        "id": "n3-088",
        "kanji": "始",
        "readings": {"on": ["し"], "kun": ["はじめる", "はじまる"]},
        "meanings": ["begin", "start", "commence"],
        "jlptLevel": "N3",
        "frequency": 88,
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
        "id": "n3-089",
        "kanji": "市",
        "readings": {"on": ["し"], "kun": ["いち"]},
        "meanings": ["city", "market", "municipality"],
        "jlptLevel": "N3",
        "frequency": 89,
        "strokes": 5,
        "examples": [
            {
                "word": "都市",
                "reading": "とし",
                "meaning": "city, urban area",
                "sentence": {
                    "japanese": "都市に住んでいます。",
                    "romaji": "Toshi ni sunde imasu.",
                    "english": "I live in the city.",
                    "uzbek": "Shaharda yashayman."
                }
            }
        ]
    },
    {
        "id": "n3-090",
        "kanji": "志",
        "readings": {"on": ["し"], "kun": ["こころざし", "こころざす"]},
        "meanings": ["intention", "will", "ambition"],
        "jlptLevel": "N3",
        "frequency": 90,
        "strokes": 7,
        "examples": [
            {
                "word": "意志",
                "reading": "いし",
                "meaning": "will, intention",
                "sentence": {
                    "japanese": "強い意志を持っています。",
                    "romaji": "Tsuyoi ishi o motte imasu.",
                    "english": "I have strong will.",
                    "uzbek": "Kuchli irodaga egaman."
                }
            }
        ]
    },
    {
        "id": "n3-091",
        "kanji": "支",
        "readings": {"on": ["し"], "kun": ["ささえる"]},
        "meanings": ["support", "branch", "sustain"],
        "jlptLevel": "N3",
        "frequency": 91,
        "strokes": 4,
        "examples": [
            {
                "word": "支払い",
                "reading": "しはらい",
                "meaning": "payment",
                "sentence": {
                    "japanese": "支払いをしました。",
                    "romaji": "Shiharai o shimashita.",
                    "english": "I made a payment.",
                    "uzbek": "To'lovni amalga oshirdim."
                }
            }
        ]
    },
    {
        "id": "n3-092",
        "kanji": "使",
        "readings": {"on": ["し"], "kun": ["つかう", "つかい"]},
        "meanings": ["use", "employ", "utilize"],
        "jlptLevel": "N3",
        "frequency": 92,
        "strokes": 8,
        "examples": [
            {
                "word": "使用",
                "reading": "しよう",
                "meaning": "use, usage",
                "sentence": {
                    "japanese": "新しい機械を使用しています。",
                    "romaji": "Atarashii kikai o shiyō shite imasu.",
                    "english": "I'm using a new machine.",
                    "uzbek": "Yangi mashinani ishlataman."
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
