# Table of Contents:


| Arabic | Cyrillic | Greek | Latin | Phonetics | TransLatin |
| --- | --- | --- | --- | --- | --- |
| [✅ Core](#gf-arabic-core) | [✅ Core](#gf-cyrillic-core) | [🛑 AncientMusicalSymbols](#gf-greek-ancientmusicalsymbols) | [✅ African](#gf-latin-african) | [🛑 APA](#gf-phonetics-apa) | [🛑 Arabic](#gf-translatin-arabic) |
| [✅ Plus](#gf-arabic-plus) | [🛑 Historical](#gf-cyrillic-historical) | [🛑 Archaic](#gf-greek-archaic) | [🛑 Beyond](#gf-latin-beyond) | [🛑 DisorderedSpeech](#gf-phonetics-disorderedspeech) | [🛑 Pinyin](#gf-translatin-pinyin) |
|  | [🛑 Plus](#gf-cyrillic-plus) | [🛑 Coptic](#gf-greek-coptic) | [✅ Core](#gf-latin-core) | [🛑 IPAHistorical](#gf-phonetics-ipahistorical) |  |
|  | [🛑 Pro](#gf-cyrillic-pro) | [✅ Core](#gf-greek-core) | [🛑 Kernel](#gf-latin-kernel) | [🛑 IPAStandard](#gf-phonetics-ipastandard) |  |
|  |  | [🛑 Expert](#gf-greek-expert) | [🛑 Plus](#gf-latin-plus) | [🛑 SinoExt](#gf-phonetics-sinoext) |  |
|  |  | [🛑 Plus](#gf-greek-plus) | [🛑 PriAfrican](#gf-latin-priafrican) |  |  |
|  |  | [🛑 Pro](#gf-greek-pro) | [🛑 Vietnamese](#gf-latin-vietnamese) |  |  |

> [!NOTE]  
> This document is a human-readable representation of the glyphset defintions defined in `.yaml` files [here](/Lib/glyphsets/definitions/) and gets updated automatically as part of the `sh build.sh` command.


> [!NOTE]  
> The symbols ✅ and 🛑 above denote whether or not this glyphset is available as part of Fontbakery's `shape_languages` check; in other words, whether or not language codes are defined for it.



# GF Arabic Core

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> Basic character set covering the 3 most widely used languages

`GF_Arabic_Core` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Arabic_Core.yaml) as:

* Script: Arabic
* Characters and glyphs defined in [GF_Arabic_Core.stub.glyphs](/data/definitions/per_glyphset/GF_Arabic_Core.stub.glyphs)
* List of languages: `
Arabic (ar_Arab),
Persian (fa_Arab),
Urdu (ur_Arab)
`

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Arabic_Core.nam](/data/results/nam/GF_Arabic_Core.nam)

Glyphs.app source file: [GF_Arabic_Core.glyphs](/data/results/glyphs/GF_Arabic_Core.glyphs)

Text files: [GF_Arabic_Core.txt](/data/results/txt/nice-names/GF_Arabic_Core.txt) (nice names) and [GF_Arabic_Core.txt](/data/results/txt/nice-names/GF_Arabic_Core.txt) (production name)

Glyphs.app Custom Filter List (contains all Arabic glyphsets): [CustomFilter_GF_Arabic.plist](/data/results/plist/CustomFilter_GF_Arabic.plist)


# GF Arabic Plus

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> Covering additional less widely used languages (but not characters needed for historical or specialized texts)

`GF_Arabic_Plus` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Arabic_Plus.yaml) as:

* Script: Arabic
* List of languages: `
Central Kurdish (ckb_Arab),
Malay (Arabic) (ms_Arab),
Pashto (ps_Arab),
Sindhi (sd_Arab),
Uyghur (ug_Arab)
`

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Arabic_Plus.nam](/data/results/nam/GF_Arabic_Plus.nam)

Glyphs.app source file: [GF_Arabic_Plus.glyphs](/data/results/glyphs/GF_Arabic_Plus.glyphs)

Text files: [GF_Arabic_Plus.txt](/data/results/txt/nice-names/GF_Arabic_Plus.txt) (nice names) and [GF_Arabic_Plus.txt](/data/results/txt/nice-names/GF_Arabic_Plus.txt) (production name)

Glyphs.app Custom Filter List (contains all Arabic glyphsets): [CustomFilter_GF_Arabic.plist](/data/results/plist/CustomFilter_GF_Arabic.plist)


# GF Cyrillic Core

`GF_Cyrillic_Core` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Cyrillic_Core.yaml) as:

* Script: Cyrillic
* List of languages: `
Belarusian (be_Cyrl),
Bosnian (Cyrillic) (bs_Cyrl),
Bulgarian (bg_Cyrl),
Russian (ru_Cyrl),
Serbian (sr_Cyrl),
Ukrainian (uk_Cyrl)
`

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Cyrillic_Core.nam](/data/results/nam/GF_Cyrillic_Core.nam)

Glyphs.app source file: [GF_Cyrillic_Core.glyphs](/data/results/glyphs/GF_Cyrillic_Core.glyphs)

Text files: [GF_Cyrillic_Core.txt](/data/results/txt/nice-names/GF_Cyrillic_Core.txt) (nice names) and [GF_Cyrillic_Core.txt](/data/results/txt/nice-names/GF_Cyrillic_Core.txt) (production name)

Glyphs.app Custom Filter List (contains all Cyrillic glyphsets): [CustomFilter_GF_Cyrillic.plist](/data/results/plist/CustomFilter_GF_Cyrillic.plist)


# GF Cyrillic Historical

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> Provides support for Pre-Petrine Old Church Slavonic Texts

`GF_Cyrillic_Historical` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Cyrillic_Historical.yaml) as:

* Script: Cyrillic
* Characters and glyphs defined in [GF_Cyrillic_Historical.stub.glyphs](/data/definitions/per_glyphset/GF_Cyrillic_Historical.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Cyrillic_Historical.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Cyrillic_Historical.nam](/data/results/nam/GF_Cyrillic_Historical.nam)

Glyphs.app source file: [GF_Cyrillic_Historical.glyphs](/data/results/glyphs/GF_Cyrillic_Historical.glyphs)

Text files: [GF_Cyrillic_Historical.txt](/data/results/txt/nice-names/GF_Cyrillic_Historical.txt) (nice names) and [GF_Cyrillic_Historical.txt](/data/results/txt/nice-names/GF_Cyrillic_Historical.txt) (production name)

Glyphs.app Custom Filter List (contains all Cyrillic glyphsets): [CustomFilter_GF_Cyrillic.plist](/data/results/plist/CustomFilter_GF_Cyrillic.plist)


# GF Cyrillic Plus

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> Includes added language coverage for Slavic, Non-Slavic, and Uralic languages. Supports the following 90 Cyrillic languages: Abaza, Adyghe, Agul, Akhvakh, Altay, Andi, Archi, Avar, Azerbaijani (Cyrillic), Bagvalal Balkar, Bashkir, Belarusian (Cyrillic), Bosnian (Cyrillic), Botlikh, Budukh, Bulgarian, Buryat, Chamalal, Chechen, Chuvash, Crimean Tatar (Cyrillic), Croatian (Cyrillic), Dargwa/Dargin, Dungan, Erzya, Gagauz (Cyrillic), Godoberi, Hinukh, Hunzib, Ingush, Juhuri/çuhuri (Cyrillic), Kabardian, Kalmyk, Karachay, Karaim (Cyrillic), Karakalpak (Cyrillic), Karata, Kazakh, Ket (Cyrillic), Khakas (Cyrillic), Khinalugh, Komi, Krymchak, Kryts, Kubachi, Kumyk, Kurdish (Cyrillic), Kurdish (Cyrillic), Kyrgyz (Cyrillic), Lak, Lezgian, Lingua Franca Nova (Cyrillic), Macedonian, Mari (Hill and Meadow), Moksha, Moldovan (Cyrillic), Mongolian (Cyrillic), Montenigrin (Cyrillic), Nanai, Nogai, Ossetian, Russian, Rusyn, Rutul, Serbian (Cyrillic), Shor, Slovio, Tabassaran, Tajik, Talysh (Cyrillic), Tat, Tatar, Tindi, Tofa, Tsakhur (Cyrillic), Tsez, Turkmen, Tuvan/Tuvinian, Udi, Udmurt, Ukrainian, Urum, Uyghur (Cyrillic), Uzbek (Cyrillic), Votik (Cyrillic), Wakhi (Cyrillic), West Polesian, Yaghnobi (Cyrillic), Yukaghir (Northern and Southern)
> 
> Includes currencies: ₮, ₴, ₸.
> 
> The ruble sign (₽ U+20BD) is not included, since it is already present in the Latin Plus set.

`GF_Cyrillic_Plus` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Cyrillic_Plus.yaml) as:

* Script: Cyrillic
* Characters and glyphs defined in [GF_Cyrillic_Plus.stub.glyphs](/data/definitions/per_glyphset/GF_Cyrillic_Plus.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Cyrillic_Plus.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Cyrillic_Plus.nam](/data/results/nam/GF_Cyrillic_Plus.nam)

Glyphs.app source file: [GF_Cyrillic_Plus.glyphs](/data/results/glyphs/GF_Cyrillic_Plus.glyphs)

Text files: [GF_Cyrillic_Plus.txt](/data/results/txt/nice-names/GF_Cyrillic_Plus.txt) (nice names) and [GF_Cyrillic_Plus.txt](/data/results/txt/nice-names/GF_Cyrillic_Plus.txt) (production name)

Glyphs.app Custom Filter List (contains all Cyrillic glyphsets): [CustomFilter_GF_Cyrillic.plist](/data/results/plist/CustomFilter_GF_Cyrillic.plist)


# GF Cyrillic Pro

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> For Headline typefaces (?), with language support more Non-Slavic languages. Additional characters in this set provide support for the following 18 languages: Abkhaz, Chukchi, Enets, Eskimo, Even, Evenki, Itelmen, Khanty, Kildin Sami, Koryak, Mansi, Nganasan, Nenets, Oroch, Orok, Sakha/Yakut, Tati, Yukaghir, Yupik Ulch

`GF_Cyrillic_Pro` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Cyrillic_Pro.yaml) as:

* Script: Cyrillic
* Characters and glyphs defined in [GF_Cyrillic_Pro.stub.glyphs](/data/definitions/per_glyphset/GF_Cyrillic_Pro.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Cyrillic_Pro.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Cyrillic_Pro.nam](/data/results/nam/GF_Cyrillic_Pro.nam)

Glyphs.app source file: [GF_Cyrillic_Pro.glyphs](/data/results/glyphs/GF_Cyrillic_Pro.glyphs)

