#!/usr/bin/env python3
import json

# Read existing N3 data
with open('src/data/kanji/n3-complete.json', 'r', encoding='utf-8') as f:
    n3_data = json.load(f)

print(f'Current N3 kanji count: {len(n3_data)}')

# Additional N3 kanji data (143-192)
additional_kanji = [
    {
        "id": "n3-143",
        "kanji": "神",
        "readings": {"on": ["しん"], "kun": ["かみ"]},
        "meanings": ["god", "deity", "spirit"],
        "jlptLevel": "N3",
        "frequency": 143,
        "strokes": 9,
        "examples": [
            {
                "word": "神社",
                "reading": "じんじゃ",
                "meaning": "shrine",
                "sentence": {
                    "japanese": "神社にお参りしました。",
                    "romaji": "Jinja ni omairi shimashita.",
                    "english": "I visited the shrine.",
                    "uzbek": "Ma'badga tashrif buyurdim."
                }
            }
        ]
    },
    {
        "id": "n3-144",
        "kanji": "真",
        "readings": {"on": ["しん"], "kun": ["ま"]},
        "meanings": ["true", "real", "genuine"],
        "jlptLevel": "N3",
        "frequency": 144,
        "strokes": 10,
        "examples": [
            {
                "word": "真実",
                "reading": "しんじつ",
                "meaning": "truth, reality",
                "sentence": {
                    "japanese": "真実を話しました。",
                    "romaji": "Shinjitsu o hanashimashita.",
                    "english": "I told the truth.",
                    "uzbek": "Haqiqatni aytdim."
                }
            }
        ]
    },
    {
        "id": "n3-145",
        "kanji": "身",
        "readings": {"on": ["しん"], "kun": ["み"]},
        "meanings": ["body", "self", "person"],
        "jlptLevel": "N3",
        "frequency": 145,
        "strokes": 7,
        "examples": [
            {
                "word": "身体",
                "reading": "しんたい",
                "meaning": "body, physical",
                "sentence": {
                    "japanese": "身体を鍛えました。",
                    "romaji": "Shintai o kitaemashita.",
                    "english": "I trained my body.",
                    "uzbek": "Tanani mashq qildim."
                }
            }
        ]
    },
    {
        "id": "n3-146",
        "kanji": "進",
        "readings": {"on": ["しん"], "kun": ["すすむ", "すすめる"]},
        "meanings": ["advance", "progress", "proceed"],
        "jlptLevel": "N3",
        "frequency": 146,
        "strokes": 11,
        "examples": [
            {
                "word": "進学",
                "reading": "しんがく",
                "meaning": "advancement to higher education",
                "sentence": {
                    "japanese": "大学に進学しました。",
                    "romaji": "Daigaku ni shingaku shimashita.",
                    "english": "I advanced to university.",
                    "uzbek": "Universitetga o'tdim."
                }
            }
        ]
    },
    {
        "id": "n3-147",
        "kanji": "針",
        "readings": {"on": ["しん"], "kun": ["はり"]},
        "meanings": ["needle", "pin", "hand"],
        "jlptLevel": "N3",
        "frequency": 147,
        "strokes": 10,
        "examples": [
            {
                "word": "時計の針",
                "reading": "とけいのはり",
                "meaning": "clock hands",
                "sentence": {
                    "japanese": "時計の針を見ました。",
                    "romaji": "Tokei no hari o mimashita.",
                    "english": "I looked at the clock hands.",
                    "uzbek": "Soat milini ko'rdim."
                }
            }
        ]
    },
    {
        "id": "n3-148",
        "kanji": "人",
        "readings": {"on": ["じん", "にん"], "kun": ["ひと"]},
        "meanings": ["person", "people", "human"],
        "jlptLevel": "N3",
        "frequency": 148,
        "strokes": 2,
        "examples": [
            {
                "word": "人間",
                "reading": "にんげん",
                "meaning": "human being, person",
                "sentence": {
                    "japanese": "人間は考える動物です。",
                    "romaji": "Ningen wa kangaeru dōbutsu desu.",
                    "english": "Humans are thinking animals.",
                    "uzbek": "Inson o'ylaydigan hayvon."
                }
            }
        ]
    },
    {
        "id": "n3-149",
        "kanji": "水",
        "readings": {"on": ["すい"], "kun": ["みず"]},
        "meanings": ["water", "liquid"],
        "jlptLevel": "N3",
        "frequency": 149,
        "strokes": 4,
        "examples": [
            {
                "word": "水道",
                "reading": "すいどう",
                "meaning": "water supply, plumbing",
                "sentence": {
                    "japanese": "水道を修理しました。",
                    "romaji": "Suidō o shūri shimashita.",
                    "english": "I repaired the plumbing.",
                    "uzbek": "Suv ta'minotini tuzatdim."
                }
            }
        ]
    },
    {
        "id": "n3-150",
        "kanji": "数",
        "readings": {"on": ["すう"], "kun": ["かず", "かぞえる"]},
        "meanings": ["number", "count", "several"],
        "jlptLevel": "N3",
        "frequency": 150,
        "strokes": 13,
        "examples": [
            {
                "word": "数学",
                "reading": "すうがく",
                "meaning": "mathematics",
                "sentence": {
                    "japanese": "数学を勉強しました。",
                    "romaji": "Sūgaku o benkyō shimashita.",
                    "english": "I studied mathematics.",
                    "uzbek": "Matematikani o'qidim."
                }
            }
        ]
    },
    {
        "id": "n3-151",
        "kanji": "世",
        "readings": {"on": ["せい", "せ"], "kun": ["よ"]},
        "meanings": ["world", "generation", "society"],
        "jlptLevel": "N3",
        "frequency": 151,
        "strokes": 5,
        "examples": [
            {
                "word": "世界",
                "reading": "せかい",
                "meaning": "world",
                "sentence": {
                    "japanese": "世界を旅行しました。",
                    "romaji": "Sekai o ryokō shimashita.",
                    "english": "I traveled the world.",
                    "uzbek": "Dunyoni kezdim."
                }
            }
        ]
    },
    {
        "id": "n3-152",
        "kanji": "正",
        "readings": {"on": ["せい"], "kun": ["ただしい", "ただす"]},
        "meanings": ["correct", "right", "positive"],
        "jlptLevel": "N3",
        "frequency": 152,
        "strokes": 5,
        "examples": [
            {
                "word": "正確",
                "reading": "せいかく",
                "meaning": "accurate, precise",
                "sentence": {
                    "japanese": "正確に答えました。",
                    "romaji": "Seikaku ni kotaemashita.",
                    "english": "I answered accurately.",
                    "uzbek": "Aniq javob berdim."
                }
            }
        ]
    },
    {
        "id": "n3-153",
        "kanji": "生",
        "readings": {"on": ["せい"], "kun": ["いきる", "うまれる", "なま"]},
        "meanings": ["life", "birth", "raw"],
        "jlptLevel": "N3",
        "frequency": 153,
        "strokes": 5,
        "examples": [
            {
                "word": "生活",
                "reading": "せいかつ",
                "meaning": "life, living",
                "sentence": {
                    "japanese": "生活を改善しました。",
                    "romaji": "Seikatsu o kaizen shimashita.",
                    "english": "I improved my life.",
                    "uzbek": "Hayotni yaxshiladim."
                }
            }
        ]
    },
    {
        "id": "n3-154",
        "kanji": "成",
        "readings": {"on": ["せい"], "kun": ["なる", "なす"]},
        "meanings": ["become", "achieve", "accomplish"],
        "jlptLevel": "N3",
        "frequency": 154,
        "strokes": 6,
        "examples": [
            {
                "word": "成功",
                "reading": "せいこう",
                "meaning": "success",
                "sentence": {
                    "japanese": "成功しました。",
                    "romaji": "Seikō shimashita.",
                    "english": "I succeeded.",
                    "uzbek": "Muvaffaqiyatga erishdim."
                }
            }
        ]
    },
    {
        "id": "n3-155",
        "kanji": "制",
        "readings": {"on": ["せい"], "kun": []},
        "meanings": ["control", "restrict", "system"],
        "jlptLevel": "N3",
        "frequency": 155,
        "strokes": 8,
        "examples": [
            {
                "word": "制度",
                "reading": "せいど",
                "meaning": "system, institution",
                "sentence": {
                    "japanese": "制度を改革しました。",
                    "romaji": "Seido o kaikaku shimashita.",
                    "english": "We reformed the system.",
                    "uzbek": "Tizimni isloh qildik."
                }
            }
        ]
    },
    {
        "id": "n3-156",
        "kanji": "性",
        "readings": {"on": ["せい"], "kun": []},
        "meanings": ["nature", "sex", "gender"],
        "jlptLevel": "N3",
        "frequency": 156,
        "strokes": 8,
        "examples": [
            {
                "word": "性格",
                "reading": "せいかく",
                "meaning": "personality, character",
                "sentence": {
                    "japanese": "性格が良いです。",
                    "romaji": "Seikaku ga ii desu.",
                    "english": "He has a good personality.",
                    "uzbek": "Xarakteri yaxshi."
                }
            }
        ]
    },
    {
        "id": "n3-157",
        "kanji": "政",
        "readings": {"on": ["せい"], "kun": ["まつりごと"]},
        "meanings": ["politics", "government", "administration"],
        "jlptLevel": "N3",
        "frequency": 157,
        "strokes": 9,
        "examples": [
            {
                "word": "政治",
                "reading": "せいじ",
                "meaning": "politics",
                "sentence": {
                    "japanese": "政治に興味があります。",
                    "romaji": "Seiji ni kyōmi ga arimasu.",
                    "english": "I'm interested in politics.",
                    "uzbek": "Siyosatga qiziqaman."
                }
            }
        ]
    },
    {
        "id": "n3-158",
        "kanji": "整",
        "readings": {"on": ["せい"], "kun": ["ととのえる"]},
        "meanings": ["arrange", "organize", "complete"],
        "jlptLevel": "N3",
        "frequency": 158,
        "strokes": 16,
        "examples": [
            {
                "word": "整理",
                "reading": "せいり",
                "meaning": "organization, arrangement",
                "sentence": {
                    "japanese": "部屋を整理しました。",
                    "romaji": "Heya o seiri shimashita.",
                    "english": "I organized the room.",
                    "uzbek": "Xonani tartibga keltirdim."
                }
            }
        ]
    },
    {
        "id": "n3-159",
        "kanji": "清",
        "readings": {"on": ["せい"], "kun": ["きよい", "きよめる"]},
        "meanings": ["pure", "clean", "clear"],
        "jlptLevel": "N3",
        "frequency": 159,
        "strokes": 11,
        "examples": [
            {
                "word": "清潔",
                "reading": "せいけつ",
                "meaning": "clean, hygienic",
                "sentence": {
                    "japanese": "清潔に保ちました。",
                    "romaji": "Seiketsu ni tamochimashita.",
                    "english": "I kept it clean.",
                    "uzbek": "Toza saqladim."
                }
            }
        ]
    },
    {
        "id": "n3-160",
        "kanji": "静",
        "readings": {"on": ["せい"], "kun": ["しずか"]},
        "meanings": ["quiet", "calm", "still"],
        "jlptLevel": "N3",
        "frequency": 160,
        "strokes": 14,
        "examples": [
            {
                "word": "静寂",
                "reading": "せいじゃく",
                "meaning": "silence, quietness",
                "sentence": {
                    "japanese": "静寂を保ちました。",
                    "romaji": "Seijaku o tamochimashita.",
                    "english": "I maintained silence.",
                    "uzbek": "Jimjitlikni saqladim."
                }
            }
        ]
    },
    {
        "id": "n3-161",
        "kanji": "税",
        "readings": {"on": ["ぜい"], "kun": []},
        "meanings": ["tax", "duty"],
        "jlptLevel": "N3",
        "frequency": 161,
        "strokes": 12,
        "examples": [
            {
                "word": "税金",
                "reading": "ぜいきん",
                "meaning": "tax",
                "sentence": {
                    "japanese": "税金を払いました。",
                    "romaji": "Zeikin o haraimashita.",
                    "english": "I paid the tax.",
                    "uzbek": "Soliq to'ladim."
                }
            }
        ]
    },
    {
        "id": "n3-162",
        "kanji": "説",
        "readings": {"on": ["せつ"], "kun": ["とく"]},
        "meanings": ["theory", "explanation", "persuade"],
        "jlptLevel": "N3",
        "frequency": 162,
        "strokes": 14,
        "examples": [
            {
                "word": "説明",
                "reading": "せつめい",
                "meaning": "explanation",
                "sentence": {
                    "japanese": "説明を聞きました。",
                    "romaji": "Setsumei o kikimashita.",
                    "english": "I heard the explanation.",
                    "uzbek": "Tushuntirishni eshitdim."
                }
            }
        ]
    },
    {
        "id": "n3-163",
        "kanji": "設",
        "readings": {"on": ["せつ"], "kun": ["もうける"]},
        "meanings": ["establish", "set up", "equip"],
        "jlptLevel": "N3",
        "frequency": 163,
        "strokes": 11,
        "examples": [
            {
                "word": "設備",
                "reading": "せつび",
                "meaning": "equipment, facilities",
                "sentence": {
                    "japanese": "設備を整えました。",
                    "romaji": "Setsubi o totonoemashita.",
                    "english": "I arranged the equipment.",
                    "uzbek": "Jihozlarni tartibga keltirdim."
                }
            }
        ]
    },
    {
        "id": "n3-164",
        "kanji": "節",
        "readings": {"on": ["せつ"], "kun": ["ふし"]},
        "meanings": ["section", "season", "joint"],
        "jlptLevel": "N3",
        "frequency": 164,
        "strokes": 13,
        "examples": [
            {
                "word": "季節",
                "reading": "きせつ",
                "meaning": "season",
                "sentence": {
                    "japanese": "季節が変わりました。",
                    "romaji": "Kisetsu ga kawarimashita.",
                    "english": "The season changed.",
                    "uzbek": "Mavsum o'zgardi."
                }
            }
        ]
    },
    {
        "id": "n3-165",
        "kanji": "絶",
        "readings": {"on": ["ぜつ"], "kun": ["たえる", "たつ"]},
        "meanings": ["cut off", "discontinue", "absolute"],
        "jlptLevel": "N3",
        "frequency": 165,
        "strokes": 12,
        "examples": [
            {
                "word": "絶対",
                "reading": "ぜったい",
                "meaning": "absolute, definitely",
                "sentence": {
                    "japanese": "絶対に約束します。",
                    "romaji": "Zettai ni yakusoku shimasu.",
                    "english": "I promise absolutely.",
                    "uzbek": "Mutlaqo va'da beraman."
                }
            }
        ]
    },
    {
        "id": "n3-166",
        "kanji": "選",
        "readings": {"on": ["せん"], "kun": ["えらぶ"]},
        "meanings": ["choose", "select", "elect"],
        "jlptLevel": "N3",
        "frequency": 166,
        "strokes": 15,
        "examples": [
            {
                "word": "選択",
                "reading": "せんたく",
                "meaning": "choice, selection",
                "sentence": {
                    "japanese": "選択をしました。",
                    "romaji": "Sentaku o shimashita.",
                    "english": "I made a choice.",
                    "uzbek": "Tanlovni amalga oshirdim."
                }
            }
        ]
    },
    {
        "id": "n3-167",
        "kanji": "戦",
        "readings": {"on": ["せん"], "kun": ["たたかう"]},
        "meanings": ["war", "battle", "fight"],
        "jlptLevel": "N3",
        "frequency": 167,
        "strokes": 13,
        "examples": [
            {
                "word": "戦争",
                "reading": "せんそう",
                "meaning": "war",
                "sentence": {
                    "japanese": "戦争を避けました。",
                    "romaji": "Sensō o sakemashita.",
                    "english": "We avoided war.",
                    "uzbek": "Urushdan qochdik."
                }
            }
        ]
    },
    {
        "id": "n3-168",
        "kanji": "線",
        "readings": {"on": ["せん"], "kun": []},
        "meanings": ["line", "railway", "route"],
        "jlptLevel": "N3",
        "frequency": 168,
        "strokes": 15,
        "examples": [
            {
                "word": "電線",
                "reading": "でんせん",
                "meaning": "electric wire, power line",
                "sentence": {
                    "japanese": "電線を修理しました。",
                    "romaji": "Densen o shūri shimashita.",
                    "english": "I repaired the power line.",
                    "uzbek": "Elektr simini tuzatdim."
                }
            }
        ]
    },
    {
        "id": "n3-169",
        "kanji": "全",
        "readings": {"on": ["ぜん"], "kun": ["すべて", "まったく"]},
        "meanings": ["all", "whole", "complete"],
        "jlptLevel": "N3",
        "frequency": 169,
        "strokes": 6,
        "examples": [
            {
                "word": "全部",
                "reading": "ぜんぶ",
                "meaning": "all, everything",
                "sentence": {
                    "japanese": "全部終わりました。",
                    "romaji": "Zenbu owarimashita.",
                    "english": "Everything is finished.",
                    "uzbek": "Hammasi tugadi."
                }
            }
        ]
    },
    {
        "id": "n3-170",
        "kanji": "然",
        "readings": {"on": ["ぜん"], "kun": ["しか", "しかり"]},
        "meanings": ["so", "thus", "natural"],
        "jlptLevel": "N3",
        "frequency": 170,
        "strokes": 12,
        "examples": [
            {
                "word": "自然",
                "reading": "しぜん",
                "meaning": "nature, natural",
                "sentence": {
                    "japanese": "自然を愛します。",
                    "romaji": "Shizen o aishimasu.",
                    "english": "I love nature.",
                    "uzbek": "Tabiatni sevaman."
                }
            }
        ]
    },
    {
        "id": "n3-171",
        "kanji": "前",
        "readings": {"on": ["ぜん"], "kun": ["まえ"]},
        "meanings": ["before", "front", "previous"],
        "jlptLevel": "N3",
        "frequency": 171,
        "strokes": 9,
        "examples": [
            {
                "word": "前回",
                "reading": "ぜんかい",
                "meaning": "last time, previous time",
                "sentence": {
                    "japanese": "前回と同じです。",
                    "romaji": "Zenkai to onaji desu.",
                    "english": "It's the same as last time.",
                    "uzbek": "O'tgan safar bilan bir xil."
                }
            }
        ]
    },
    {
        "id": "n3-172",
        "kanji": "善",
        "readings": {"on": ["ぜん"], "kun": ["よい"]},
        "meanings": ["good", "virtue", "kindness"],
        "jlptLevel": "N3",
        "frequency": 172,
        "strokes": 12,
        "examples": [
            {
                "word": "善悪",
                "reading": "ぜんあく",
                "meaning": "good and evil",
                "sentence": {
                    "japanese": "善悪を判断しました。",
                    "romaji": "Zen'aku o handan shimashita.",
                    "english": "I judged good and evil.",
                    "uzbek": "Yaxshilik va yomonlikni baholadim."
                }
            }
        ]
    },
    {
        "id": "n3-173",
        "kanji": "相",
        "readings": {"on": ["そう"], "kun": ["あい"]},
        "meanings": ["mutual", "together", "appearance"],
        "jlptLevel": "N3",
        "frequency": 173,
        "strokes": 9,
        "examples": [
            {
                "word": "相談",
                "reading": "そうだん",
                "meaning": "consultation, discussion",
                "sentence": {
                    "japanese": "相談しました。",
                    "romaji": "Sōdan shimashita.",
                    "english": "I consulted.",
                    "uzbek": "Maslahatlashdim."
                }
            }
        ]
    },
    {
        "id": "n3-174",
        "kanji": "想",
        "readings": {"on": ["そう"], "kun": ["おもう"]},
        "meanings": ["think", "imagine", "concept"],
        "jlptLevel": "N3",
        "frequency": 174,
        "strokes": 13,
        "examples": [
            {
                "word": "思想",
                "reading": "しそう",
                "meaning": "thought, ideology",
                "sentence": {
                    "japanese": "思想を表現しました。",
                    "romaji": "Shisō o hyōgen shimashita.",
                    "english": "I expressed my thoughts.",
                    "uzbek": "Fikrimni bildirdim."
                }
            }
        ]
    },
    {
        "id": "n3-175",
        "kanji": "早",
        "readings": {"on": ["そう"], "kun": ["はやい", "はや"]},
        "meanings": ["early", "fast", "quick"],
        "jlptLevel": "N3",
        "frequency": 175,
        "strokes": 6,
        "examples": [
            {
                "word": "早朝",
                "reading": "そうちょう",
                "meaning": "early morning",
                "sentence": {
                    "japanese": "早朝に起きました。",
                    "romaji": "Sōchō ni okimashita.",
                    "english": "I woke up early in the morning.",
                    "uzbek": "Ertalab ertaroq turdim."
                }
            }
        ]
    },
    {
        "id": "n3-176",
        "kanji": "送",
        "readings": {"on": ["そう"], "kun": ["おくる"]},
        "meanings": ["send", "deliver", "escort"],
        "jlptLevel": "N3",
        "frequency": 176,
        "strokes": 9,
        "examples": [
            {
                "word": "送信",
                "reading": "そうしん",
                "meaning": "transmission, sending",
                "sentence": {
                    "japanese": "メールを送信しました。",
                    "romaji": "Mēru o sōshin shimashita.",
                    "english": "I sent an email.",
                    "uzbek": "Elektron pochta yubordim."
                }
            }
        ]
    },
    {
        "id": "n3-177",
        "kanji": "草",
        "readings": {"on": ["そう"], "kun": ["くさ"]},
        "meanings": ["grass", "herb", "weed"],
        "jlptLevel": "N3",
        "frequency": 177,
        "strokes": 9,
        "examples": [
            {
                "word": "草原",
                "reading": "そうげん",
                "meaning": "grassland, prairie",
                "sentence": {
                    "japanese": "草原を歩きました。",
                    "romaji": "Sōgen o arukimashita.",
                    "english": "I walked through the grassland.",
                    "uzbek": "O'tloqda yurdim."
                }
            }
        ]
    },
    {
        "id": "n3-178",
        "kanji": "装",
        "readings": {"on": ["そう"], "kun": ["よそおう"]},
        "meanings": ["dress", "equip", "decorate"],
        "jlptLevel": "N3",
        "frequency": 178,
        "strokes": 12,
        "examples": [
            {
                "word": "服装",
                "reading": "ふくそう",
                "meaning": "clothing, dress",
                "sentence": {
                    "japanese": "服装を選びました。",
                    "romaji": "Fukusō o erabimashita.",
                    "english": "I chose my clothing.",
                    "uzbek": "Kiyimni tanladim."
                }
            }
        ]
    },
    {
        "id": "n3-179",
        "kanji": "増",
        "readings": {"on": ["ぞう"], "kun": ["ふえる", "ふやす"]},
        "meanings": ["increase", "grow", "add"],
        "jlptLevel": "N3",
        "frequency": 179,
        "strokes": 14,
        "examples": [
            {
                "word": "増加",
                "reading": "ぞうか",
                "meaning": "increase, growth",
                "sentence": {
                    "japanese": "人口が増加しました。",
                    "romaji": "Jinkō ga zōka shimashita.",
                    "english": "The population increased.",
                    "uzbek": "Aholi soni ko'paydi."
                }
            }
        ]
    },
    {
        "id": "n3-180",
        "kanji": "像",
        "readings": {"on": ["ぞう"], "kun": []},
        "meanings": ["statue", "image", "figure"],
        "jlptLevel": "N3",
        "frequency": 180,
        "strokes": 14,
        "examples": [
            {
                "word": "映像",
                "reading": "えいぞう",
                "meaning": "image, video",
                "sentence": {
                    "japanese": "映像を見ました。",
                    "romaji": "Eizō o mimashita.",
                    "english": "I watched the video.",
                    "uzbek": "Video ko'rdim."
                }
            }
        ]
    },
    {
        "id": "n3-181",
        "kanji": "造",
        "readings": {"on": ["ぞう"], "kun": ["つくる"]},
        "meanings": ["make", "create", "build"],
        "jlptLevel": "N3",
        "frequency": 181,
        "strokes": 10,
        "examples": [
            {
                "word": "製造",
                "reading": "せいぞう",
                "meaning": "manufacturing, production",
                "sentence": {
                    "japanese": "製造を開始しました。",
                    "romaji": "Seizō o kaishi shimashita.",
                    "english": "We started manufacturing.",
                    "uzbek": "Ishlab chiqarishni boshladik."
                }
            }
        ]
    },
    {
        "id": "n3-182",
        "kanji": "側",
        "readings": {"on": ["そく"], "kun": ["がわ", "そば"]},
        "meanings": ["side", "near", "beside"],
        "jlptLevel": "N3",
        "frequency": 182,
        "strokes": 11,
        "examples": [
            {
                "word": "側面",
                "reading": "そくめん",
                "meaning": "side, aspect",
                "sentence": {
                    "japanese": "側面を調べました。",
                    "romaji": "Sokumen o shirabemashita.",
                    "english": "I examined the side.",
                    "uzbek": "Yon tomonni tekshirdim."
                }
            }
        ]
    },
    {
        "id": "n3-183",
        "kanji": "続",
        "readings": {"on": ["ぞく"], "kun": ["つづく", "つづける"]},
        "meanings": ["continue", "follow", "series"],
        "jlptLevel": "N3",
        "frequency": 183,
        "strokes": 13,
        "examples": [
            {
                "word": "続行",
                "reading": "ぞっこう",
                "meaning": "continuation, proceeding",
                "sentence": {
                    "japanese": "続行しました。",
                    "romaji": "Zokkō shimashita.",
                    "english": "I continued.",
                    "uzbek": "Davom ettirdim."
                }
            }
        ]
    },
    {
        "id": "n3-184",
        "kanji": "卒",
        "readings": {"on": ["そつ"], "kun": []},
        "meanings": ["graduate", "finish", "complete"],
        "jlptLevel": "N3",
        "frequency": 184,
        "strokes": 8,
        "examples": [
            {
                "word": "卒業",
                "reading": "そつぎょう",
                "meaning": "graduation",
                "sentence": {
                    "japanese": "卒業しました。",
                    "romaji": "Sotsugyō shimashita.",
                    "english": "I graduated.",
                    "uzbek": "Bitirdim."
                }
            }
        ]
    },
    {
        "id": "n3-185",
        "kanji": "村",
        "readings": {"on": ["そん"], "kun": ["むら"]},
        "meanings": ["village", "town"],
        "jlptLevel": "N3",
        "frequency": 185,
        "strokes": 7,
        "examples": [
            {
                "word": "村人",
                "reading": "むらびと",
                "meaning": "villager",
                "sentence": {
                    "japanese": "村人と話しました。",
                    "romaji": "Murabito to hanashimashita.",
                    "english": "I talked with the villagers.",
                    "uzbek": "Qishloq aholisi bilan gaplashdim."
                }
            }
        ]
    },
    {
        "id": "n3-186",
        "kanji": "他",
        "readings": {"on": ["た"], "kun": ["ほか"]},
        "meanings": ["other", "another", "else"],
        "jlptLevel": "N3",
        "frequency": 186,
        "strokes": 5,
        "examples": [
            {
                "word": "他人",
                "reading": "たにん",
                "meaning": "other person, stranger",
                "sentence": {
                    "japanese": "他人に頼りました。",
                    "romaji": "Tanin ni tayorimashita.",
                    "english": "I relied on others.",
                    "uzbek": "Boshqalarga ishondim."
                }
            }
        ]
    },
    {
        "id": "n3-187",
        "kanji": "多",
        "readings": {"on": ["た"], "kun": ["おおい"]},
        "meanings": ["many", "much", "numerous"],
        "jlptLevel": "N3",
        "frequency": 187,
        "strokes": 6,
        "examples": [
            {
                "word": "多数",
                "reading": "たすう",
                "meaning": "majority, many",
                "sentence": {
                    "japanese": "多数の人が参加しました。",
                    "romaji": "Tasū no hito ga sanka shimashita.",
                    "english": "Many people participated.",
                    "uzbek": "Ko'p odam qatnashdi."
                }
            }
        ]
    },
    {
        "id": "n3-188",
        "kanji": "太",
        "readings": {"on": ["た"], "kun": ["ふとい", "ふとる"]},
        "meanings": ["thick", "fat", "bold"],
        "jlptLevel": "N3",
        "frequency": 188,
        "strokes": 4,
        "examples": [
            {
                "word": "太陽",
                "reading": "たいよう",
                "meaning": "sun",
                "sentence": {
                    "japanese": "太陽が輝いています。",
                    "romaji": "Taiyō ga kagayaite imasu.",
                    "english": "The sun is shining.",
                    "uzbek": "Quyosh porlayapti."
                }
            }
        ]
    },
    {
        "id": "n3-189",
        "kanji": "対",
        "readings": {"on": ["たい"], "kun": ["あいて"]},
        "meanings": ["opposite", "against", "pair"],
        "jlptLevel": "N3",
        "frequency": 189,
        "strokes": 7,
        "examples": [
            {
                "word": "対話",
                "reading": "たいわ",
                "meaning": "dialogue, conversation",
                "sentence": {
                    "japanese": "対話をしました。",
                    "romaji": "Taiwa o shimashita.",
                    "english": "I had a dialogue.",
                    "uzbek": "Suhbatlashdim."
                }
            }
        ]
    },
    {
        "id": "n3-190",
        "kanji": "体",
        "readings": {"on": ["たい"], "kun": ["からだ"]},
        "meanings": ["body", "substance", "form"],
        "jlptLevel": "N3",
        "frequency": 190,
        "strokes": 7,
        "examples": [
            {
                "word": "体力",
                "reading": "たいりょく",
                "meaning": "physical strength",
                "sentence": {
                    "japanese": "体力を鍛えました。",
                    "romaji": "Tairyoku o kitaemashita.",
                    "english": "I trained my physical strength.",
                    "uzbek": "Jismoniy kuchni mashq qildim."
                }
            }
        ]
    },
    {
        "id": "n3-191",
        "kanji": "台",
        "readings": {"on": ["だい"], "kun": []},
        "meanings": ["platform", "stand", "counter"],
        "jlptLevel": "N3",
        "frequency": 191,
        "strokes": 5,
        "examples": [
            {
                "word": "舞台",
                "reading": "ぶたい",
                "meaning": "stage, platform",
                "sentence": {
                    "japanese": "舞台に立ちました。",
                    "romaji": "Butai ni tachimashita.",
                    "english": "I stood on the stage.",
                    "uzbek": "Sahnaga chiqdim."
                }
            }
        ]
    },
    {
        "id": "n3-192",
        "kanji": "第",
        "readings": {"on": ["だい"], "kun": []},
        "meanings": ["ordinal number", "first", "chapter"],
        "jlptLevel": "N3",
        "frequency": 192,
        "strokes": 11,
        "examples": [
            {
                "word": "第一",
                "reading": "だいいち",
                "meaning": "first, primary",
                "sentence": {
                    "japanese": "第一の目標です。",
                    "romaji": "Daiichi no mokuhyō desu.",
                    "english": "It's the first goal.",
                    "uzbek": "Birinchi maqsad."
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
