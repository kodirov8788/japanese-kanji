#!/usr/bin/env python3
import json

# Read existing N3 data
with open('src/data/kanji/n3-complete.json', 'r', encoding='utf-8') as f:
    n3_data = json.load(f)

print(f'Current N3 kanji count: {len(n3_data)}')

# Additional N3 kanji data (193-242)
additional_kanji = [
    {
        "id": "n3-193",
        "kanji": "代",
        "readings": {"on": ["だい"], "kun": ["かわる", "かえる"]},
        "meanings": ["generation", "era", "substitute"],
        "jlptLevel": "N3",
        "frequency": 193,
        "strokes": 5,
        "examples": [
            {
                "word": "時代",
                "reading": "じだい",
                "meaning": "era, period",
                "sentence": {
                    "japanese": "時代が変わりました。",
                    "romaji": "Jidai ga kawarimashita.",
                    "english": "The era changed.",
                    "uzbek": "Davr o'zgardi."
                }
            }
        ]
    },
    {
        "id": "n3-194",
        "kanji": "台",
        "readings": {"on": ["だい"], "kun": []},
        "meanings": ["platform", "stand", "counter"],
        "jlptLevel": "N3",
        "frequency": 194,
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
        "id": "n3-195",
        "kanji": "題",
        "readings": {"on": ["だい"], "kun": []},
        "meanings": ["topic", "subject", "title"],
        "jlptLevel": "N3",
        "frequency": 195,
        "strokes": 18,
        "examples": [
            {
                "word": "問題",
                "reading": "もんだい",
                "meaning": "problem, question",
                "sentence": {
                    "japanese": "問題を解決しました。",
                    "romaji": "Mondai o kaiketsu shimashita.",
                    "english": "I solved the problem.",
                    "uzbek": "Muammoni hal qildim."
                }
            }
        ]
    },
    {
        "id": "n3-196",
        "kanji": "達",
        "readings": {"on": ["たつ"], "kun": []},
        "meanings": ["reach", "achieve", "attain"],
        "jlptLevel": "N3",
        "frequency": 196,
        "strokes": 12,
        "examples": [
            {
                "word": "到達",
                "reading": "とうたつ",
                "meaning": "arrival, reaching",
                "sentence": {
                    "japanese": "目的地に到達しました。",
                    "romaji": "Mokutekichi ni tōtatsu shimashita.",
                    "english": "I reached the destination.",
                    "uzbek": "Maqsadga yetdim."
                }
            }
        ]
    },
    {
        "id": "n3-197",
        "kanji": "単",
        "readings": {"on": ["たん"], "kun": []},
        "meanings": ["simple", "single", "alone"],
        "jlptLevel": "N3",
        "frequency": 197,
        "strokes": 9,
        "examples": [
            {
                "word": "単語",
                "reading": "たんご",
                "meaning": "word, vocabulary",
                "sentence": {
                    "japanese": "単語を覚えました。",
                    "romaji": "Tango o oboemashita.",
                    "english": "I memorized the word.",
                    "uzbek": "So'zni yodladim."
                }
            }
        ]
    },
    {
        "id": "n3-198",
        "kanji": "短",
        "readings": {"on": ["たん"], "kun": ["みじかい"]},
        "meanings": ["short", "brief"],
        "jlptLevel": "N3",
        "frequency": 198,
        "strokes": 12,
        "examples": [
            {
                "word": "短期",
                "reading": "たんき",
                "meaning": "short term",
                "sentence": {
                    "japanese": "短期の計画です。",
                    "romaji": "Tanki no keikaku desu.",
                    "english": "It's a short-term plan.",
                    "uzbek": "Qisqa muddatli reja."
                }
            }
        ]
    },
    {
        "id": "n3-199",
        "kanji": "談",
        "readings": {"on": ["だん"], "kun": []},
        "meanings": ["talk", "discussion", "conversation"],
        "jlptLevel": "N3",
        "frequency": 199,
        "strokes": 15,
        "examples": [
            {
                "word": "会談",
                "reading": "かいだん",
                "meaning": "meeting, conference",
                "sentence": {
                    "japanese": "会談を行いました。",
                    "romaji": "Kaidan o okonaimashita.",
                    "english": "We held a meeting.",
                    "uzbek": "Yig'ilish o'tkazdik."
                }
            }
        ]
    },
    {
        "id": "n3-200",
        "kanji": "地",
        "readings": {"on": ["ち", "じ"], "kun": []},
        "meanings": ["ground", "earth", "place"],
        "jlptLevel": "N3",
        "frequency": 200,
        "strokes": 6,
        "examples": [
            {
                "word": "土地",
                "reading": "とち",
                "meaning": "land, ground",
                "sentence": {
                    "japanese": "土地を購入しました。",
                    "romaji": "Tochi o kōnyū shimashita.",
                    "english": "I purchased land.",
                    "uzbek": "Yerni sotib oldim."
                }
            }
        ]
    },
    {
        "id": "n3-201",
        "kanji": "知",
        "readings": {"on": ["ち"], "kun": ["しる"]},
        "meanings": ["know", "understand", "wisdom"],
        "jlptLevel": "N3",
        "frequency": 201,
        "strokes": 8,
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
        "id": "n3-202",
        "kanji": "値",
        "readings": {"on": ["ち"], "kun": ["あたい", "ね"]},
        "meanings": ["value", "price", "worth"],
        "jlptLevel": "N3",
        "frequency": 202,
        "strokes": 10,
        "examples": [
            {
                "word": "価値",
                "reading": "かち",
                "meaning": "value, worth",
                "sentence": {
                    "japanese": "価値があります。",
                    "romaji": "Kachi ga arimasu.",
                    "english": "It has value.",
                    "uzbek": "Qiymati bor."
                }
            }
        ]
    },
    {
        "id": "n3-203",
        "kanji": "中",
        "readings": {"on": ["ちゅう"], "kun": ["なか"]},
        "meanings": ["middle", "center", "during"],
        "jlptLevel": "N3",
        "frequency": 203,
        "strokes": 4,
        "examples": [
            {
                "word": "中央",
                "reading": "ちゅうおう",
                "meaning": "center, central",
                "sentence": {
                    "japanese": "中央に置きました。",
                    "romaji": "Chūō ni okimashita.",
                    "english": "I placed it in the center.",
                    "uzbek": "Markazga qo'ydim."
                }
            }
        ]
    },
    {
        "id": "n3-204",
        "kanji": "注",
        "readings": {"on": ["ちゅう"], "kun": ["そそぐ", "つぐ"]},
        "meanings": ["pour", "focus", "note"],
        "jlptLevel": "N3",
        "frequency": 204,
        "strokes": 8,
        "examples": [
            {
                "word": "注意",
                "reading": "ちゅうい",
                "meaning": "attention, caution",
                "sentence": {
                    "japanese": "注意を払いました。",
                    "romaji": "Chūi o haraimashita.",
                    "english": "I paid attention.",
                    "uzbek": "E'tibor berdim."
                }
            }
        ]
    },
    {
        "id": "n3-205",
        "kanji": "柱",
        "readings": {"on": ["ちゅう"], "kun": ["はしら"]},
        "meanings": ["pillar", "column", "support"],
        "jlptLevel": "N3",
        "frequency": 205,
        "strokes": 9,
        "examples": [
            {
                "word": "支柱",
                "reading": "しちゅう",
                "meaning": "support pillar",
                "sentence": {
                    "japanese": "支柱を立てました。",
                    "romaji": "Shichū o tatemashita.",
                    "english": "I erected a support pillar.",
                    "uzbek": "Qo'llab-quvvatlovchi ustunni o'rnatdim."
                }
            }
        ]
    },
    {
        "id": "n3-206",
        "kanji": "調",
        "readings": {"on": ["ちょう"], "kun": ["しらべる", "ととのえる"]},
        "meanings": ["investigate", "adjust", "tune"],
        "jlptLevel": "N3",
        "frequency": 206,
        "strokes": 15,
        "examples": [
            {
                "word": "調査",
                "reading": "ちょうさ",
                "meaning": "investigation, survey",
                "sentence": {
                    "japanese": "調査を実施しました。",
                    "romaji": "Chōsa o jisshi shimashita.",
                    "english": "I conducted an investigation.",
                    "uzbek": "Tekshiruv o'tkazdim."
                }
            }
        ]
    },
    {
        "id": "n3-207",
        "kanji": "長",
        "readings": {"on": ["ちょう"], "kun": ["ながい", "おさ"]},
        "meanings": ["long", "leader", "chief"],
        "jlptLevel": "N3",
        "frequency": 207,
        "strokes": 8,
        "examples": [
            {
                "word": "長所",
                "reading": "ちょうしょ",
                "meaning": "merit, advantage",
                "sentence": {
                    "japanese": "長所を活かしました。",
                    "romaji": "Chōsho o ikashimashita.",
                    "english": "I utilized my strengths.",
                    "uzbek": "Afzalliklarimdan foydalandim."
                }
            }
        ]
    },
    {
        "id": "n3-208",
        "kanji": "鳥",
        "readings": {"on": ["ちょう"], "kun": ["とり"]},
        "meanings": ["bird"],
        "jlptLevel": "N3",
        "frequency": 208,
        "strokes": 11,
        "examples": [
            {
                "word": "小鳥",
                "reading": "ことり",
                "meaning": "small bird",
                "sentence": {
                    "japanese": "小鳥が鳴いています。",
                    "romaji": "Kotori ga naite imasu.",
                    "english": "A small bird is singing.",
                    "uzbek": "Kichik qush sayrayapti."
                }
            }
        ]
    },
    {
        "id": "n3-209",
        "kanji": "朝",
        "readings": {"on": ["ちょう"], "kun": ["あさ"]},
        "meanings": ["morning", "dawn"],
        "jlptLevel": "N3",
        "frequency": 209,
        "strokes": 12,
        "examples": [
            {
                "word": "朝食",
                "reading": "ちょうしょく",
                "meaning": "breakfast",
                "sentence": {
                    "japanese": "朝食を食べました。",
                    "romaji": "Chōshoku o tabemashita.",
                    "english": "I ate breakfast.",
                    "uzbek": "Nonushtani yedim."
                }
            }
        ]
    },
    {
        "id": "n3-210",
        "kanji": "直",
        "readings": {"on": ["ちょく"], "kun": ["なおる", "なおす", "ただちに"]},
        "meanings": ["straight", "direct", "fix"],
        "jlptLevel": "N3",
        "frequency": 210,
        "strokes": 8,
        "examples": [
            {
                "word": "直接",
                "reading": "ちょくせつ",
                "meaning": "direct, immediate",
                "sentence": {
                    "japanese": "直接話しました。",
                    "romaji": "Chokusetsu hanashimashita.",
                    "english": "I spoke directly.",
                    "uzbek": "To'g'ridan-to'g'ri gapirdim."
                }
            }
        ]
    },
    {
        "id": "n3-211",
        "kanji": "通",
        "readings": {"on": ["つう"], "kun": ["とおる", "かよう"]},
        "meanings": ["pass through", "commute", "understand"],
        "jlptLevel": "N3",
        "frequency": 211,
        "strokes": 10,
        "examples": [
            {
                "word": "通学",
                "reading": "つうがく",
                "meaning": "commuting to school",
                "sentence": {
                    "japanese": "電車で通学しています。",
                    "romaji": "Densha de tsūgaku shite imasu.",
                    "english": "I commute to school by train.",
                    "uzbek": "Poyezdda maktabga boraman."
                }
            }
        ]
    },
    {
        "id": "n3-212",
        "kanji": "低",
        "readings": {"on": ["てい"], "kun": ["ひくい"]},
        "meanings": ["low", "short", "inferior"],
        "jlptLevel": "N3",
        "frequency": 212,
        "strokes": 7,
        "examples": [
            {
                "word": "最低",
                "reading": "さいてい",
                "meaning": "lowest, minimum",
                "sentence": {
                    "japanese": "最低の条件です。",
                    "romaji": "Saitei no jōken desu.",
                    "english": "It's the minimum condition.",
                    "uzbek": "Minimal shart."
                }
            }
        ]
    },
    {
        "id": "n3-213",
        "kanji": "定",
        "readings": {"on": ["てい"], "kun": ["さだめる", "さだまる"]},
        "meanings": ["decide", "fix", "regular"],
        "jlptLevel": "N3",
        "frequency": 213,
        "strokes": 8,
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
        "id": "n3-214",
        "kanji": "庭",
        "readings": {"on": ["てい"], "kun": ["にわ"]},
        "meanings": ["garden", "yard", "courtyard"],
        "jlptLevel": "N3",
        "frequency": 214,
        "strokes": 10,
        "examples": [
            {
                "word": "庭園",
                "reading": "ていえん",
                "meaning": "garden, park",
                "sentence": {
                    "japanese": "庭園を散歩しました。",
                    "romaji": "Teien o sanpo shimashita.",
                    "english": "I took a walk in the garden.",
                    "uzbek": "Bog'da sayr qildim."
                }
            }
        ]
    },
    {
        "id": "n3-215",
        "kanji": "停",
        "readings": {"on": ["てい"], "kun": ["とまる"]},
        "meanings": ["stop", "halt", "park"],
        "jlptLevel": "N3",
        "frequency": 215,
        "strokes": 11,
        "examples": [
            {
                "word": "停止",
                "reading": "ていし",
                "meaning": "stop, halt",
                "sentence": {
                    "japanese": "停止しました。",
                    "romaji": "Teishi shimashita.",
                    "english": "I stopped.",
                    "uzbek": "To'xtadim."
                }
            }
        ]
    },
    {
        "id": "n3-216",
        "kanji": "的",
        "readings": {"on": ["てき"], "kun": ["まと"]},
        "meanings": ["target", "aim", "adjective suffix"],
        "jlptLevel": "N3",
        "frequency": 216,
        "strokes": 8,
        "examples": [
            {
                "word": "目的",
                "reading": "もくてき",
                "meaning": "purpose, aim",
                "sentence": {
                    "japanese": "目的を達成しました。",
                    "romaji": "Mokuteki o tassei shimashita.",
                    "english": "I achieved my purpose.",
                    "uzbek": "Maqsadga erishdim."
                }
            }
        ]
    },
    {
        "id": "n3-217",
        "kanji": "展",
        "readings": {"on": ["てん"], "kun": []},
        "meanings": ["exhibition", "display", "develop"],
        "jlptLevel": "N3",
        "frequency": 217,
        "strokes": 10,
        "examples": [
            {
                "word": "展示",
                "reading": "てんじ",
                "meaning": "exhibition, display",
                "sentence": {
                    "japanese": "展示を見ました。",
                    "romaji": "Tenji o mimashita.",
                    "english": "I viewed the exhibition.",
                    "uzbek": "Ko'rgazmani ko'rdim."
                }
            }
        ]
    },
    {
        "id": "n3-218",
        "kanji": "点",
        "readings": {"on": ["てん"], "kun": []},
        "meanings": ["point", "dot", "score"],
        "jlptLevel": "N3",
        "frequency": 218,
        "strokes": 9,
        "examples": [
            {
                "word": "点数",
                "reading": "てんすう",
                "meaning": "score, points",
                "sentence": {
                    "japanese": "点数が良かったです。",
                    "romaji": "Tensū ga yokatta desu.",
                    "english": "The score was good.",
                    "uzbek": "Ball yaxshi edi."
                }
            }
        ]
    },
    {
        "id": "n3-219",
        "kanji": "店",
        "readings": {"on": ["てん"], "kun": ["みせ"]},
        "meanings": ["shop", "store", "restaurant"],
        "jlptLevel": "N3",
        "frequency": 219,
        "strokes": 8,
        "examples": [
            {
                "word": "店員",
                "reading": "てんいん",
                "meaning": "shop clerk, employee",
                "sentence": {
                    "japanese": "店員に聞きました。",
                    "romaji": "Ten'in ni kikimashita.",
                    "english": "I asked the clerk.",
                    "uzbek": "Sotuvchidan so'radim."
                }
            }
        ]
    },
    {
        "id": "n3-220",
        "kanji": "電",
        "readings": {"on": ["でん"], "kun": []},
        "meanings": ["electricity", "electric"],
        "jlptLevel": "N3",
        "frequency": 220,
        "strokes": 13,
        "examples": [
            {
                "word": "電気",
                "reading": "でんき",
                "meaning": "electricity, electric",
                "sentence": {
                    "japanese": "電気を消しました。",
                    "romaji": "Denki o keshimashita.",
                    "english": "I turned off the electricity.",
                    "uzbek": "Elektrni o'chirdim."
                }
            }
        ]
    },
    {
        "id": "n3-221",
        "kanji": "都",
        "readings": {"on": ["と"], "kun": ["みやこ"]},
        "meanings": ["capital", "metropolis", "all"],
        "jlptLevel": "N3",
        "frequency": 221,
        "strokes": 11,
        "examples": [
            {
                "word": "首都",
                "reading": "しゅと",
                "meaning": "capital city",
                "sentence": {
                    "japanese": "首都に住んでいます。",
                    "romaji": "Shuto ni sunde imasu.",
                    "english": "I live in the capital.",
                    "uzbek": "Poytaxtda yashayman."
                }
            }
        ]
    },
    {
        "id": "n3-222",
        "kanji": "度",
        "readings": {"on": ["ど"], "kun": ["たび"]},
        "meanings": ["degree", "times", "frequency"],
        "jlptLevel": "N3",
        "frequency": 222,
        "strokes": 9,
        "examples": [
            {
                "word": "温度",
                "reading": "おんど",
                "meaning": "temperature",
                "sentence": {
                    "japanese": "温度を測りました。",
                    "romaji": "Ondo o hakari mashita.",
                    "english": "I measured the temperature.",
                    "uzbek": "Haroratni o'lchadim."
                }
            }
        ]
    },
    {
        "id": "n3-223",
        "kanji": "登",
        "readings": {"on": ["とう"], "kun": ["のぼる"]},
        "meanings": ["climb", "ascend", "register"],
        "jlptLevel": "N3",
        "frequency": 223,
        "strokes": 12,
        "examples": [
            {
                "word": "登山",
                "reading": "とざん",
                "meaning": "mountain climbing",
                "sentence": {
                    "japanese": "登山をしました。",
                    "romaji": "Tozan o shimashita.",
                    "english": "I went mountain climbing.",
                    "uzbek": "Tog'ga chiqdim."
                }
            }
        ]
    },
    {
        "id": "n3-224",
        "kanji": "等",
        "readings": {"on": ["とう"], "kun": ["ひとしい", "など"]},
        "meanings": ["equal", "etc.", "class"],
        "jlptLevel": "N3",
        "frequency": 224,
        "strokes": 12,
        "examples": [
            {
                "word": "平等",
                "reading": "びょうどう",
                "meaning": "equality, equal",
                "sentence": {
                    "japanese": "平等を求めます。",
                    "romaji": "Byōdō o motomemasu.",
                    "english": "I seek equality.",
                    "uzbek": "Tenglikni qidiraman."
                }
            }
        ]
    },
    {
        "id": "n3-225",
        "kanji": "動",
        "readings": {"on": ["どう"], "kun": ["うごく", "うごかす"]},
        "meanings": ["move", "motion", "change"],
        "jlptLevel": "N3",
        "frequency": 225,
        "strokes": 11,
        "examples": [
            {
                "word": "運動",
                "reading": "うんどう",
                "meaning": "exercise, movement",
                "sentence": {
                    "japanese": "運動をしました。",
                    "romaji": "Undō o shimashita.",
                    "english": "I exercised.",
                    "uzbek": "Mashq qildim."
                }
            }
        ]
    },
    {
        "id": "n3-226",
        "kanji": "同",
        "readings": {"on": ["どう"], "kun": ["おなじ"]},
        "meanings": ["same", "together", "similar"],
        "jlptLevel": "N3",
        "frequency": 226,
        "strokes": 6,
        "examples": [
            {
                "word": "同時",
                "reading": "どうじ",
                "meaning": "simultaneous, same time",
                "sentence": {
                    "japanese": "同時に始めました。",
                    "romaji": "Dōji ni hajimemashita.",
                    "english": "We started at the same time.",
                    "uzbek": "Bir vaqtda boshladik."
                }
            }
        ]
    },
    {
        "id": "n3-227",
        "kanji": "道",
        "readings": {"on": ["どう"], "kun": ["みち"]},
        "meanings": ["road", "way", "path"],
        "jlptLevel": "N3",
        "frequency": 227,
        "strokes": 12,
        "examples": [
            {
                "word": "道路",
                "reading": "どうろ",
                "meaning": "road, highway",
                "sentence": {
                    "japanese": "道路を歩きました。",
                    "romaji": "Dōro o arukimashita.",
                    "english": "I walked on the road.",
                    "uzbek": "Yo'lda yurdim."
                }
            }
        ]
    },
    {
        "id": "n3-228",
        "kanji": "特",
        "readings": {"on": ["とく"], "kun": []},
        "meanings": ["special", "particular", "especially"],
        "jlptLevel": "N3",
        "frequency": 228,
        "strokes": 10,
        "examples": [
            {
                "word": "特別",
                "reading": "とくべつ",
                "meaning": "special, particular",
                "sentence": {
                    "japanese": "特別な日です。",
                    "romaji": "Tokubetsu na hi desu.",
                    "english": "It's a special day.",
                    "uzbek": "Maxsus kun."
                }
            }
        ]
    },
    {
        "id": "n3-229",
        "kanji": "読",
        "readings": {"on": ["どく"], "kun": ["よむ"]},
        "meanings": ["read", "study"],
        "jlptLevel": "N3",
        "frequency": 229,
        "strokes": 14,
        "examples": [
            {
                "word": "読書",
                "reading": "どくしょ",
                "meaning": "reading",
                "sentence": {
                    "japanese": "読書をしました。",
                    "romaji": "Dokusho o shimashita.",
                    "english": "I read books.",
                    "uzbek": "Kitob o'qidim."
                }
            }
        ]
    },
    {
        "id": "n3-230",
        "kanji": "内",
        "readings": {"on": ["ない"], "kun": ["うち"]},
        "meanings": ["inside", "within", "internal"],
        "jlptLevel": "N3",
        "frequency": 230,
        "strokes": 4,
        "examples": [
            {
                "word": "内容",
                "reading": "ないよう",
                "meaning": "content, substance",
                "sentence": {
                    "japanese": "内容を確認しました。",
                    "romaji": "Naiyō o kakunin shimashita.",
                    "english": "I confirmed the content.",
                    "uzbek": "Mazmunni tekshirdim."
                }
            }
        ]
    },
    {
        "id": "n3-231",
        "kanji": "南",
        "readings": {"on": ["なん"], "kun": ["みなみ"]},
        "meanings": ["south"],
        "jlptLevel": "N3",
        "frequency": 231,
        "strokes": 9,
        "examples": [
            {
                "word": "南側",
                "reading": "みなみがわ",
                "meaning": "south side",
                "sentence": {
                    "japanese": "南側にあります。",
                    "romaji": "Minamigawa ni arimasu.",
                    "english": "It's on the south side.",
                    "uzbek": "Janubiy tomonda."
                }
            }
        ]
    },
    {
        "id": "n3-232",
        "kanji": "難",
        "readings": {"on": ["なん"], "kun": ["むずかしい", "かたい"]},
        "meanings": ["difficult", "trouble", "disaster"],
        "jlptLevel": "N3",
        "frequency": 232,
        "strokes": 18,
        "examples": [
            {
                "word": "困難",
                "reading": "こんなん",
                "meaning": "difficulty, hardship",
                "sentence": {
                    "japanese": "困難を乗り越えました。",
                    "romaji": "Konnan o norikoemashita.",
                    "english": "I overcame the difficulty.",
                    "uzbek": "Qiyinchilikni engib o'tdim."
                }
            }
        ]
    },
    {
        "id": "n3-233",
        "kanji": "二",
        "readings": {"on": ["に"], "kun": ["ふたつ", "ふた"]},
        "meanings": ["two", "second"],
        "jlptLevel": "N3",
        "frequency": 233,
        "strokes": 2,
        "examples": [
            {
                "word": "二回",
                "reading": "にかい",
                "meaning": "twice, two times",
                "sentence": {
                    "japanese": "二回読みました。",
                    "romaji": "Nikai yomimashita.",
                    "english": "I read it twice.",
                    "uzbek": "Ikki marta o'qidim."
                }
            }
        ]
    },
    {
        "id": "n3-234",
        "kanji": "日",
        "readings": {"on": ["にち", "じつ"], "kun": ["ひ", "か"]},
        "meanings": ["day", "sun", "Japan"],
        "jlptLevel": "N3",
        "frequency": 234,
        "strokes": 4,
        "examples": [
            {
                "word": "日曜日",
                "reading": "にちようび",
                "meaning": "Sunday",
                "sentence": {
                    "japanese": "日曜日に休みました。",
                    "romaji": "Nichiyōbi ni yasumimashita.",
                    "english": "I rested on Sunday.",
                    "uzbek": "Yakshanba kuni dam oldim."
                }
            }
        ]
    },
    {
        "id": "n3-235",
        "kanji": "入",
        "readings": {"on": ["にゅう"], "kun": ["いる", "はいる"]},
        "meanings": ["enter", "insert", "income"],
        "jlptLevel": "N3",
        "frequency": 235,
        "strokes": 2,
        "examples": [
            {
                "word": "入学",
                "reading": "にゅうがく",
                "meaning": "entering school",
                "sentence": {
                    "japanese": "大学に入学しました。",
                    "romaji": "Daigaku ni nyūgaku shimashita.",
                    "english": "I entered university.",
                    "uzbek": "Universitetga kirdim."
                }
            }
        ]
    },
    {
        "id": "n3-236",
        "kanji": "年",
        "readings": {"on": ["ねん"], "kun": ["とし"]},
        "meanings": ["year", "age"],
        "jlptLevel": "N3",
        "frequency": 236,
        "strokes": 6,
        "examples": [
            {
                "word": "年間",
                "reading": "ねんかん",
                "meaning": "yearly, annual",
                "sentence": {
                    "japanese": "年間計画を立てました。",
                    "romaji": "Nenkan keikaku o tatemashita.",
                    "english": "I made an annual plan.",
                    "uzbek": "Yillik reja tuzdim."
                }
            }
        ]
    },
    {
        "id": "n3-237",
        "kanji": "念",
        "readings": {"on": ["ねん"], "kun": []},
        "meanings": ["thought", "idea", "concern"],
        "jlptLevel": "N3",
        "frequency": 237,
        "strokes": 8,
        "examples": [
            {
                "word": "記念",
                "reading": "きねん",
                "meaning": "commemoration, memory",
                "sentence": {
                    "japanese": "記念写真を撮りました。",
                    "romaji": "Kinen shashin o torimashita.",
                    "english": "I took a commemorative photo.",
                    "uzbek": "Xotira suratini oldim."
                }
            }
        ]
    },
    {
        "id": "n3-238",
        "kanji": "能",
        "readings": {"on": ["のう"], "kun": []},
        "meanings": ["ability", "talent", "can"],
        "jlptLevel": "N3",
        "frequency": 238,
        "strokes": 10,
        "examples": [
            {
                "word": "能力",
                "reading": "のうりょく",
                "meaning": "ability, capability",
                "sentence": {
                    "japanese": "能力を発揮しました。",
                    "romaji": "Nōryoku o hakki shimashita.",
                    "english": "I demonstrated my ability.",
                    "uzbek": "Qobiliyatni namoyish qildim."
                }
            }
        ]
    },
    {
        "id": "n3-239",
        "kanji": "農",
        "readings": {"on": ["のう"], "kun": []},
        "meanings": ["agriculture", "farming"],
        "jlptLevel": "N3",
        "frequency": 239,
        "strokes": 13,
        "examples": [
            {
                "word": "農業",
                "reading": "のうぎょう",
                "meaning": "agriculture, farming",
                "sentence": {
                    "japanese": "農業を学んでいます。",
                    "romaji": "Nōgyō o manande imasu.",
                    "english": "I'm studying agriculture.",
                    "uzbek": "Qishloq xo'jaligini o'rganaman."
                }
            }
        ]
    },
    {
        "id": "n3-240",
        "kanji": "配",
        "readings": {"on": ["はい"], "kun": ["くばる"]},
        "meanings": ["distribute", "arrange", "serve"],
        "jlptLevel": "N3",
        "frequency": 240,
        "strokes": 10,
        "examples": [
            {
                "word": "配達",
                "reading": "はいたつ",
                "meaning": "delivery",
                "sentence": {
                    "japanese": "配達をしました。",
                    "romaji": "Haitatsu o shimashita.",
                    "english": "I made a delivery.",
                    "uzbek": "Yetkazib berdim."
                }
            }
        ]
    },
    {
        "id": "n3-241",
        "kanji": "敗",
        "readings": {"on": ["はい"], "kun": ["やぶれる"]},
        "meanings": ["defeat", "failure", "lose"],
        "jlptLevel": "N3",
        "frequency": 241,
        "strokes": 11,
        "examples": [
            {
                "word": "失敗",
                "reading": "しっぱい",
                "meaning": "failure, mistake",
                "sentence": {
                    "japanese": "失敗から学びました。",
                    "romaji": "Shippai kara manabimashita.",
                    "english": "I learned from failure.",
                    "uzbek": "Muvaffaqiyatsizlikdan o'rganadim."
                }
            }
        ]
    },
    {
        "id": "n3-242",
        "kanji": "売",
        "readings": {"on": ["ばい"], "kun": ["うる", "うれる"]},
        "meanings": ["sell", "sale"],
        "jlptLevel": "N3",
        "frequency": 242,
        "strokes": 7,
        "examples": [
            {
                "word": "販売",
                "reading": "はんばい",
                "meaning": "sales, selling",
                "sentence": {
                    "japanese": "販売を開始しました。",
                    "romaji": "Hanbai o kaishi shimashita.",
                    "english": "I started selling.",
                    "uzbek": "Sotishni boshladim."
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