Text files: [GF_Cyrillic_Pro.txt](/data/results/txt/nice-names/GF_Cyrillic_Pro.txt) (nice names) and [GF_Cyrillic_Pro.txt](/data/results/txt/nice-names/GF_Cyrillic_Pro.txt) (production name)

Glyphs.app Custom Filter List (contains all Cyrillic glyphsets): [CustomFilter_GF_Cyrillic.plist](/data/results/plist/CustomFilter_GF_Cyrillic.plist)


# GF Greek AncientMusicalSymbols

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> **Scholarly Use:** Greek and Byzantine Musical Symbols
> 
> * Greek Vocal Notation Symbols
> * Greek Instrumental Notation Symbols
> * Byzantine Musical Symbols

`GF_Greek_AncientMusicalSymbols` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Greek_AncientMusicalSymbols.yaml) as:

* Script: Greek
* Characters and glyphs defined in [GF_Greek_AncientMusicalSymbols.stub.glyphs](/data/definitions/per_glyphset/GF_Greek_AncientMusicalSymbols.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Greek_AncientMusicalSymbols.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Greek_AncientMusicalSymbols.nam](/data/results/nam/GF_Greek_AncientMusicalSymbols.nam)

Glyphs.app source file: [GF_Greek_AncientMusicalSymbols.glyphs](/data/results/glyphs/GF_Greek_AncientMusicalSymbols.glyphs)

Text files: [GF_Greek_AncientMusicalSymbols.txt](/data/results/txt/nice-names/GF_Greek_AncientMusicalSymbols.txt) (nice names) and [GF_Greek_AncientMusicalSymbols.txt](/data/results/txt/nice-names/GF_Greek_AncientMusicalSymbols.txt) (production name)

Glyphs.app Custom Filter List (contains all Greek glyphsets): [CustomFilter_GF_Greek.plist](/data/results/plist/CustomFilter_GF_Greek.plist)


# GF Greek Archaic

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> **Scholarly Use:** Variable Letterforms for Ancient Texts, Papyri
> 
>  * Archaic UC `ϘϚϜϞϠϺ`
> * Archaic LC `ϙϛϝϟϡϻ`
> * Variant Letterforms `κρςΣ`, `Θϐϑϒϓϔϕϖε϶`
>  * Additional Letter `ϳ`
> * Additional Archaic Letters for Bactrian `Ϸϸ`
> * Symbols `ϼ ☧`
> * Editorial Symbols `ϽϾϿ`
> * Ancient Greek Mathematical Character `⟀ ⟁`
>  * Ancient Greek Acrophonic Numerals `𐅀𐅁𐅂𐅃𐅆𐅇𐅈𐅉𐅊𐅋𐅌𐅍𐅎𐅏𐅐𐅑𐅒𐅓𐅔𐅕𐅖𐅗𐅘𐅙𐅚𐅛𐅜𐅝𐅞𐅟𐅠𐅡𐅢𐅣𐅤𐅥𐅦𐅧𐅨𐅩𐅪𐅫𐅬𐅭𐅮𐅯𐅰𐅱𐅲𐅳𐅴`
>  * Geometric shape `□`
> * Astrological symbols `★☉☊☋☌☍☽☾☿♀♁♂♃♄♅♆♇♈♉♊♋♌♍♎♏♐♑♒♓`

`GF_Greek_Archaic` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Greek_Archaic.yaml) as:

* Script: Greek
* Characters and glyphs defined in [GF_Greek_Archaic.stub.glyphs](/data/definitions/per_glyphset/GF_Greek_Archaic.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Greek_Archaic.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Greek_Archaic.nam](/data/results/nam/GF_Greek_Archaic.nam)

Glyphs.app source file: [GF_Greek_Archaic.glyphs](/data/results/glyphs/GF_Greek_Archaic.glyphs)

Text files: [GF_Greek_Archaic.txt](/data/results/txt/nice-names/GF_Greek_Archaic.txt) (nice names) and [GF_Greek_Archaic.txt](/data/results/txt/nice-names/GF_Greek_Archaic.txt) (production name)

Glyphs.app Custom Filter List (contains all Greek glyphsets): [CustomFilter_GF_Greek.plist](/data/results/plist/CustomFilter_GF_Greek.plist)


# GF Greek Coptic

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> **Scholarly Use:** Liturgical language for Coptic Church
> 
> Coptic `U+03E2` – `U+03EF`, Coptic Unicode block `U+2C80` – `U+2CFF`
> 
> * Coptic Letters `ϢϣϤϥϦϧϨϩϪϫϬϭϮϯ`
>  * Bohairic Coptic UC ` ⲀⲂⲄⲆⲈⲊⲌⲎⲐⲒⲔⲖⲘⲚⲜⲞⲠⲢⲤⲦⲨⲪⲬⲮⲰ`
> * Bohairic Coptic LC ` ⲁⲃⲅⲇⲉⲋⲍⲏⲑⲓⲕⲗⲙⲛⲝⲟⲡⲣⲥⲧⲩⲫⲭⲯⲱ `
> * Old Coptic and Dialect Letters UC` ⲲⲴⲶⲸⲺⲼⲾⳀⳂⳄⳆⳈⳊⳌⳎⳐⳒⳔⳖⳘⳚ`
> * Old Coptic and Dialect Letters LC ` ⲳⲵⲷⲹⲻⲽⲿⳁⳃⳅⳇⳉⳋⳍⳏⳑⳓⳕⳗⳙⳛ `
> * Old Nubian Letters ` ⳜⳞⳠⳢⳝⳟⳡⳣ `
>  * Symbols ` ⳤ⳥⳦⳧⳨⳩⳪ `
> * Cryptogrammic Letters ` ⳫⳬⳭⳮ⳯⳰⳱ `
> * Combining Marks ` ⳯⳰⳱ ` 
> * Bohairic Coptic Letters ` Ⳳⳳ `
> * Old Nubian Punctuation ` ⳹⳺⳻⳼ `
> * Coptic Fraction ` ⳽ ` 
> * Punctuation ` ⳾ ⳿ ` 

`GF_Greek_Coptic` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Greek_Coptic.yaml) as:

* Script: Greek
* Characters and glyphs defined in [GF_Greek_Coptic.stub.glyphs](/data/definitions/per_glyphset/GF_Greek_Coptic.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Greek_Coptic.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Greek_Coptic.nam](/data/results/nam/GF_Greek_Coptic.nam)

Glyphs.app source file: [GF_Greek_Coptic.glyphs](/data/results/glyphs/GF_Greek_Coptic.glyphs)

Text files: [GF_Greek_Coptic.txt](/data/results/txt/nice-names/GF_Greek_Coptic.txt) (nice names) and [GF_Greek_Coptic.txt](/data/results/txt/nice-names/GF_Greek_Coptic.txt) (production name)

Glyphs.app Custom Filter List (contains all Greek glyphsets): [CustomFilter_GF_Greek.plist](/data/results/plist/CustomFilter_GF_Greek.plist)


# GF Greek Core

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> **General Use:** Basic Monotonic set for everyday Modern Greek
> 
> * Basic Greek UC ` ΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫ `
> * Basic Greek LC ` άέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώ `
> * Punctuation ` · ; `
> * Greek numeral signs or keraia ` ʹ ͵ `
> * Accents `  ́ ΅ `
> * Kai symbol ` ϗ Ϗ `

`GF_Greek_Core` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Greek_Core.yaml) as:

* Script: Greek
* Characters and glyphs defined in [GF_Greek_Core.stub.glyphs](/data/definitions/per_glyphset/GF_Greek_Core.stub.glyphs)
* List of languages: `
Greek (el_Grek)
`

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Greek_Core.nam](/data/results/nam/GF_Greek_Core.nam)

Glyphs.app source file: [GF_Greek_Core.glyphs](/data/results/glyphs/GF_Greek_Core.glyphs)

Text files: [GF_Greek_Core.txt](/data/results/txt/nice-names/GF_Greek_Core.txt) (nice names) and [GF_Greek_Core.txt](/data/results/txt/nice-names/GF_Greek_Core.txt) (production name)

Glyphs.app Custom Filter List (contains all Greek glyphsets): [CustomFilter_GF_Greek.plist](/data/results/plist/CustomFilter_GF_Greek.plist)


# GF Greek Expert

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> **General Use:** Small Caps for Core and Plus sets, Superscript Letters
>  
> * Core .sc `άέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώ`
> * Plus .sc `ἀἁἂἃἄἅἆἇἐἑἒἓἔἕἠἡἢἣἤἥἦἧἰἱἲἳἴἵἶἷὀὁὂὃὄὅὐὑὒὓὔὕὖὗὠὡὢὣὤὥὦὧὰάὲέὴήὶίὸόὺύὼώᾀᾁᾂᾃᾄᾅᾆᾇᾐᾑᾒᾓᾔᾕᾖᾗᾠᾡᾢᾣᾤᾥᾦᾧᾰᾱᾲᾳᾴᾶᾷιῂῃῄῆῇῐῑῒΐῖῗῠῡῢΰῤῥῦῧῲῳῴῶῷ Ϗ`
> * Archaic Numerals .sc `ϛ ϟ ϡ ϝ`
> * Iota Adscript as ss01 .sc `ᾈᾉᾊᾋᾌᾍᾎᾏᾘᾙᾚᾛᾜᾝᾞᾟᾨᾩᾪᾫᾬᾭᾮᾯᾼῌῼ`
>  * Superior Letters .sups `ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρςστυφχψω`
> * Ligatures `λλ γγ`

`GF_Greek_Expert` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Greek_Expert.yaml) as:

* Script: Greek
* Characters and glyphs defined in [GF_Greek_Expert.stub.glyphs](/data/definitions/per_glyphset/GF_Greek_Expert.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Greek_Expert.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Greek_Expert.nam](/data/results/nam/GF_Greek_Expert.nam)

Glyphs.app source file: [GF_Greek_Expert.glyphs](/data/results/glyphs/GF_Greek_Expert.glyphs)

Text files: [GF_Greek_Expert.txt](/data/results/txt/nice-names/GF_Greek_Expert.txt) (nice names) and [GF_Greek_Expert.txt](/data/results/txt/nice-names/GF_Greek_Expert.txt) (production name)

Glyphs.app Custom Filter List (contains all Greek glyphsets): [CustomFilter_GF_Greek.plist](/data/results/plist/CustomFilter_GF_Greek.plist)


