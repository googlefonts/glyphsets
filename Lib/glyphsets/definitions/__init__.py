# Google Fonts glyphset definitions to be consumed by other tools.
# The "script" value needs to correspond to the folder name
# in /GF_Glyphsets of this repo in order to find the other definition files.

glyphset_definitions = {
    "GF_Arabic_Core": {
        "script": "Arabic",
        "description": "Basic character set covering the 3 most widely used languages",
        "language_codes": [
            "ar_Arab",  # Arabic
            "fa_Arab",  # Persian
            "ur_Arab",  # Urdu
        ],
    },
    "GF_Arabic_Plus": {
        "script": "Arabic",
        "description": "Covering additional less widely used languages (but not characters needed for historical or specialized texts)",
        "language_codes": [
            "ckb_Arab",  # Kurdish
            "ms_Arab",  # Malay
            "ps_Arab",  # Pashto
            "sd_Arab",  # Sindhi
            "ug_Arab",  # Uyghur
        ],
    },
    "GF_Cyrillic_Core": {
        "script": "Cyrillic",
        "language_codes": [
            "ru_Cyrl",
            "uk_Cyrl",
            "sr_Cyrl",
            "be_Cyrl",
            "bg_Cyrl",
            "bs_Cyrl",
        ],
    },
    "GF_Cyrillic_Historical": {
        "script": "Cyrillic",
        "description": "Provides support for Pre-Petrine Old Church Slavonic Texts",
    },
    "GF_Cyrillic_Plus": {
        "script": "Cyrillic",
        "description": """Includes added language coverage for Slavic, Non-Slavic, and Uralic languages. Supports the following 90 Cyrillic languages: Abaza, Adyghe, Agul, Akhvakh, Altay, Andi, Archi, Avar, Azerbaijani (Cyrillic), Bagvalal Balkar, Bashkir, Belarusian (Cyrillic), Bosnian (Cyrillic), Botlikh, Budukh, Bulgarian, Buryat, Chamalal, Chechen, Chuvash, Crimean Tatar (Cyrillic), Croatian (Cyrillic), Dargwa/Dargin, Dungan, Erzya, Gagauz (Cyrillic), Godoberi, Hinukh, Hunzib, Ingush, Juhuri/çuhuri (Cyrillic), Kabardian, Kalmyk, Karachay, Karaim (Cyrillic), Karakalpak (Cyrillic), Karata, Kazakh, Ket (Cyrillic), Khakas (Cyrillic), Khinalugh, Komi, Krymchak, Kryts, Kubachi, Kumyk, Kurdish (Cyrillic), Kurdish (Cyrillic), Kyrgyz (Cyrillic), Lak, Lezgian, Lingua Franca Nova (Cyrillic), Macedonian, Mari (Hill and Meadow), Moksha, Moldovan (Cyrillic), Mongolian (Cyrillic), Montenigrin (Cyrillic), Nanai, Nogai, Ossetian, Russian, Rusyn, Rutul, Serbian (Cyrillic), Shor, Slovio, Tabassaran, Tajik, Talysh (Cyrillic), Tat, Tatar, Tindi, Tofa, Tsakhur (Cyrillic), Tsez, Turkmen, Tuvan/Tuvinian, Udi, Udmurt, Ukrainian, Urum, Uyghur (Cyrillic), Uzbek (Cyrillic), Votik (Cyrillic), Wakhi (Cyrillic), West Polesian, Yaghnobi (Cyrillic), Yukaghir (Northern and Southern)

Includes currencies: ₮, ₴, ₸.

The ruble sign (₽ U+20BD) is not included, since it is already present in the Latin Plus set.""",
    },
    "GF_Cyrillic_Pro": {
        "script": "Cyrillic",
        "description": """For Headline typefaces (?), with language support more Non-Slavic languages. Additional characters in this set provide support for the following 18 languages: Abkhaz, Chukchi, Enets, Eskimo, Even, Evenki, Itelmen, Khanty, Kildin Sami, Koryak, Mansi, Nganasan, Nenets, Oroch, Orok, Sakha/Yakut, Tati, Yukaghir, Yupik Ulch""",
    },
    "GF_Greek_AncientMusicalSymbols": {
        "script": "Greek",
        "description": """**Scholarly Use:** Greek and Byzantine Musical Symbols

* Greek Vocal Notation Symbols
* Greek Instrumental Notation Symbols
* Byzantine Musical Symbols""",
    },
    "GF_Greek_Archaic": {
        "script": "Greek",
        "description": """**Scholarly Use:** Variable Letterforms for Ancient Texts, Papyri

* Archaic UC `ϘϚϜϞϠϺ`
* Archaic LC `ϙϛϝϟϡϻ`
* Variant Letterforms `κρςΣ`, `Θϐϑϒϓϔϕϖε϶`
* Additional Letter `ϳ`
* Additional Archaic Letters for Bactrian `Ϸϸ`
* Symbols `ϼ ☧`
* Editorial Symbols `ϽϾϿ`
* Ancient Greek Mathematical Character `⟀ ⟁`
* Ancient Greek Acrophonic Numerals `𐅀𐅁𐅂𐅃𐅆𐅇𐅈𐅉𐅊𐅋𐅌𐅍𐅎𐅏𐅐𐅑𐅒𐅓𐅔𐅕𐅖𐅗𐅘𐅙𐅚𐅛𐅜𐅝𐅞𐅟𐅠𐅡𐅢𐅣𐅤𐅥𐅦𐅧𐅨𐅩𐅪𐅫𐅬𐅭𐅮𐅯𐅰𐅱𐅲𐅳𐅴`
* Geometric shape `□`
* Astrological symbols `★☉☊☋☌☍☽☾☿♀♁♂♃♄♅♆♇♈♉♊♋♌♍♎♏♐♑♒♓`""",
    },
    "GF_Greek_Coptic": {
        "script": "Greek",
        "description": """**Scholarly Use:** Liturgical language for Coptic Church

Coptic `U+03E2` – `U+03EF`, Coptic Unicode block `U+2C80` – `U+2CFF`

* Coptic Letters `ϢϣϤϥϦϧϨϩϪϫϬϭϮϯ`
* Bohairic Coptic UC ` ⲀⲂⲄⲆⲈⲊⲌⲎⲐⲒⲔⲖⲘⲚⲜⲞⲠⲢⲤⲦⲨⲪⲬⲮⲰ`
* Bohairic Coptic LC ` ⲁⲃⲅⲇⲉⲋⲍⲏⲑⲓⲕⲗⲙⲛⲝⲟⲡⲣⲥⲧⲩⲫⲭⲯⲱ `
* Old Coptic and Dialect Letters UC` ⲲⲴⲶⲸⲺⲼⲾⳀⳂⳄⳆⳈⳊⳌⳎⳐⳒⳔⳖⳘⳚ`
* Old Coptic and Dialect Letters LC ` ⲳⲵⲷⲹⲻⲽⲿⳁⳃⳅⳇⳉⳋⳍⳏⳑⳓⳕⳗⳙⳛ `
* Old Nubian Letters ` ⳜⳞⳠⳢⳝⳟⳡⳣ `
* Symbols ` ⳤ⳥⳦⳧⳨⳩⳪ `
* Cryptogrammic Letters ` ⳫⳬⳭⳮ⳯⳰⳱ `
* Combining Marks ` ⳯⳰⳱ ` 
* Bohairic Coptic Letters ` Ⳳⳳ `
* Old Nubian Punctuation ` ⳹⳺⳻⳼ `
* Coptic Fraction ` ⳽ ` 
* Punctuation ` ⳾ ⳿ ` """,
    },
    "GF_Greek_Core": {
        "script": "Greek",
        "description": """**General Use:** Basic Monotonic set for everyday Modern Greek

* Basic Greek UC ` ΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫ `
* Basic Greek LC ` άέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώ `
* Punctuation ` · ; `
* Greek numeral signs or keraia ` ʹ ͵ `
* Accents `  ́ ΅ `
* Kai symbol ` ϗ Ϗ `""",
        "language_codes": ["el_Grek"],
    },
    "GF_Greek_Expert": {
        "script": "Greek",
        "description": """**General Use:** Small Caps for Core and Plus sets, Superscript Letters

* Core .sc `άέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώ`
* Plus .sc `ἀἁἂἃἄἅἆἇἐἑἒἓἔἕἠἡἢἣἤἥἦἧἰἱἲἳἴἵἶἷὀὁὂὃὄὅὐὑὒὓὔὕὖὗὠὡὢὣὤὥὦὧὰάὲέὴήὶίὸόὺύὼώᾀᾁᾂᾃᾄᾅᾆᾇᾐᾑᾒᾓᾔᾕᾖᾗᾠᾡᾢᾣᾤᾥᾦᾧᾰᾱᾲᾳᾴᾶᾷιῂῃῄῆῇῐῑῒΐῖῗῠῡῢΰῤῥῦῧῲῳῴῶῷ Ϗ`
* Archaic Numerals .sc `ϛ ϟ ϡ ϝ`
* Iota Adscript as ss01 .sc `ᾈᾉᾊᾋᾌᾍᾎᾏᾘᾙᾚᾛᾜᾝᾞᾟᾨᾩᾪᾫᾬᾭᾮᾯᾼῌῼ`
* Superior Letters .sups `ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρςστυφχψω`
* Ligatures `λλ γγ`""",
    },
    "GF_Greek_Plus": {
        "script": "Greek",
        "description": """**General Use:** Basic Polytonic set for Scholarly Greek

* Polytonic UC `ἈἉἊἋἌἍἎἏἘἙἚἛἜἝἨἩἪἫἬἭἮἯἸἹἺἻἼἽἾἿὈὉὊὋὌὍὙὛὝὟὨὩὪὫὬὭὮὯᾈᾉᾊᾋᾌᾍᾎᾏᾘᾙᾚᾛᾜᾝᾞᾟᾨᾩᾪᾫᾬᾭᾮᾯᾸᾹᾺΆᾼῈΈῊΉῌῘῙῚΊῨῩῪΎῬῸΌῺΏῼ `
* Polytonic LC ` ἀἁἂἃἄἅἆἇἐἑἒἓἔἕἠἡἢἣἤἥἦἧἰἱἲἳἴἵἶἷὀὁὂὃὄὅὐὑὒὓὔὕὖὗὠὡὢὣὤὥὦὧὰάὲέὴήὶίὸόὺύὼώᾀᾁᾂᾃᾄᾅᾆᾇᾐᾑᾒᾓᾔᾕᾖᾗᾠᾡᾢᾣᾤᾥᾦᾧᾰᾱᾲᾳᾴᾶᾷιῂῃῄῆῇῐῑῒΐῖῗῠῡῢΰῤῥῦῧῲῳῴῶῷ `
* Accents ```   ́ ` ῀ `  ```
* Breathings ` ῾ ᾿ `
* Combinations ` ῁ ῍ ῎ ῏ ῝ ῞ ῟  ̈́ `
* Diactritics `  ͅ ι `
* Punctuation ` ᾽ `
* Combining Marks `  ̓ ΅  ͂ ͅ `
* Iota Adscript as ss01 `ᾈᾉᾊᾋᾌᾍᾎᾏᾘᾙᾚᾛᾜᾝᾞᾟᾨᾩᾪᾫᾬᾭᾮᾯᾼῌῼ`""",
    },
    "GF_Greek_Pro": {
        "script": "Greek",
        "description": """**Scholarly Use:** Extended Polytonic Greek, for scholarly edition of ancient texts (Ancient and Roman Greece studies, Byzantine studies, Greek Biblical studies)

**[Learn how to draw good Polytonic Greek at irenevl.github.io/Polytonic-tutorial](https://irenevl.github.io/Polytonic-tutorial/)**

**N.B.** List of characters from GF Latin Plus and Pro sets that are prerequisites to this set.

№ | char | nice name (Glyphs App) | uni name | set
---|---|---|---|---
1|²|twosuperior|uni00B2|GF Latin Plus
2|³|threesuperior|uni00B3|GF Latin Plus
3|¹|onesuperior|uni00B9|GF Latin Plus
4|⁰|zerosuperior|uni0270|GF Latin Pro
5|†|dagger|uni2020|GF Latin Plus
6|‡|daggerdbl|uni2021|GF Latin Plus
7|⁴|foursuperior|uni2074|GF Latin Plus
8|⁵|fivesuperior|uni2075|GF Latin Pro
9|⁶|sixsuperior|uni2076|GF Latin Pro
10|⁷|sevensuperior|uni2077|GF Latin Pro
11|⁸|eightsuperior|uni2078|GF Latin Pro
12|⁹|ninesuperior|uni2079|GF Latin Pro
13|₀|zeroinferior|uni2080|GF Latin Pro
14|₁|oneinferior|uni2081|GF Latin Pro
15|₂|twoinferior|uni2082|GF Latin Pro
16|₃|threeinferior|uni2083|GF Latin Pro
17|₄|fourinferior|uni2084|GF Latin Pro
18|₅|fiveinferior|uni2085|GF Latin Pro
19|₆|sixinferior|uni2086|GF Latin Pro
20|₇|seveninferior|uni2087|GF Latin Pro
21|₈|eightinferior|uni2088|GF Latin Pro
22|₉|nineinferior|uni2089|GF Latin Pro


* Archaic Letters and Numerals `Ϛ Ϟ Ϡ Ϝ ϛ ϟ ϡ ϝ`
* Ancient Greek Textual symbols `⸎ ⸏ ⸐ ⸑ ⸒ ⸓ ⸔ ⸕ ⸖ ⸗`
* Archaic Punctuation `※ ⁂ ‿ ͜ ˙ ⁖ ⁘ ⁙ ⁚ ⁛ ⁜ ⁝ ⁞ ⊗ ⋮`
* Greek Metrical Symbols `⏑ ⏒ ⏓ ⏔ ⏕ ⏖ ⏗ ⏘ ⏙`
* Critical Sigla `̅ ̣ ͙ ‖ ⁺ ⁻ ⁼ ₊ ₋ ₌ ⫽ ⸀ ⸁ ⸂ ⸃ ⸄ ⸅ ⸆ ⸇ ⸈ ⸉ ⸊ ⸋ ⸌ ⸍ 〈 〉《 》「 」〚 〛`
* Biblical Apparatus `ℵ ℶ 𝑙 𝔖 𝔐 𝔓 𝔭`


**N.B.** For certain design cases it is best practice to include inital and final variants of ` ̅` overlinecomb (uni0305):

* `overlinecomb.init`, cropped on the left
* `overlinecomb.fina`, cropped on the right""",
    },
    "GF_Latin_African": {
        "script": "Latin",
        "use_auxiliary": True,
        "historical": False,
        "population": 1,
        "regions": "AO BF BI BJ BW CD CF CG CI CM CV DJ DZ EA EG EH ER ET GA "
        "GH GM GN GQ GW IC IO KE KM LR LS LY MA MG ML MR MU MW MZ "
        "NA NE NG RE RW SC SD SH SL SN SO SS ST SZ TD TF TG TN TZ "
        "UG YT ZA ZM ZW ".split(),
    },
    "GF_Latin_Core": {
        "script": "Latin",
        "description": """Languages of Europe and the Americas with >5M speakers, with manually curated exceptions. This set is the minimal set required for all families meant to be onboarded into Google Fonts.

**This below is taken from the old README and is not accurate, as it lists languages that accidentally happen to be covered under this glyphset but are not actually intended to be covered here. This set needs more consideration:** Acheron, Achinese, Afrikaans, Anuta, Aragonese, Arbëreshë Albanian, Arvanitika Albanian, Ashéninka Perené, Balinese, Bari, Basque, Bosnian, Breton, Caquinte, Caribbean Hindustani, Cashibo-Cacataibo, Catalan, Central Aymara, Central Kurdish, Chamorro, Chavacano, Chiltepec Chinantec, Chuukese, Cimbrian, Cofán, Cook Islands Māori, Cornish, Corsican, Creek, Crimean Tatar, Croatian, Czech, Danish, Dehu, Dutch, Eastern Abnaki, English, Ese Ejja, Faroese, Filipino, Finnish, French, Friulian, Galician, Ganda, Garifuna, Ga’anda, German, Gheg Albanian, Gooniyandi, Guadeloupean Creole French, Haitian, Hawaiian, Ho-Chunk, Hopi, Hungarian, Hän, Icelandic, Iloko, Inari Sami, Irish, Istro Romanian, Italian, Javanese, Jola-Fonyi, Kabuverdianu, Kaonde, Karelian, Kashubian, Khasi, Konzo, Kven Finnish, Kölsch, Ladin, Latgalian, Ligurian, Lithuanian, Lombard, Low German, Lower Sorbian, Lule Sami, Luxembourgish, Macedo-Romanian, Makhuwa, Malagasy, Maltese, Manx, Maori, Mapudungun, Marshallese, Matsés, Meriam Mir, Meru, Mohawk, Montagnais, Montenegrin, Munsee, Mískito, Neapolitan, Niuean, Nomatsiguenga, Northern Kurdish, Norwegian, Nyanja, Occitan, Ojitlán Chinantec, Oroqen, Palauan, Papantla Totonac, Papiamento, Pedi, Picard, Pichis Ashéninka, Piemontese, Pijin, Pipil, Polish, Portuguese, Potawatomi, Purepecha, Quechua, Romanian, Romansh, Samoan, Sango, Sangu (Tanzania), Saramaccan, Sardinian, Scottish Gaelic, Seri, Sicilian, Silesian, Slovak, Slovenian, Southern Aymara, Southern Sami, Southern Sotho, Spanish, Sranan Tongo, Standard Estonian, Standard Latvian, Sundanese, Swedish, Swiss German, Tagalog, Tahitian, Teso, Tetum, Tetun Dili, Tiv, Tokelau, Tonga (Tonga Islands), Tonga (Zambia), Tosk Albanian, Tswana, Turkish, Turkmen, Uab Meto, Upper Sorbian, Venetian, Veps, Võro, Walloon, Waray (Philippines), Wayuu, Welsh, Western Abnaki, Western Frisian, Wolof, Yanesha', Yao, Yapese, Yucateco, Zapotec, Záparo.""",
        "language_codes": [
            "ca_Latn",  # Catalan
            "cs_Latn",  # Czech
            "cy_Latn",  # Welsh
            "da_Latn",  # Danish
            "de_Latn",  # German
            "en_Latn",  # English
            "es_Latn",  # Spanish
            "fi_Latn",  # Finnish
            "fr_Latn",  # French
            "hr_Latn",  # Croatian
            "hu_Latn",  # Hungarian
            "is_Latn",  # Icelandic
            "it_Latn",  # Italian
            "lt_Latn",  # Lithuanian
            "lv_Latn",  # Latvian
            "mt_Latn",  # Maltese
            "nb_Latn",  # Norwegian Bokmål
            "nl_Latn",  # Dutch
            "pl_Latn",  # Polish
            "pt_Latn",  # Portuguese
            "ro_Latn",  # Romanian
            "sk_Latn",  # Slovak
            "sq_Latn",  # Albanian
            "sr_Latn",  # Serbian (Latin)
            "sv_Latn",  # Swedish
            "tr_Latn",  # Turkish
        ],
    },
    "GF_Latin_Kernel": {
        "script": "Latin",
        "description": """Support ASCII + necessary punctuation and symbols for English language. This set is the minimal set required for non-latin script families that are not meant to be used in latin language based context. 

English support is still mandatory for technical reasons: application support on one hand, and GF platform display on the other hand (to avoid .notdef glyphs appearing everywhere on the website). GF encourages designers to also support GF Latin Core glyphset, in addition to any script, so native speakers living abroad can also enjoy and use the font wherever they are in the world.

**This below is taken from the old README and is not accurate, as it lists languages that accidentally happen to be covered under this glyphset but are not actually intended to be covered here. This set needs more consideration:** Afar, Eastern Arrernte, Amahuaca, Amis, Amarakaeri, Asu (Tanzania), Batak Toba, Bemba (Zambia), Bena (Tanzania), Bikol, Bislama, Batak Dairi, Batak Mandailing, Batak Simalungun, Batak Karo, Candoshi-Shapra, Cebuano, Chiga, Chokwe, Asháninka, Seselwa Creole French, Tedim Chin, Taita, Andaandi, Dongolawi, Nobiin, Fijian, Borana-Arsi-Guji Oromo, West Central Oromo, Gilbertese, Gusii, Eastern Oromo, Northern Qiandong Miao, Hiligaynon, Southern Qiandong Miao, Hani, Huastec, Indonesian, Jamaican Creole English, Japanese, Kalaallisut, Makonde, Kekchí, Kinyarwanda, Kalenjin, Kimbundu, Kongo, Shambala, Kituba (DRC), Kuanyama, Ladino, Latin, Luba-Lulua, Luo (Kenya and Tanzania), Mauritian Creole, Makhuwa-Meetto, Minangkabau, Murrinh-Patha, Ixcatlán Mazatec, Naga Pidgin, South Ndebele, North Ndebele, Ndonga, Ao Naga, Nyankole, Orma, Pampanga, Pintupi-Luritja, Paluan, Pohnpeian, Upper Guinea Crioulo, K'iche', Rotokas, Rundi, Rwa, Samburu, Sena, Shipibo-Conibo, Shawnee, Shona, Soninke, Somali, Swati, Maore Comorian, Congo Swahili, Swahili, Tok Pisin, Tsonga, Tumbuka, Tzeltal, Tzotzil, Northern Uzbek, Warlpiri, Wik-Mungkan, Mwani, Wiradjuri, Wangaaybuwan-Ngiyambaa, Xhosa, Kenzi, Mattokki, Soga, Yindjibarndi, Makwe, Ngazidja Comorian, Malaysian, Standard Malay, Zulu.
""",
    },
    "GF_Latin_Beyond": {
        "script": "Latin",
        "description": """Support for indigenous Latin-based languages from European and American regions (< 5M speakers), that are not supported in Latin Core.

**This below is taken from the old README and is not accurate, as it lists languages that accidentally happen to be covered under this glyphset but are not actually intended to be covered here. This set needs more consideration:** Abron, Acholi, Achuar-Shiwiar, Adangme, Aguaruna, Ahtna, Akoose, Alekano, Aleut, Anaang, Anufo, Apinayé, Arabela, Asturian, Atayal, Awa-Cuaiquer, Awetí, Awing, Baatonum, Baoulé, Boko (Benin), Bora, Bouna Kulango, Buginese, Cashinahua, Chachi, Chayahuita, Dagbani, Dendi (Benin), Dimli, Dinka, Embu, Fanti, Ga, Gagauz, Gonja, Gwichʼin, Kaingang, Kamba (Kenya), Kaqchikel, Kikuyu, Kirmanjki, Krio, Kwak’wala, Lamnso', Lingala, Lozi, Luba-Katanga, Mandinka, Mandjak, Mankanya, Mende (Sierra Leone), Meta’, Metlatónoc Mixtec, Mezquital Otomi, Mi'kmaq, Mirandese, Murui Huitoto, Muslim Tat, Navajo, North Azerbaijani, Northeastern Dinka, Northern Kissi, Northern Sami, Nuer, Nuuchahnulth, Nyamwezi, Nyemba, Nzima, Otuho, Paraguayan Guaraní, Pite Sami, Páez, Secoya, Sharanahua, Shilluk, Shuar, Siona, Skolt Sami, South Azerbaijani, Southern Dagaare, Talysh, Ticuna, Toba, Tojolabal, Totontepec Mixe, Tsafiki, Tsakhur, Tuvalu, Twi, Umbundu, Ume Sami, Waama, Walser, Waorani, Wasa, Xavánte, Yagua, Yangben, Yanomamö, Zuni""",
    },
    "GF_Latin_Plus": {
        "script": "Latin",
        "description": "Additional set of symbols for basic math and economy. This includes the 3 sets Kernel/Core/Vietnamese. This set add to GF Core some support for all in use currencies and basic math symboles and punctuation. It adds necessary glyphs for fraction feature support. All fonts commissionned by Google should have a glyphset support up to this level: Core-Vietnamese-Plus.",
    },
    "GF_Latin_PriAfrican": {"script": "Latin"},
    "GF_Latin_Vietnamese": {
        "script": "Latin",
        "description": "Achuar-Shiwiar, Aguaruna, Apinayé, Bini, Cashinahua, Chachi, Embu, Kaingang, Kamba (Kenya), Kikuyu, Mirandese, Páez, Shuar, Toba, Umbundu, Vietnamese, Walser, Waorani, Xavánte",
    },
    "GF_Phonetics_APA": {
        "script": "Phonetics",
        "description": "These glyphs sets are still a work in progress. Any research, resource and contribution are welcome!!",
    },
    "GF_Phonetics_DisorderedSpeech": {
        "script": "Phonetics",
        "description": "These glyphs sets are still a work in progress. Any research, resource and contribution are welcome!!",
    },
    "GF_Phonetics_IPAHistorical": {
        "script": "Phonetics",
        "description": "These glyphs sets are still a work in progress. Any research, resource and contribution are welcome!!",
    },
    "GF_Phonetics_IPAStandard": {
        "script": "Phonetics",
        "description": "These glyphs sets are still a work in progress. Any research, resource and contribution are welcome!!",
    },
    "GF_Phonetics_SinoExt": {
        "script": "Phonetics",
        "description": "These glyphs sets are still a work in progress. Any research, resource and contribution are welcome!!",
    },
    "GF_TransLatin_Arabic": {
        "script": "TransLatin",
        "description": "These glyphs sets are still a work in progress. Any research, resource and contribution are welcome!!",
    },
    "GF_TransLatin_Pinyin": {
        "script": "TransLatin",
        "description": "These glyphs sets are still a work in progress. Any research, resource and contribution are welcome!!",
    },
}