# GF Greek Plus

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> **General Use:** Basic Polytonic set for Scholarly Greek
> 
> * Polytonic UC `ἈἉἊἋἌἍἎἏἘἙἚἛἜἝἨἩἪἫἬἭἮἯἸἹἺἻἼἽἾἿὈὉὊὋὌὍὙὛὝὟὨὩὪὫὬὭὮὯᾈᾉᾊᾋᾌᾍᾎᾏᾘᾙᾚᾛᾜᾝᾞᾟᾨᾩᾪᾫᾬᾭᾮᾯᾸᾹᾺΆᾼῈΈῊΉῌῘῙῚΊῨῩῪΎῬῸΌῺΏῼ `
> * Polytonic LC ` ἀἁἂἃἄἅἆἇἐἑἒἓἔἕἠἡἢἣἤἥἦἧἰἱἲἳἴἵἶἷὀὁὂὃὄὅὐὑὒὓὔὕὖὗὠὡὢὣὤὥὦὧὰάὲέὴήὶίὸόὺύὼώᾀᾁᾂᾃᾄᾅᾆᾇᾐᾑᾒᾓᾔᾕᾖᾗᾠᾡᾢᾣᾤᾥᾦᾧᾰᾱᾲᾳᾴᾶᾷιῂῃῄῆῇῐῑῒΐῖῗῠῡῢΰῤῥῦῧῲῳῴῶῷ `
> * Accents ```   ́ ` ῀ `  ```
> * Breathings ` ῾ ᾿ `
> * Combinations ` ῁ ῍ ῎ ῏ ῝ ῞ ῟  ̈́ `
> * Diactritics `  ͅ ι `
> * Punctuation ` ᾽ `
> * Combining Marks `  ̓ ΅  ͂ ͅ `
> * Iota Adscript as ss01 `ᾈᾉᾊᾋᾌᾍᾎᾏᾘᾙᾚᾛᾜᾝᾞᾟᾨᾩᾪᾫᾬᾭᾮᾯᾼῌῼ`

`GF_Greek_Plus` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Greek_Plus.yaml) as:

* Script: Greek
* Characters and glyphs defined in [GF_Greek_Plus.stub.glyphs](/data/definitions/per_glyphset/GF_Greek_Plus.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Greek_Plus.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Greek_Plus.nam](/data/results/nam/GF_Greek_Plus.nam)

Glyphs.app source file: [GF_Greek_Plus.glyphs](/data/results/glyphs/GF_Greek_Plus.glyphs)

Text files: [GF_Greek_Plus.txt](/data/results/txt/nice-names/GF_Greek_Plus.txt) (nice names) and [GF_Greek_Plus.txt](/data/results/txt/nice-names/GF_Greek_Plus.txt) (production name)

Glyphs.app Custom Filter List (contains all Greek glyphsets): [CustomFilter_GF_Greek.plist](/data/results/plist/CustomFilter_GF_Greek.plist)


# GF Greek Pro

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> **Scholarly Use:** Extended Polytonic Greek, for scholarly edition of ancient texts (Ancient and Roman Greece studies, Byzantine studies, Greek Biblical studies)
> 
> **[Learn how to draw good Polytonic Greek at irenevl.github.io/Polytonic-tutorial](https://irenevl.github.io/Polytonic-tutorial/)**
>  
> **N.B.** List of characters from GF Latin Plus and Pro sets that are prerequisites to this set.
> 
> № | char | nice name (Glyphs App) | uni name | set
> ---|---|---|---|---
>  1|²|twosuperior|uni00B2|GF Latin Plus
> 2|³|threesuperior|uni00B3|GF Latin Plus
>  3|¹|onesuperior|uni00B9|GF Latin Plus
> 4|⁰|zerosuperior|uni0270|GF Latin Pro
> 5|†|dagger|uni2020|GF Latin Plus
> 6|‡|daggerdbl|uni2021|GF Latin Plus
> 7|⁴|foursuperior|uni2074|GF Latin Plus
> 8|⁵|fivesuperior|uni2075|GF Latin Pro
> 9|⁶|sixsuperior|uni2076|GF Latin Pro
>  10|⁷|sevensuperior|uni2077|GF Latin Pro
> 11|⁸|eightsuperior|uni2078|GF Latin Pro
>  12|⁹|ninesuperior|uni2079|GF Latin Pro
> 13|₀|zeroinferior|uni2080|GF Latin Pro
>  14|₁|oneinferior|uni2081|GF Latin Pro
> 15|₂|twoinferior|uni2082|GF Latin Pro
> 16|₃|threeinferior|uni2083|GF Latin Pro
> 17|₄|fourinferior|uni2084|GF Latin Pro
> 18|₅|fiveinferior|uni2085|GF Latin Pro
> 19|₆|sixinferior|uni2086|GF Latin Pro
> 20|₇|seveninferior|uni2087|GF Latin Pro
> 21|₈|eightinferior|uni2088|GF Latin Pro
> 22|₉|nineinferior|uni2089|GF Latin Pro
> 
> 
> * Archaic Letters and Numerals `Ϛ Ϟ Ϡ Ϝ ϛ ϟ ϡ ϝ`
> * Ancient Greek Textual symbols `⸎ ⸏ ⸐ ⸑ ⸒ ⸓ ⸔ ⸕ ⸖ ⸗`
> * Archaic Punctuation `※ ⁂ ‿ ͜ ˙ ⁖ ⁘ ⁙ ⁚ ⁛ ⁜ ⁝ ⁞ ⊗ ⋮`
> * Greek Metrical Symbols `⏑ ⏒ ⏓ ⏔ ⏕ ⏖ ⏗ ⏘ ⏙`
> * Critical Sigla `̅ ̣ ͙ ‖ ⁺ ⁻ ⁼ ₊ ₋ ₌ ⫽ ⸀ ⸁ ⸂ ⸃ ⸄ ⸅ ⸆ ⸇ ⸈ ⸉ ⸊ ⸋ ⸌ ⸍ 〈 〉《 》「 」〚 〛`
> * Biblical Apparatus `ℵ ℶ 𝑙 𝔖 𝔐 𝔓 𝔭`
> 
> 
> **N.B.** For certain design cases it is best practice to include inital and final variants of ` ̅` overlinecomb (uni0305):
> 
> * `overlinecomb.init`, cropped on the left
> * `overlinecomb.fina`, cropped on the right

`GF_Greek_Pro` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Greek_Pro.yaml) as:

* Script: Greek
* Characters and glyphs defined in [GF_Greek_Pro.stub.glyphs](/data/definitions/per_glyphset/GF_Greek_Pro.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Greek_Pro.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Greek_Pro.nam](/data/results/nam/GF_Greek_Pro.nam)

Glyphs.app source file: [GF_Greek_Pro.glyphs](/data/results/glyphs/GF_Greek_Pro.glyphs)

Text files: [GF_Greek_Pro.txt](/data/results/txt/nice-names/GF_Greek_Pro.txt) (nice names) and [GF_Greek_Pro.txt](/data/results/txt/nice-names/GF_Greek_Pro.txt) (production name)

Glyphs.app Custom Filter List (contains all Greek glyphsets): [CustomFilter_GF_Greek.plist](/data/results/plist/CustomFilter_GF_Greek.plist)


# GF Latin African

`GF_Latin_African` is **dynamically** defined [here](/Lib/glyphsets/definitions/GF_Latin_African.yaml) as:

* Script: Latin
* All languages of the countries `
Algeria (DZ),
Angola (AO),
Benin (BJ),
Botswana (BW),
British Indian Ocean Territory (IO),
Burkina Faso (BF),
Burundi (BI),
Cameroon (CM),
Canary Islands (IC),
Cape Verde (CV),
Central African Republic (CF),
Ceuta & Melilla (EA),
Chad (TD),
Comoros (KM),
Congo - Brazzaville (CG),
Congo - Kinshasa (CD),
Côte d’Ivoire (CI),
Djibouti (DJ),
Egypt (EG),
Equatorial Guinea (GQ),
Eritrea (ER),
Eswatini (SZ),
Ethiopia (ET),
French Southern Territories (TF),
Gabon (GA),
Gambia (GM),
Ghana (GH),
Guinea (GN),
Guinea-Bissau (GW),
Kenya (KE),
Lesotho (LS),
Liberia (LR),
Libya (LY),
Madagascar (MG),
Malawi (MW),
Mali (ML),
Mauritania (MR),
Mauritius (MU),
Mayotte (YT),
Morocco (MA),
Mozambique (MZ),
Namibia (NA),
Niger (NE),
Nigeria (NG),
Rwanda (RW),
Réunion (RE),
Senegal (SN),
Seychelles (SC),
Sierra Leone (SL),
Somalia (SO),
South Africa (ZA),
South Sudan (SS),
St. Helena (SH),
Sudan (SD),
São Tomé & Príncipe (ST),
Tanzania (TZ),
Togo (TG),
Tunisia (TN),
Uganda (UG),
Western Sahara (EH),
Zambia (ZM),
Zimbabwe (ZW)
`
* With a population of over 1 speakers
* Including auxiliary characters
* Excluding the following languages: `
English (en_Latn),
French (fr_Latn),
German (de_Latn),
Portuguese (pt_Latn),
Spanish (es_Latn)
`


The following list of **598** languages is computed as a result of the dynamic conditions described above:

`
Abidji (abi_Latn),
Abron (abr_Latn),
Abua (abn_Latn),
Acoli (ach_Latn),
Adangme (ada_Latn),
Adara (kad_Latn),
Adele (ade_Latn),
Adioukrou (adj_Latn),
Afar (aa_Latn),
Afrikaans (af_Latn),
Agatu (agc_Latn),
Aghem (agq_Latn),
Agwagwune (yay_Latn),
Ahanta (aha_Latn),
Aja (ajg_Latn),
Akebu (keu_Latn),
Akoose (bss_Latn),
Akuapem Twi (tw_akuapem_Latn),
Alago (ala_Latn),
Amo (amo_Latn),
Anaang (anw_Latn),
Anii (blo_Latn),
Anufo (cko_Latn),
Anyin (any_Latn),
Arabic, Chadian Spoken (shu_Latn),
Ashe (ahs_Latn),
Asu (asa_Latn),
Atsam (cch_Latn),
Avatime (avn_Latn),
Avokaya (avu_Latn),
Awak (awo_Latn),
Awing (azo_Latn),
Ayizo Gbe (ayb_Latn),
Baatonum (bba_Latn),
Bacama (bcy_Latn),
Bafia (ksf_Latn),
Bafut (bfd_Latn),
Baga Sitemu (bsp_Latn),
Baka (bdh_Latn),
Baka (beh_Latn),
Baka (bkc_Latn),
Balanta-Ganja (bjt_Latn),
Bali (bcn_Latn),
Bambara (bm_Latn),
Bamun, Latin (bax_Latn),
Bana (bcw_Latn),
Banda, West Central (bbp_Latn),
Bandi (bza_Latn),
Bandial (bqj_Latn),
Bangwinji (bsj_Latn),
Baoulé (bci_Latn),
Bapuku (bnm_Latn),
Bari (bfa_Latn),
Basa (bzw_Latn),
Basaa (bas_Latn),
Bassa (bsq_Latn),
Bassari (bsc_Latn),
Bassari (bsc_Latn_GN),
Bedawiyet (bej_Latn),
Bedjond (bjv_Latn),
Bekwarra (bkv_Latn),
Belanda Viri, Latin (bvi_Latn),
Bemba (bem_Latn),
Bena (bez_Latn),
Bench (bcq_Latn),
Beng (nhb_Latn),
Benga (bng_Latn),
Berom (bom_Latn),
Bete-Bendi (btt_Latn),
Bhele (bhy_Latn),
Bilen (byn_Latn),
Bimoba (bim_Latn),
Bini (bin_Latn),
Birifor, Southern (biv_Latn),
Bissa (bib_Latn),
Bisã (bqp_Latn),
Boko (bqc_Latn),
Bokobaru (bus_Latn),
Bomu (bmq_Latn),
Bondoukou Kulango (kzc_Latn),
Bozo, Hainyaxo (bzx_Latn),
Buamu (box_Latn),
Bube (bvb_Latn),
Budu (buu_Latn),
Bulu (bum_Latn),
Bura-Pabir (bwr_Latn),
Burak (bys_Latn),
Bushi (buc_Latn),
Bété, Daloa (bev_Latn),
Bété, Guiberoua (bet_Latn),
Cahungwarya (nat_Latn),
Cakfem-Mushere (cky_Latn),
Cebaara Senoufo (sef_Latn),
Central Atlas Tamazight (tzm_Latn),
Central-Eastern Niger Fulfulde (fuq_Latn),
Cerma (cme_Latn),
Chiduruma (dug_Latn),
Chiga (cgg_Latn),
Chokwe (cjk_Latn),
Chumburung (ncu_Latn),
Cicipu (awc_Latn),
Cishingini (asg_Latn),
Comorian, Ngazidja (zdj_Latn),
Crioulo, Upper Guinea (pov_Latn),
C’Lela (dri_Latn),
Daba (dbq_Latn),
Dadiya (dbd_Latn),
Dagaare, Southern (dga_Latn),
Dagbani (dag_Latn),
Dan (dnj_Latn),
Dan (dnj_Latn_LR),
Dangaléat (daa_Latn),
Dawro (dwr_Latn),
Dazaga (dzg_Latn),
Deg (mzw_Latn),
Delo (ntr_Latn),
Dendi (ddn_Latn),
Denya (anv_Latn),
Dghwede (dgh_Latn),
Dida, Yocoboué (gud_Latn),
Didinga (did_Latn),
Dii (dur_Latn),
Dikaka (cfa_Latn),
Dinka (din_Latn),
Dinka, Northeastern (dip_Latn),
Ditammari (tbz_Latn),
Dogon, Toro So (dts_Latn),
Doyayo (dow_Latn),
Duala (dua_Latn),
Duya (ldb_Latn),
Dyan (dya_Latn),
Dyula (dyu_Latn),
Dza (jen_Latn),
Eastern Gurung, Latin (ggn_Latn),
Ebira (igb_Latn),
Ede Cabe (cbj_Latn),
Ede Ica (ica_Latn),
Ede Idaca (idd_Latn),
Ede Ije (ijj_Latn),
Efik (efi_Latn),
Ejagham (etu_Latn),
Ekajuk (eka_Latn),
Ekpeye (ekp_Latn),
Elip (ekm_Latn),
Emai-Iuleha-Ora (ema_Latn),
Embu (ebu_Latn),
Engenni (enn_Latn),
Esan (ish_Latn),
Etkywan (ich_Latn),
Etulo (utr_Latn),
Ewe (ee_Latn),
Ewondo (ewo_Latn),
Ezaa (eza_Latn),
Fang (fan_Latn),
Fanti (fat_Latn),
Fe’fe’ (fmp_Latn),
Fon (fon_Latn),
Foodo (fod_Latn),
Frafra (gur_Latn),
Fulah (ff_Latn),
Fulfulde, Adamawa (fub_Latn),
Fulfulde, Borgu (fue_Latn),
Fulfulde, Western Niger (fuh_Latn),
Fuliiru (flr_Latn),
Fur (fvr_Latn),
Ga (gaa_Latn),
Gamo (gmv_Latn),
Ganda (lg_Latn),
Gbari (gby_Latn),
Gbaya (Sudan) (krs_Latn),
Gbaya-Mbodomo (gmm_Latn),
Gbe, Tofin (tfi_Latn),
Gbe, Waci (wci_Latn),
Gbe, Xwela (xwe_Latn),
Gen (gej_Latn),
Ghomala (bbj_Latn),
Gikyode (acd_Latn),
Godié (god_Latn),
Goemai (ank_Latn),
Gofa (gof_Latn),
Gokana (gkn_Latn),
Gonja (gjn_Latn),
Goo (gov_Latn),
Gor (gqr_Latn),
Gourmanchéma (gux_Latn),
Grebo (grb_Latn),
Gude (gde_Latn),
Gulay (gvl_Latn),
Gumuz (guk_Latn),
Gun (guw_Latn),
Gungu (rub_Latn),
Guro (goa_Latn),
Gusii (guz_Latn),
Gwak (jgk_Latn),
Gyele (gyi_Latn),
Hanga (hag_Latn),
Harari (har_Latn),
Hassaniyya (mey_Latn),
Hausa (ha_Latn),
Hdi (xed_Latn),
Herero (hz_Latn),
Hyam (jab_Latn),
Ibani (iby_Latn),
Ibibio (ibb_Latn),
Idoma (idu_Latn),
Ifè (ife_Latn),
Igbo (ig_Latn),
Igede (ige_Latn),
Igo (ahl_Latn),
Ijo, Southeast (ijs_Latn),
Ik (ikx_Latn),
Ika (ikk_Latn),
Ikposo (kpo_Latn),
Ikwere (ikw_Latn),
Ikwo (iqw_Latn),
Iten (etx_Latn),
Ivbie North-Okpela-Arhe (atg_Latn),
Izere (izr_Latn),
Izii (izz_Latn),
Jenaama Bozo (bze_Latn),
Jibu (jib_Latn),
Jju (kaj_Latn),
Jola-Fonyi (dyo_Latn),
Jola-Kasa (csk_Latn),
Jukun Takum (jbu_Latn),
Jur Modo (bex_Latn),
Juǀʼhoan (ktz_Latn),
Kaansa (gna_Latn),
Kabalai (kvf_Latn),
Kabba (ksp_Latn),
Kabiyé (kbp_Latn),
Kabuverdianu (kea_Latn),
Kabyle (kab_Latn),
Kako (kkj_Latn),
Kalanga (kck_Latn),
Kalenjin (kln_Latn),
Kamba (kam_Latn),
Kamuku (cdr_Latn),
Kamwe (hig_Latn),
Kanuri (kr_Latn),
Kanuri, Central (knc_Latn),
Kanuri, Manga (kby_Latn),
Kaonde (kqn_Latn),
Karaboro, Eastern (xrb_Latn),
Karang (kzr_Latn),
Karekare (kai_Latn),
Kasem (xsm_Latn),
Kasem (xsm_Latn_BF),
Kenga (kyq_Latn),
Kenyang (ken_Latn),
Kibaku (ckl_Latn),
Kikuyu (ki_Latn),
Kim (kia_Latn),
Kimbundu (kmb_Latn),
Kimré (kqp_Latn),
Kinyarwanda (rw_Latn),
Kirike (okr_Latn),
Kissi, Northern (kqs_Latn),
Kita Maninkakan (mwk_Latn),
Kituba (ktu_Latn),
Koalib (kib_Latn),
Kom (bkm_Latn),
Koma (kmy_Latn),
Kombe (nui_Latn),
Kongo (kg_Latn),
Konjo (koo_Latn),
Konkomba (xon_Latn),
Koonzime (ozm_Latn),
Koro (kfo_Latn),
Koro Wachi (bqv_Latn),
Kouya (kyf_Latn),
Koyra Chiini (khq_Latn),
Koyraboro Senni (ses_Latn),
Kpelle (kpe_Latn),
Kpelle, Guinea (gkp_Latn),
Krache (kye_Latn),
Krio (kri_Latn),
Krumen, Plapo (ktj_Latn),
Krumen, Tepo (ted_Latn),
Kuanyama (kj_Latn),
Kukele (kez_Latn),
Kulango, Bouna (nku_Latn),
Kunama (kun_Latn),
Kuo (xuo_Latn),
Kuria (kuj_Latn),
Kusaal (kus_Latn),
Kutep (kub_Latn),
Kutu (kdc_Latn),
Kwanja (knp_Latn),
Kwasio (nmg_Latn),
Kwere (cwe_Latn),
Lama (Togo) (las_Latn),
Lamang (hia_Latn),
Lamba (lam_Latn),
Lamnso’ (lns_Latn),
Langi (lag_Latn),
Lango [Uganda] (laj_Latn),
Lehar (cae_Latn),
Lele (lln_Latn),
Lendu (led_Latn),
Lese (les_Latn),
Ligbi (lig_Latn),
Limba, West-Central (lia_Latn),
Limbum (lmp_Latn),
Lingala (ln_Latn),
Lobala (loq_Latn),
Lobi (lob_Latn),
Logo (log_Latn),
Lokaa (yaz_Latn),
Loko (lok_Latn),
Lomwe (ngl_Latn),
Longuda (lnu_Latn),
Lozi (loz_Latn),
Luba-Katanga (lu_Latn),
Luba-Lulua (lua_Latn),
Lugbara (lgg_Latn),
Luguru (ruf_Latn),
Lukpa (dop_Latn),
Lunda (lun_Latn),
Luo (luo_Latn),
Luvale (lue_Latn),
Luwo (lwo_Latn),
Luyia (luy_Latn),
Lyélé (lee_Latn),
Láá Láá Bwamu (bwj_Latn),
Maasina Fulfulde (ffm_Latn),
Machame (jmc_Latn),
Mada (mda_Latn),
Mafa (maf_Latn),
Makaa (mcp_Latn),
Makhuwa (vmw_Latn),
Makhuwa-Meetto (mgh_Latn),
Makonde (kde_Latn),
Malagasy (mg_Latn),
Malba Birifor (bfo_Latn),
Mamara Senoufo (myk_Latn),
Mambila, Cameroon (mcu_Latn),
Mambila, Nigeria (mzk_Latn),
Mampruli (maw_Latn),
Mandingo (man_Latn),
Mandinka (mnk_Latn),
Mandjak (mfv_Latn),
Mangbetu (mdj_Latn),
Mango (mge_Latn),
Maninka, Sankaran (msc_Latn),
Maninkakan, Eastern (emk_Latn),
Mankanya (knf_Latn),
Mano (mev_Latn),
Manyika (mxc_Latn),
Maore Comorian, Latin (swb_Latn),
Masaaba (myx_Latn),
Masai (mas_Latn),
Masalit (mls_Latn),
Masana (mcn_Latn),
Ma’di (mhi_Latn),
Mbe (mfo_Latn),
Mbelime (mql_Latn),
Mbembe, Cross River (mfn_Latn),
Mbere (mdt_Latn),
Mbo (mbo_Latn),
Mbuko (mqb_Latn),
Mbula-Bwazza (mbu_Latn),
Mbunga (mgy_Latn),
Medumba (byv_Latn),
Mendankwe-Nkwen (mfd_Latn),
Mende (men_Latn),
Merey (meq_Latn),
Meru (mer_Latn),
Metaʼ (mgo_Latn),
Me’en (mym_Latn),
Mfumte (nfu_Latn),
Mina (hna_Latn),
Miyobe (soy_Latn),
Mmaala (mmu_Latn),
Moba (mfq_Latn),
Mokole (mkl_Latn),
Mongo (lol_Latn),
Morisyen (mfe_Latn),
Moro (mor_Latn),
Morokodo (mgc_Latn),
Mossi (mos_Latn),
Mumuye (mzm_Latn),
Mundang (mua_Latn),
Mundani (mnf_Latn),
Murle (mur_Latn),
Muyang (muy_Latn),
Mwaghavul (sur_Latn),
Mwan (moa_Latn),
Mwani (wmw_Latn),
Ménik (tnr_Latn),
Mündü (muh_Latn),
Nafaanra (nfr_Latn),
Nama (naq_Latn),
Nara (nrb_Latn),
Nateni (ntm_Latn),
Nawdm (nmz_Latn),
Nawuri (naw_Latn),
Ndamba (ndj_Latn),
Ndau (ndc_Latn),
Ndogo (ndz_Latn),
Ndonga (ng_Latn),
Ndrulo (dno_Latn),
Ndut (ndv_Latn),
Ngambay (sba_Latn),
Ngangam (gng_Latn),
Ngas (anc_Latn),
Ngbaka (nga_Latn),
Ngbandi, Northern (ngb_Latn),
Ngiemboon (nnh_Latn),
Ngindo (nnq_Latn),
Ngiti (niy_Latn),
Ngomba (jgo_Latn),
Ngulu (ngp_Latn),
Nigerian Fulfulde (fuv_Latn),
Nigerian Pidgin (pcm_Latn),
Ninzo (nin_Latn),
Nkonya (nko_Latn),
Nomaande (lem_Latn),
Noon (snf_Latn),
Noone (nhu_Latn),
North Ndebele (nd_Latn),
Northern Bobo Madaré (bbo_Latn),
Northern Dagara (dgi_Latn),
Northern Sotho (nso_Latn),
Ntcham (bud_Latn),
Nuer (nus_Latn),
Nugunu (yas_Latn),
Nuni, Northern (nuv_Latn),
Nupe-Nupe-Tako (nup_Latn),
Nyabwa (nwb_Latn),
Nyamwezi (nym_Latn),
Nyangbo (nyb_Latn),
Nyanja (ny_Latn),
Nyankole (nyn_Latn),
Nyasa Tonga (tog_Latn),
Nyemba (nba_Latn),
Nyoro (nyo_Latn),
Nzakara (nzk_Latn),
Nzima (nzi_Latn),
Nǁng (ngh_Latn),
Obolo (ann_Latn),
Ogbah (ogc_Latn),
Okiek (oki_Latn),
Oromo (om_Latn),
Otuho (lot_Latn),
Paasaal (sig_Latn),
Pana (Central African Republic) (pnz_Latn),
Pangu (png_Latn),
Parkwa (pbi_Latn),
Pero (pip_Latn),
Phuie (pug_Latn),
Pogolo (poy_Latn),
Pokomo (pkb_Latn),
Pulaar (fuc_Latn),
Pular (fuf_Latn),
Punu (puu_Latn),
Pyam (pym_Latn),
Pökoot (pko_Latn),
Rendille (rel_Latn),
Reshe (res_Latn),
Riffian (Latin) (rif_Latn),
Rigwe (iri_Latn),
Rombo (rof_Latn),
Ron (cla_Latn),
Ronga (rng_Latn),
Rundi (rn_Latn),
Rwa (rwk_Latn),
Réunion Creole French (rcf_Latn),
Saafi-Saafi (sav_Latn),
Safaliba (saf_Latn),
Saho (ssy_Latn),
Samburu (saq_Latn),
Sandawe (sad_Latn),
Sango (sg_Latn),
Sangu (sbp_Latn),
Sar (mwm_Latn),
Saxwe Gbe (sxw_Latn),
Seki (syi_Latn),
Sekpele (lip_Latn),
Selee (snw_Latn),
Sena (seh_Latn),
Serer (srr_Latn),
Seselwa Creole French (crs_Latn),
Shambala (ksb_Latn),
Sheko (she_Latn),
Shilluk (shk_Latn),
Shona (sn_Latn),
Sidamo (sid_Latn),
Sisaala, Tumulung (sil_Latn),
Sissala (sld_Latn),
Siwu (akp_Latn),
Soga (xog_Latn),
Sokoro (sok_Latn),
Somali (so_Latn),
Soninke (snk_Latn),
South Central Banda (lnl_Latn),
South Ndebele (nr_Latn),
Southern Bobo Madaré (bwq_Latn),
Southern Kisi (kss_Latn),
Southern Nuni (nnw_Latn),
Southern Samo (sbd_Latn),
Southern Sotho (st_Latn),
Suba (sxb_Latn),
Sudanese Arabic (apd_Latn),
Sukuma (suk_Latn),
Suri, Tirmaga-Chai (suq_Latn),
Susu (sus_Latn),
Swahili (sw_Latn),
Swahili, Congo (swc_Latn),
Swati (ss_Latn),
Syenara Senoufo (shz_Latn),
Sãotomense (cri_Latn),
Sénoufo, Djimini (dyi_Latn),
Sénoufo, Supyire (spp_Latn),
Tachelhit (Latin) (shi_Latn),
Tafi (tcd_Latn),
Taita (dav_Latn),
Takwane (tke_Latn),
Tal (tal_Latn),
Talinga-Bwisi (tlj_Latn),
Tamashek (tmh_Latn),
Tamasheq, Latin (taq_Latn),
Tampulma (tpm_Latn),
Tangale (tan_Latn),
Tarok (yer_Latn),
Tasawaq (twq_Latn),
Tawallammat Tamajaq (ttq_Latn),
Tedaga (tuq_Latn),
Tem (kdh_Latn),
Tera (ttr_Latn),
Teso (teo_Latn),
Tigon Mbembe (nza_Latn),
Tikar (tik_Latn),
Timne (tem_Latn),
Tiv (tiv_Latn),
Tiéyaxo Bozo (boz_Latn),
Toma (tod_Latn),
Tomo Kan Dogon (dtm_Latn),
Tonga (toi_Latn),
Tooro (ttj_Latn),
Toposa (toq_Latn),
Toura (neb_Latn),
Toussian, Southern (wib_Latn),
Tsikimba (kdl_Latn),
Tsishingini (tsw_Latn),
Tsonga (ts_Latn),
Tsuvadi (tvd_Latn),
Tswana (tn_Latn),
Tula (tul_Latn),
Tumbuka (tum_Latn),
Tunen (tvu_Latn),
Tunisian Darija (aeb_Latn),
Turka (tuz_Latn),
Tuwuli (bov_Latn),
Tyap (kcg_Latn),
Téén (lor_Latn),
Uduk (udu_Latn),
Umbundu (umb_Latn),
Vagla (vag_Latn),
Vai (Latin) (vai_Latn),
Venda (ve_Latn),
Vengo (bav_Latn),
Vidunda (vid_Latn),
Vunjo (vun_Latn),
Vute (vut_Latn),
Waama (wwa_Latn),
Waja (wja_Latn),
Wamey (cou_Latn),
Wan (wan_Latn),
Wandala (mfi_Latn),
Warji (wji_Latn),
Winyé (kst_Latn),
Wolaytta (wal_Latn),
Wolof (wo_Latn),
Wè Northern (wob_Latn),
Xaasongaxango (kao_Latn),
Xhosa (xh_Latn),
Yala (yba_Latn),
Yalunka (yal_Latn),
Yamba (yam_Latn),
Yambeta (yat_Latn),
Yangben (yav_Latn),
Yao (yao_Latn),
Yaouré (yre_Latn),
Yasa (yko_Latn),
Yemba (ybb_Latn),
Yom (pil_Latn),
Yoruba (yo_Latn),
Zaghawa (zag_Latn),
Zande (zne_Latn),
Zarma (dje_Latn),
Zayse (zay_Latn),
Zigula (ziw_Latn),
Zulgo-Gemzek (gnd_Latn),
Zulu (zu_Latn),
gevové (buw_Latn),
ut-Hun (uth_Latn),
ut-Ma’in (gel_Latn)
`

### Decomposed Characters

The following 722 composed character sequences are decomposed in the font:

`
A̋ A̍ A̧ A̰ A̱ A᷄ A᷅ A᷆ A᷇ B̀ B́ B̯ C̱ D̯ E̋ E̍ E̱ E᷄ E᷅ E᷆ E᷇ G̈ H̃ H̱ I̋ I̍ I̧ I̱ I᷄ I᷅ I᷆ I᷇ J̌ L̀ L̄ M̀ Ḿ M̂ M̄ N̂ N̄ N̈ N̰ O̍ O̧ O̰ O̱ O᷄ O᷅ O᷆ O᷇ P̱ R̀ R̂ R̃ R̄ S̀ T̯ T͟H U̍ U̧ U̱ U᷄ U᷅ U᷆ U᷇ V̄ V̱ W̃ W̄ W̤ a̋ a̍ a̧ a̰ a̱ a᷄ a᷅ a᷆ a᷇ b̀ b́ b̯ c̱ d̯ e̋ e̍ e̱ e᷄ e᷅ e᷆ e᷇ g̈ h̃ i̋ i̍ i̧ i̱ i᷄ i᷅ i᷆ i᷇ l̀ l̄ m̀ ḿ m̂ m̄ n̂ n̄ n̈ n̰ o̍ o̧ o̰ o̱ o᷄ o᷅ o᷆ o᷇ p̱ r̀ r̂ r̃ r̄ s̀ t̯ t͟h u̍ u̧ u̱ u᷄ u᷅ u᷆ u᷇ v̄ v̱ w̃ w̄ w̤ À̧ À̰ Á̧ Á̰ Á̱ Â̧ Â̱ Ã̀ Ã́ Ã̂ Ã̄ Ã̌ Ã̍ Ä́ Ä̃ Æ̀ Æ̂ Æ̋ Æ̌ Æ̏ Ë́ Ë̃ Ì̧ Í̧ Í̱ Î̧ Ï̃ Ò̧ Ò̰ Ó̧ Ó̰ Ô̧ Õ̀ Õ̂ Õ̌ Õ̱ Ö́ Ö̃ Ø̀ Ø̂ Ø̃ Ø̃̀ Ø̃́ Ø̃̂ Ø̋ Ø̌ Ù̧ Ú̧ Û̧ Ü̃ à̧ à̰ á̧ á̰ á̱ â̧ â̱ ã̀ ã́ ã̂ ã̄ ã̌ ã̍ ä́ ä̃ æ̀ æ̂ æ̋ æ̌ æ̏ ë́ ë̃ ì̧ í̧ í̱ î̧ ï̃ ò̧ ò̰ ó̧ ó̰ ô̧ õ̀ õ̂ õ̌ õ̱ ö́ ö̃ ø̀ ø̂ ø̃ ø̃̀ ø̃́ ø̃̂ ø̋ ø̌ ù̧ ú̧ û̧ ü̃ Ā̰ ā̰ Ą́ ą́ Ĩ̀ Ĩ́ Ĩ̂ Ĩ̌ Ĩ̍ ĩ̀ ĩ́ ĩ̂ ĩ̌ ĩ̍ Į́ į́ Ŋ̀ Ŋ́ Ŋ̂ Ŋ̄ Ŋ̈ Ŋ̍ ŋ̀ ŋ́ ŋ̂ ŋ̄ ŋ̈ ŋ̍ Ō̰ ō̰ Œ̀ Œ́ Œ̂ Œ̄ Œ̋ Œ̌ Œ̏ œ̀ œ́ œ̂ œ̄ œ̋ œ̌ œ̏ Ũ̀ Ũ̂ Ũ̄ Ũ̌ Ũ̍ Ũ᷆ ũ̀ ũ̂ ũ̄ ũ̌ ũ̍ ũ᷆ Ų́ ų́ Ɔ̀ Ɔ́ Ɔ̂ Ɔ̃ Ɔ̃̀ Ɔ̃́ Ɔ̃̂ Ɔ̃̄ Ɔ̃̌ Ɔ̃̍ Ɔ̄ Ɔ̈ Ɔ̌ Ɔ̍ Ɔ̧ Ɔ̧̀ Ɔ̧́ Ɔ̧̂ Ɔ̧̌ Ɔ̨ Ɔ̨́ Ɔ̰ Ɔ̰̀ Ɔ̰́ Ɔ̰̄ Ɔ̱ Ɔ᷄ Ɔ᷅ Ɔ᷆ Ɔ᷇ Ǝ̀ Ǝ́ Ǝ̂ Ǝ̃ Ǝ̃̀ Ǝ̃́ Ǝ̃̂ Ǝ̄ Ǝ̌ Ǝ̰ Ə̀ Ə́ Ə̂ Ə̄ Ə̈ Ə̌ Ə̧ Ə̧̀ Ə̧́ Ə̨ Ə̨́ Ə̰ Ə̰̀ Ə̰́ Ə̰̄ Ɛ̀ Ɛ́ Ɛ̧́ Ɛ̂ Ɛ̧̂ Ɛ̃ Ɛ̃̀ Ɛ̃́ Ɛ̃̂ Ɛ̃̌ Ɛ̃̍ Ɛ̄ Ɛ̈ Ɛ̋ Ɛ̌ Ɛ̧̌ Ɛ̍ Ɛ̏ Ɛ̧ Ɛ̧́ Ɛ̧̂ Ɛ̨ Ɛ̨́ Ɛ̰ Ɛ̰̀ Ɛ̰́ Ɛ̰̄ Ɛ̱ Ɛ̱̈ Ɛ᷄ Ɛ᷅ Ɛ᷆ Ɛ᷇ Ɩ̀ Ɩ́ Ɩ̂ Ɩ̃ Ɩ̃̀ Ɩ̃́ Ɩ̃̂ Ɩ̃᷆ Ɩ̄ Ɩ̌ Ɩ᷆ Ɨ̀ Ɨ́ Ɨ̂ Ɨ̄ Ɨ̈ Ɨ̌ Ɨ̧ Ɨ̧̀ Ɨ̧̂ Ɨ̧̌ Ɯ̀ Ɯ́ Ɯ̂ Ɯ̄ Ɯ̋ Ɯ̏ Ɵ̀ Ɵ́ Ɵ̂ Ʊ̀ Ʊ́ Ʊ̂ Ʊ̃ Ʊ̃́ Ʊ̄ Ʊ̌ Ʋ̀ Ʋ́ Ʋ̂ Ʋ̃ Ʋ̃̀ Ʋ̃́ Ʋ̈ Ʋ̌ Ǎ̧ Ǎ̱ ǎ̧ ǎ̱ Ǒ̧ ǒ̧ Ǔ̧ ǔ̧ ǝ̀ ǝ́ ǝ̂ ǝ̃ ǝ̃̀ ǝ̃́ ǝ̃̂ ǝ̄ ǝ̌ ǝ̰ Ȩ̀ Ȩ́ Ȩ̂ Ȩ̌ ȩ̀ ȩ́ ȩ̂ ȩ̌ Ʉ̀ Ʉ́ Ʉ̂ Ʉ̄ Ʉ̈ Ʉ̌ Ʌ̀ Ʌ́ Ʌ̂ Ʌ̄ Ʌ̋ Ʌ̏ ɐ̀ ɐ́ ɐ̂ ɑ̀ ɑ́ ɑ̂ ɑ̄ ɑ̌ ɔ̀ ɔ́ ɔ̂ ɔ̃ ɔ̃̀ ɔ̃́ ɔ̃̂ ɔ̃̄ ɔ̃̌ ɔ̃̍ ɔ̄ ɔ̈ ɔ̌ ɔ̍ ɔ̧ ɔ̧̀ ɔ̧́ ɔ̧̂ ɔ̧̌ ɔ̨ ɔ̨́ ɔ̰ ɔ̰̀ ɔ̰́ ɔ̰̄ ɔ̱ ɔ᷄ ɔ᷅ ɔ᷆ ɔ᷇ ə̀ ə́ ə̂ ə̄ ə̈ ə̌ ə̧ ə̧̀ ə̧́ ə̨ ə̨́ ə̰ ə̰̀ ə̰́ ə̰̄ ɛ̀ ɛ́ ɛ̧́ ɛ̂ ɛ̧̂ ɛ̃ ɛ̃̀ ɛ̃́ ɛ̃̂ ɛ̃̌ ɛ̃̍ ɛ̄ ɛ̈ ɛ̋ ɛ̌ ɛ̧̌ ɛ̍ ɛ̏ ɛ̧ ɛ̧́ ɛ̧̂ ɛ̨ ɛ̨́ ɛ̰ ɛ̰̀ ɛ̰́ ɛ̰̄ ɛ̱ ɛ̱̈ ɛ᷄ ɛ᷅ ɛ᷆ ɛ᷇ ɤ̀ ɤ́ ɤ̂ ɤ̄ ɤ̋ ɤ̏ ɥ̀ ɥ́ ɥ̂ ɥ̃̀ ɨ̀ ɨ́ ɨ̂ ɨ̄ ɨ̈ ɨ̌ ɨ̧ ɨ̧̀ ɨ̧̂ ɨ̧̌ ɩ̀ ɩ́ ɩ̂ ɩ̃ ɩ̃̀ ɩ̃́ ɩ̃̂ ɩ̃᷆ ɩ̄ ɩ̌ ɩ᷆ ɪ̃ ɯ̀ ɯ́ ɯ̂ ɯ̄ ɯ̋ ɯ̏ ɵ̀ ɵ́ ɵ̂ ʉ̀ ʉ́ ʉ̂ ʉ̄ ʉ̈ ʉ̌ ʊ̀ ʊ́ ʊ̂ ʊ̃ ʊ̃́ ʊ̄ ʊ̌ ʋ̀ ʋ́ ʋ̂ ʋ̃ ʋ̃̀ ʋ̃́ ʋ̈ ʋ̌ ʌ̀ ʌ́ ʌ̂ ʌ̄ ʌ̋ ʌ̏ Ḛ̀ Ḛ́ Ḛ̄ ḛ̀ ḛ́ ḛ̄ Ḭ̀ Ḭ́ Ḭ̄ ḭ̀ ḭ́ ḭ̄ Ṵ̀ Ṵ́ Ṵ̄ ṵ̀ ṵ́ ṵ̄ Ạ́ Ạ̃ ạ́ ạ̃ Ẹ̀ Ẹ́ Ẹ̃ Ẹ̄ Ẹ̌ ẹ̀ ẹ́ ẹ̃ ẹ̄ ẹ̌ Ẽ̀ Ẽ́ Ẽ̂ Ẽ̄ Ẽ̌ Ẽ̱ ẽ̀ ẽ́ ẽ̂ ẽ̄ ẽ̌ ẽ̱ Ị̀ Ị́ Ị̂ Ị̃ Ị̄ Ị̌ ị̀ ị́ ị̂ ị̃ ị̄ ị̌ Ọ̀ Ọ́ Ọ̃ Ọ̄ Ọ̌ ọ̀ ọ́ ọ̃ ọ̄ ọ̌ Ụ̀ Ụ́ Ụ̂ Ụ̃ Ụ̄ Ụ̌ ụ̀ ụ́ ụ̂ ụ̃ ụ̄ ụ̌ Ɑ̀ Ɑ́ Ɑ̂ Ɑ̄ Ɑ̌ Ɐ̀ Ɐ́ Ɐ̂ Ɥ̀ Ɥ́ Ɥ̂ Ɥ̃̀ Ɪ̃ Ꞷ̃ ꞷ̃ Ɤ̀ Ɤ́ Ɤ̂ Ɤ̄ Ɤ̋ Ɤ̏
`

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Latin_African.nam](/data/results/nam/GF_Latin_African.nam)

Glyphs.app source file: [GF_Latin_African.glyphs](/data/results/glyphs/GF_Latin_African.glyphs)

Text files: [GF_Latin_African.txt](/data/results/txt/nice-names/GF_Latin_African.txt) (nice names) and [GF_Latin_African.txt](/data/results/txt/nice-names/GF_Latin_African.txt) (production name)

Glyphs.app Custom Filter List (contains all Latin glyphsets): [CustomFilter_GF_Latin.plist](/data/results/plist/CustomFilter_GF_Latin.plist)


# GF Latin Beyond

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> Support for indigenous Latin-based languages from European and American regions (< 5M speakers), that are not supported in Latin Core.
> 
> **This below is taken from the old README and is not accurate, as it lists languages that accidentally happen to be covered under this glyphset but are not actually intended to be covered here. This set needs more consideration:** Abron, Acholi, Achuar-Shiwiar, Adangme, Aguaruna, Ahtna, Akoose, Alekano, Aleut, Anaang, Anufo, Apinayé, Arabela, Asturian, Atayal, Awa-Cuaiquer, Awetí, Awing, Baatonum, Baoulé, Boko (Benin), Bora, Bouna Kulango, Buginese, Cashinahua, Chachi, Chayahuita, Dagbani, Dendi (Benin), Dimli, Dinka, Embu, Fanti, Ga, Gagauz, Gonja, Gwichʼin, Kaingang, Kamba (Kenya), Kaqchikel, Kikuyu, Kirmanjki, Krio, Kwak’wala, Lamnso', Lingala, Lozi, Luba-Katanga, Mandinka, Mandjak, Mankanya, Mende (Sierra Leone), Meta’, Metlatónoc Mixtec, Mezquital Otomi, Mi'kmaq, Mirandese, Murui Huitoto, Muslim Tat, Navajo, North Azerbaijani, Northeastern Dinka, Northern Kissi, Northern Sami, Nuer, Nuuchahnulth, Nyamwezi, Nyemba, Nzima, Otuho, Paraguayan Guaraní, Pite Sami, Páez, Secoya, Sharanahua, Shilluk, Shuar, Siona, Skolt Sami, South Azerbaijani, Southern Dagaare, Talysh, Ticuna, Toba, Tojolabal, Totontepec Mixe, Tsafiki, Tsakhur, Tuvalu, Twi, Umbundu, Ume Sami, Waama, Walser, Waorani, Wasa, Xavánte, Yagua, Yangben, Yanomamö, Zuni

`GF_Latin_Beyond` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Latin_Beyond.yaml) as:

* Script: Latin
* Characters and glyphs defined in [GF_Latin_Beyond.stub.glyphs](/data/definitions/per_glyphset/GF_Latin_Beyond.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Latin_Beyond.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Latin_Beyond.nam](/data/results/nam/GF_Latin_Beyond.nam)

Glyphs.app source file: [GF_Latin_Beyond.glyphs](/data/results/glyphs/GF_Latin_Beyond.glyphs)

Text files: [GF_Latin_Beyond.txt](/data/results/txt/nice-names/GF_Latin_Beyond.txt) (nice names) and [GF_Latin_Beyond.txt](/data/results/txt/nice-names/GF_Latin_Beyond.txt) (production name)

Glyphs.app Custom Filter List (contains all Latin glyphsets): [CustomFilter_GF_Latin.plist](/data/results/plist/CustomFilter_GF_Latin.plist)


# GF Latin Core

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> Languages of Europe and the Americas with >5M speakers, with manually curated exceptions. This set is the minimal set required for all families meant to be onboarded into Google Fonts.

`GF_Latin_Core` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Latin_Core.yaml) as:

* Script: Latin
* Characters and glyphs defined in [GF_Latin_Core.stub.glyphs](/data/definitions/per_glyphset/GF_Latin_Core.stub.glyphs)
* Characters and glyphs defined in [ca_Latn.stub.glyphs](/data/definitions/per_language/ca_Latn.stub.glyphs)
* List of languages: `
Albanian (sq_Latn),
Catalan (ca_Latn),
Croatian (hr_Latn),
Czech (cs_Latn),
Danish (da_Latn),
Dutch (nl_Latn),
English (en_Latn),
Finnish (fi_Latn),
French (fr_Latn),
German (de_Latn),
Hungarian (hu_Latn),
Icelandic (is_Latn),
Italian (it_Latn),
Latvian (lv_Latn),
Lithuanian (lt_Latn),
Maltese (mt_Latn),
Norwegian Bokmål (nb_Latn),
Polish (pl_Latn),
Portuguese (pt_Latn),
Romanian (ro_Latn),
Serbian (Latin) (sr_Latn),
Slovak (sk_Latn),
Spanish (es_Latn),
Swedish (sv_Latn),
Turkish (tr_Latn),
Welsh (cy_Latn)
`

### Decomposed Characters

The following 2 composed character sequences are decomposed in the font:

`
ÍJ́ íj́
`

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Latin_Core.nam](/data/results/nam/GF_Latin_Core.nam)

Glyphs.app source file: [GF_Latin_Core.glyphs](/data/results/glyphs/GF_Latin_Core.glyphs)

Text files: [GF_Latin_Core.txt](/data/results/txt/nice-names/GF_Latin_Core.txt) (nice names) and [GF_Latin_Core.txt](/data/results/txt/nice-names/GF_Latin_Core.txt) (production name)

Glyphs.app Custom Filter List (contains all Latin glyphsets): [CustomFilter_GF_Latin.plist](/data/results/plist/CustomFilter_GF_Latin.plist)


# GF Latin Kernel

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> Support ASCII + necessary punctuation and symbols for English language. This set is the minimal set required for non-latin script families that are not meant to be used in latin language based context. 
> 
> English support is still mandatory for technical reasons: application support on one hand, and GF platform display on the other hand (to avoid .notdef glyphs appearing everywhere on the website). GF encourages designers to also support GF Latin Core glyphset, in addition to any script, so native speakers living abroad can also enjoy and use the font wherever they are in the world.
> 
> **This below is taken from the old README and is not accurate, as it lists languages that accidentally happen to be covered under this glyphset but are not actually intended to be covered here. This set needs more consideration:** Afar, Eastern Arrernte, Amahuaca, Amis, Amarakaeri, Asu (Tanzania), Batak Toba, Bemba (Zambia), Bena (Tanzania), Bikol, Bislama, Batak Dairi, Batak Mandailing, Batak Simalungun, Batak Karo, Candoshi-Shapra, Cebuano, Chiga, Chokwe, Asháninka, Seselwa Creole French, Tedim Chin, Taita, Andaandi, Dongolawi, Nobiin, Fijian, Borana-Arsi-Guji Oromo, West Central Oromo, Gilbertese, Gusii, Eastern Oromo, Northern Qiandong Miao, Hiligaynon, Southern Qiandong Miao, Hani, Huastec, Indonesian, Jamaican Creole English, Japanese, Kalaallisut, Makonde, Kekchí, Kinyarwanda, Kalenjin, Kimbundu, Kongo, Shambala, Kituba (DRC), Kuanyama, Ladino, Latin, Luba-Lulua, Luo (Kenya and Tanzania), Mauritian Creole, Makhuwa-Meetto, Minangkabau, Murrinh-Patha, Ixcatlán Mazatec, Naga Pidgin, South Ndebele, North Ndebele, Ndonga, Ao Naga, Nyankole, Orma, Pampanga, Pintupi-Luritja, Paluan, Pohnpeian, Upper Guinea Crioulo, K'iche', Rotokas, Rundi, Rwa, Samburu, Sena, Shipibo-Conibo, Shawnee, Shona, Soninke, Somali, Swati, Maore Comorian, Congo Swahili, Swahili, Tok Pisin, Tsonga, Tumbuka, Tzeltal, Tzotzil, Northern Uzbek, Warlpiri, Wik-Mungkan, Mwani, Wiradjuri, Wangaaybuwan-Ngiyambaa, Xhosa, Kenzi, Mattokki, Soga, Yindjibarndi, Makwe, Ngazidja Comorian, Malaysian, Standard Malay, Zulu.
> 

`GF_Latin_Kernel` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Latin_Kernel.yaml) as:

* Script: Latin
* Characters and glyphs defined in [GF_Latin_Kernel.stub.glyphs](/data/definitions/per_glyphset/GF_Latin_Kernel.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Latin_Kernel.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Latin_Kernel.nam](/data/results/nam/GF_Latin_Kernel.nam)

Glyphs.app source file: [GF_Latin_Kernel.glyphs](/data/results/glyphs/GF_Latin_Kernel.glyphs)

Text files: [GF_Latin_Kernel.txt](/data/results/txt/nice-names/GF_Latin_Kernel.txt) (nice names) and [GF_Latin_Kernel.txt](/data/results/txt/nice-names/GF_Latin_Kernel.txt) (production name)

Glyphs.app Custom Filter List (contains all Latin glyphsets): [CustomFilter_GF_Latin.plist](/data/results/plist/CustomFilter_GF_Latin.plist)


# GF Latin Plus

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> Additional set of symbols for basic math and economy. This includes the 3 sets Kernel/Core/Vietnamese. This set add to GF Core some support for all in use currencies and basic math symboles and punctuation. It adds necessary glyphs for fraction feature support. All fonts commissionned by Google should have a glyphset support up to this level: Core-Vietnamese-Plus.

`GF_Latin_Plus` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Latin_Plus.yaml) as:

* Script: Latin
* Characters and glyphs defined in [GF_Latin_Plus.stub.glyphs](/data/definitions/per_glyphset/GF_Latin_Plus.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Latin_Plus.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Latin_Plus.nam](/data/results/nam/GF_Latin_Plus.nam)

Glyphs.app source file: [GF_Latin_Plus.glyphs](/data/results/glyphs/GF_Latin_Plus.glyphs)

Text files: [GF_Latin_Plus.txt](/data/results/txt/nice-names/GF_Latin_Plus.txt) (nice names) and [GF_Latin_Plus.txt](/data/results/txt/nice-names/GF_Latin_Plus.txt) (production name)

Glyphs.app Custom Filter List (contains all Latin glyphsets): [CustomFilter_GF_Latin.plist](/data/results/plist/CustomFilter_GF_Latin.plist)


# GF Latin PriAfrican

`GF_Latin_PriAfrican` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Latin_PriAfrican.yaml) as:

* Script: Latin
* Characters and glyphs defined in [GF_Latin_PriAfrican.stub.glyphs](/data/definitions/per_glyphset/GF_Latin_PriAfrican.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Latin_PriAfrican.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Latin_PriAfrican.nam](/data/results/nam/GF_Latin_PriAfrican.nam)

Glyphs.app source file: [GF_Latin_PriAfrican.glyphs](/data/results/glyphs/GF_Latin_PriAfrican.glyphs)

Text files: [GF_Latin_PriAfrican.txt](/data/results/txt/nice-names/GF_Latin_PriAfrican.txt) (nice names) and [GF_Latin_PriAfrican.txt](/data/results/txt/nice-names/GF_Latin_PriAfrican.txt) (production name)

Glyphs.app Custom Filter List (contains all Latin glyphsets): [CustomFilter_GF_Latin.plist](/data/results/plist/CustomFilter_GF_Latin.plist)


# GF Latin Vietnamese

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> Achuar-Shiwiar, Aguaruna, Apinayé, Bini, Cashinahua, Chachi, Embu, Kaingang, Kamba (Kenya), Kikuyu, Mirandese, Páez, Shuar, Toba, Umbundu, Vietnamese, Walser, Waorani, Xavánte

`GF_Latin_Vietnamese` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Latin_Vietnamese.yaml) as:

* Script: Latin
* Characters and glyphs defined in [GF_Latin_Vietnamese.stub.glyphs](/data/definitions/per_glyphset/GF_Latin_Vietnamese.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Latin_Vietnamese.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Latin_Vietnamese.nam](/data/results/nam/GF_Latin_Vietnamese.nam)

Glyphs.app source file: [GF_Latin_Vietnamese.glyphs](/data/results/glyphs/GF_Latin_Vietnamese.glyphs)

Text files: [GF_Latin_Vietnamese.txt](/data/results/txt/nice-names/GF_Latin_Vietnamese.txt) (nice names) and [GF_Latin_Vietnamese.txt](/data/results/txt/nice-names/GF_Latin_Vietnamese.txt) (production name)

Glyphs.app Custom Filter List (contains all Latin glyphsets): [CustomFilter_GF_Latin.plist](/data/results/plist/CustomFilter_GF_Latin.plist)


# GF Phonetics APA

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> These glyphs sets are still a work in progress. Any research, resource and contribution are welcome!!

`GF_Phonetics_APA` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Phonetics_APA.yaml) as:

* Script: Phonetics
* Characters and glyphs defined in [GF_Phonetics_APA.stub.glyphs](/data/definitions/per_glyphset/GF_Phonetics_APA.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Phonetics_APA.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Phonetics_APA.nam](/data/results/nam/GF_Phonetics_APA.nam)

Glyphs.app source file: [GF_Phonetics_APA.glyphs](/data/results/glyphs/GF_Phonetics_APA.glyphs)

Text files: [GF_Phonetics_APA.txt](/data/results/txt/nice-names/GF_Phonetics_APA.txt) (nice names) and [GF_Phonetics_APA.txt](/data/results/txt/nice-names/GF_Phonetics_APA.txt) (production name)

Glyphs.app Custom Filter List (contains all Phonetics glyphsets): [CustomFilter_GF_Phonetics.plist](/data/results/plist/CustomFilter_GF_Phonetics.plist)


# GF Phonetics DisorderedSpeech

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> These glyphs sets are still a work in progress. Any research, resource and contribution are welcome!!

`GF_Phonetics_DisorderedSpeech` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Phonetics_DisorderedSpeech.yaml) as:

* Script: Phonetics
* Characters and glyphs defined in [GF_Phonetics_DisorderedSpeech.stub.glyphs](/data/definitions/per_glyphset/GF_Phonetics_DisorderedSpeech.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Phonetics_DisorderedSpeech.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Phonetics_DisorderedSpeech.nam](/data/results/nam/GF_Phonetics_DisorderedSpeech.nam)

Glyphs.app source file: [GF_Phonetics_DisorderedSpeech.glyphs](/data/results/glyphs/GF_Phonetics_DisorderedSpeech.glyphs)

Text files: [GF_Phonetics_DisorderedSpeech.txt](/data/results/txt/nice-names/GF_Phonetics_DisorderedSpeech.txt) (nice names) and [GF_Phonetics_DisorderedSpeech.txt](/data/results/txt/nice-names/GF_Phonetics_DisorderedSpeech.txt) (production name)

Glyphs.app Custom Filter List (contains all Phonetics glyphsets): [CustomFilter_GF_Phonetics.plist](/data/results/plist/CustomFilter_GF_Phonetics.plist)


# GF Phonetics IPAHistorical

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> These glyphs sets are still a work in progress. Any research, resource and contribution are welcome!!

`GF_Phonetics_IPAHistorical` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Phonetics_IPAHistorical.yaml) as:

* Script: Phonetics
* Characters and glyphs defined in [GF_Phonetics_IPAHistorical.stub.glyphs](/data/definitions/per_glyphset/GF_Phonetics_IPAHistorical.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Phonetics_IPAHistorical.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Phonetics_IPAHistorical.nam](/data/results/nam/GF_Phonetics_IPAHistorical.nam)

Glyphs.app source file: [GF_Phonetics_IPAHistorical.glyphs](/data/results/glyphs/GF_Phonetics_IPAHistorical.glyphs)

Text files: [GF_Phonetics_IPAHistorical.txt](/data/results/txt/nice-names/GF_Phonetics_IPAHistorical.txt) (nice names) and [GF_Phonetics_IPAHistorical.txt](/data/results/txt/nice-names/GF_Phonetics_IPAHistorical.txt) (production name)

Glyphs.app Custom Filter List (contains all Phonetics glyphsets): [CustomFilter_GF_Phonetics.plist](/data/results/plist/CustomFilter_GF_Phonetics.plist)


# GF Phonetics IPAStandard

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> These glyphs sets are still a work in progress. Any research, resource and contribution are welcome!!

`GF_Phonetics_IPAStandard` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Phonetics_IPAStandard.yaml) as:

* Script: Phonetics
* Characters and glyphs defined in [GF_Phonetics_IPAStandard.stub.glyphs](/data/definitions/per_glyphset/GF_Phonetics_IPAStandard.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Phonetics_IPAStandard.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Phonetics_IPAStandard.nam](/data/results/nam/GF_Phonetics_IPAStandard.nam)

Glyphs.app source file: [GF_Phonetics_IPAStandard.glyphs](/data/results/glyphs/GF_Phonetics_IPAStandard.glyphs)

Text files: [GF_Phonetics_IPAStandard.txt](/data/results/txt/nice-names/GF_Phonetics_IPAStandard.txt) (nice names) and [GF_Phonetics_IPAStandard.txt](/data/results/txt/nice-names/GF_Phonetics_IPAStandard.txt) (production name)

Glyphs.app Custom Filter List (contains all Phonetics glyphsets): [CustomFilter_GF_Phonetics.plist](/data/results/plist/CustomFilter_GF_Phonetics.plist)


# GF Phonetics SinoExt

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> These glyphs sets are still a work in progress. Any research, resource and contribution are welcome!!

`GF_Phonetics_SinoExt` is **statically** defined [here](/Lib/glyphsets/definitions/GF_Phonetics_SinoExt.yaml) as:

* Script: Phonetics
* Characters and glyphs defined in [GF_Phonetics_SinoExt.stub.glyphs](/data/definitions/per_glyphset/GF_Phonetics_SinoExt.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_Phonetics_SinoExt.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_Phonetics_SinoExt.nam](/data/results/nam/GF_Phonetics_SinoExt.nam)

Glyphs.app source file: [GF_Phonetics_SinoExt.glyphs](/data/results/glyphs/GF_Phonetics_SinoExt.glyphs)

Text files: [GF_Phonetics_SinoExt.txt](/data/results/txt/nice-names/GF_Phonetics_SinoExt.txt) (nice names) and [GF_Phonetics_SinoExt.txt](/data/results/txt/nice-names/GF_Phonetics_SinoExt.txt) (production name)

Glyphs.app Custom Filter List (contains all Phonetics glyphsets): [CustomFilter_GF_Phonetics.plist](/data/results/plist/CustomFilter_GF_Phonetics.plist)


# GF TransLatin Arabic

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> These glyphs sets are still a work in progress. Any research, resource and contribution are welcome!!

`GF_TransLatin_Arabic` is **statically** defined [here](/Lib/glyphsets/definitions/GF_TransLatin_Arabic.yaml) as:

* Script: TransLatin
* Characters and glyphs defined in [GF_TransLatin_Arabic.stub.glyphs](/data/definitions/per_glyphset/GF_TransLatin_Arabic.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_TransLatin_Arabic.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_TransLatin_Arabic.nam](/data/results/nam/GF_TransLatin_Arabic.nam)

Glyphs.app source file: [GF_TransLatin_Arabic.glyphs](/data/results/glyphs/GF_TransLatin_Arabic.glyphs)

Text files: [GF_TransLatin_Arabic.txt](/data/results/txt/nice-names/GF_TransLatin_Arabic.txt) (nice names) and [GF_TransLatin_Arabic.txt](/data/results/txt/nice-names/GF_TransLatin_Arabic.txt) (production name)

Glyphs.app Custom Filter List (contains all TransLatin glyphsets): [CustomFilter_GF_TransLatin.plist](/data/results/plist/CustomFilter_GF_TransLatin.plist)


# GF TransLatin Pinyin

> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_
> 
> These glyphs sets are still a work in progress. Any research, resource and contribution are welcome!!

`GF_TransLatin_Pinyin` is **statically** defined [here](/Lib/glyphsets/definitions/GF_TransLatin_Pinyin.yaml) as:

* Script: TransLatin
* Characters and glyphs defined in [GF_TransLatin_Pinyin.stub.glyphs](/data/definitions/per_glyphset/GF_TransLatin_Pinyin.stub.glyphs)

> [!CAUTION]  
> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.
> Please add language code definions [here](/Lib/glyphsets/definitions/GF_TransLatin_Pinyin.yaml).

### Resulting Glyphset Files

.nam file (only encoded characters): [GF_TransLatin_Pinyin.nam](/data/results/nam/GF_TransLatin_Pinyin.nam)

Glyphs.app source file: [GF_TransLatin_Pinyin.glyphs](/data/results/glyphs/GF_TransLatin_Pinyin.glyphs)

Text files: [GF_TransLatin_Pinyin.txt](/data/results/txt/nice-names/GF_TransLatin_Pinyin.txt) (nice names) and [GF_TransLatin_Pinyin.txt](/data/results/txt/nice-names/GF_TransLatin_Pinyin.txt) (production name)

Glyphs.app Custom Filter List (contains all TransLatin glyphsets): [CustomFilter_GF_TransLatin.plist](/data/results/plist/CustomFilter_GF_TransLatin.plist)

