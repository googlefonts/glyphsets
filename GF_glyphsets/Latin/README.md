Google Fonts Latin Character Sets
==================================

GF defines 6 level of language support for latin fonts:

1. Kernel: support ASCII + necessary punctuation and symbols for English language.
2. Core: support latin alphabets for European and American languages >5M speakers (incl. Kernel).
3. Vietnamese: additional support for Vietnamese language.
4. Plus: additional set of symbols for basic math and economy.
5. African: support for Latin African languages not supported by Latin Core.
6. Beyond: support for indigenous latin based languages from European and American regions (< 5M peakers), that are not supported in Latin Core.

All latin font families commissioned by GF should support level 4 and therefore include Vietnamese and Plus sets.

Fonts families submitted by designers through the issue tracker must support at least level 2.

GF Latin Kernel
---------------
This set is the minimal set required for non-latin script families that are not meant to be used in latin language based context. 

English support is still mandatory for technical reasons: application support on one hand, and GF platform display on the other hand (to avoid .notdef glyphs appearing evrywhere on the website). GF encourages designers to also support GF Latin Core glyphset, in addition to any script, so native speakers leaving abroad can also enjoy and use the font wherever they are in the world. 

The "English" charset actually allows the support (or transcription in Latin) of 105 languages:

Afar, Eastern Arrernte, Amahuaca, Amis, Amarakaeri, Asu (Tanzania), Batak Toba, Bemba (Zambia), Bena (Tanzania), Bikol, Bislama, Batak Dairi, Batak Mandailing, Batak Simalungun, Batak Karo, Candoshi-Shapra, Cebuano, Chiga, Chokwe, Asháninka, Seselwa Creole French, Tedim Chin, Taita, Andaandi, Dongolawi, Nobiin, Fijian, Borana-Arsi-Guji Oromo, West Central Oromo, Gilbertese, Gusii, Eastern Oromo, Northern Qiandong Miao, Hiligaynon, Southern Qiandong Miao, Hani, Huastec, Indonesian, Jamaican Creole English, Japanese, Kalaallisut, Makonde, Kekchí, Kinyarwanda, Kalenjin, Kimbundu, Kongo, Shambala, Kituba (DRC), Kuanyama, Ladino, Latin, Luba-Lulua, Luo (Kenya and Tanzania), Mauritian Creole, Makhuwa-Meetto, Minangkabau, Murrinh-Patha, Ixcatlán Mazatec, Naga Pidgin, South Ndebele, North Ndebele, Ndonga, Ao Naga, Nyankole, Orma, Pampanga, Pintupi-Luritja, Paluan, Pohnpeian, Upper Guinea Crioulo, K'iche', Rotokas, Rundi, Rwa, Samburu, Sena, Shipibo-Conibo, Shawnee, Shona, Soninke, Somali, Swati, Maore Comorian, Congo Swahili, Swahili, Tok Pisin, Tsonga, Tumbuka, Tzeltal, Tzotzil, Northern Uzbek, Warlpiri, Wik-Mungkan, Mwani, Wiradjuri, Wangaaybuwan-Ngiyambaa, Xhosa, Kenzi, Mattokki, Soga, Yindjibarndi, Makwe, Ngazidja Comorian, Malaysian, Standard Malay, Zulu.

GF Latin Core
---------------
This set is the minimal set required for all families meant to be onbaorded into Google Fonts; it includes GF Kernel.

It support the main latin-base languages from Europe and American regions. Like Kernel, the impact is braoder than the intention, and GF Latin Core supports 280 latin languages (or transcription to latin), so 175 additional languages: 

Acheron, Achinese, Afrikaans, Anuta, Aragonese, Arbëreshë Albanian, Arvanitika Albanian, Ashéninka Perené, Balinese, Bari, Basque, Bosnian, Breton, Caquinte, Caribbean Hindustani, Cashibo-Cacataibo, Catalan, Central Aymara, Central Kurdish, Chamorro, Chavacano, Chiltepec Chinantec, Chuukese, Cimbrian, Cofán, Cook Islands Māori, Cornish, Corsican, Creek, Crimean Tatar, Croatian, Czech, Danish, Dehu, Dutch, Eastern Abnaki, English, Ese Ejja, Faroese, Filipino, Finnish, French, Friulian, Galician, Ganda, Garifuna, Ga’anda, German, Gheg Albanian, Gooniyandi, Guadeloupean Creole French, Haitian, Hawaiian, Ho-Chunk, Hopi, Hungarian, Hän, Icelandic, Iloko, Inari Sami, Irish, Istro Romanian, Italian, Javanese, Jola-Fonyi, Kabuverdianu, Kaonde, Karelian, Kashubian, Khasi, Konzo, Kven Finnish, Kölsch, Ladin, Latgalian, Ligurian, Lithuanian, Lombard, Low German, Lower Sorbian, Lule Sami, Luxembourgish, Macedo-Romanian, Makhuwa, Malagasy, Maltese, Manx, Maori, Mapudungun, Marshallese, Matsés, Meriam Mir, Meru, Mohawk, Montagnais, Montenegrin, Munsee, Mískito, Neapolitan, Niuean, Nomatsiguenga, Northern Kurdish, Norwegian, Nyanja, Occitan, Ojitlán Chinantec, Oroqen, Palauan, Papantla Totonac, Papiamento, Pedi, Picard, Pichis Ashéninka, Piemontese, Pijin, Pipil, Polish, Portuguese, Potawatomi, Purepecha, Quechua, Romanian, Romansh, Samoan, Sango, Sangu (Tanzania), Saramaccan, Sardinian, Scottish Gaelic, Seri, Sicilian, Silesian, Slovak, Slovenian, Southern Aymara, Southern Sami, Southern Sotho, Spanish, Sranan Tongo, Standard Estonian, Standard Latvian, Sundanese, Swedish, Swiss German, Tagalog, Tahitian, Teso, Tetum, Tetun Dili, Tiv, Tokelau, Tonga (Tonga Islands), Tonga (Zambia), Tosk Albanian, Tswana, Turkish, Turkmen, Uab Meto, Upper Sorbian, Venetian, Veps, Võro, Walloon, Waray (Philippines), Wayuu, Welsh, Western Abnaki, Western Frisian, Wolof, Yanesha', Yao, Yapese, Yucateco, Zapotec, Záparo.

GF Latin Vietnamese
-------------------
299 languages, 19 more than GF Latin Core:

Achuar-Shiwiar, Aguaruna, Apinayé, Bini, Cashinahua, Chachi, Embu, Kaingang, Kamba (Kenya), Kikuyu, Mirandese, Páez, Shuar, Toba, Umbundu, Vietnamese, Walser, Waorani, Xavánte.

GF Latin Plus
-------------
This set add to GF Core some support for all in use currencies and basic math symboles and punctuation. It adds necessary glyphs for fraction feature support. All fonts commissionned by Google should have a glyphset support up to this level: Core-Vietnamese-Plus.

GF Latin African
----------------

426 languages supported, 146 more than GF Latin Core:

Abron, Achuar-Shiwiar, Adamawa Fulfulde, Adangme, Aghem, Aguaruna, Aja (Benin), Anii, Arabela, Atayal, Awa-Cuaiquer, Baatonum, Bafia, Bagirmi Fulfulde, Balkan Romani, Bambara, Baoulé, Basa (Cameroon), Biali, Boko (Benin), Bora, Borgu Fulfulde, Bouna Kulango, Bushi, Cashinahua, Central Nahuatl, Central-Eastern Niger Fulfulde, Chachi, Chayahuita, Dagbani, Dendi (Benin), Dimli, Dinka, Ditammari, Duala, Dyula, Eastern Maninkakan, Embu, Ewe, Ewondo, Fanti, Fon, Foodo, Ga, Gen, Gonja, Guinea Kpelle, Gwichʼin, Hausa, Kabiyè, Kamba (Kenya), Kanuri, Kaqchikel, Kara-Kalpak, Kasem, Khoekhoe, Kikuyu, Kirmanjki, Koyra Chiini Songhay, Koyraboro Senni Songhai, Krio, Kwasio, Lakota, Lamnso', Langi, Lingala, Lobi, Lozi, Luba-Katanga, Lukpa, Maasina Fulfulde, Mam, Masai, Mbelime, Mende (Sierra Leone), Meta’, Metlatónoc Mixtec, Mezquital Otomi, Mi'kmaq, Mirandese, Miyobe, Moba, Mossi, Mundang, Murui Huitoto, Muslim Tat, Nateni, Navajo, Ngiemboon, Ngomba, Nigerian Fulfulde, North Azerbaijani, North Marquesan, Northeastern Dinka, Northern Kissi, Nuer, Nyamwezi, Nyemba, Nzima, Otuho, Prussian, Pulaar, Pular, Páez, Secoya, Serer, Sharanahua, Shilluk, Shuar, Siona, Skolt Sami, South Azerbaijani, South Marquesan, Southern Dagaare, Sukuma, Susu, Talysh, Tasawaq, Tem, Ticuna, Timne, Tojolabal, Totontepec Mixe, Tsafiki, Tsakhur, Tuvalu, Twi, Umbundu, Urarina, Venda, Vlax Romani, Waama, Waci Gbe, Wallisian, Walser, Waorani, Wasa, Western Niger Fulfulde, Xavánte, Xwela Gbe, Yagua, Yangben, Yanomamö, Yom, Zarma, Zuni


GF Latin Beyond
---------------
380 languages supported, 98 more than Latin Core:

Abron, Acholi, Achuar-Shiwiar, Adangme, Aguaruna, Ahtna, Akoose, Alekano, Aleut, Anaang, Anufo, Apinayé, Arabela, Asturian, Atayal, Awa-Cuaiquer, Awetí, Awing, Baatonum, Baoulé, Boko (Benin), Bora, Bouna Kulango, Buginese, Cashinahua, Chachi, Chayahuita, Dagbani, Dendi (Benin), Dimli, Dinka, Embu, Fanti, Ga, Gagauz, Gonja, Gwichʼin, Kaingang, Kamba (Kenya), Kaqchikel, Kikuyu, Kirmanjki, Krio, Kwak’wala, Lamnso', Lingala, Lozi, Luba-Katanga, Mandinka, Mandjak, Mankanya, Mende (Sierra Leone), Meta’, Metlatónoc Mixtec, Mezquital Otomi, Mi'kmaq, Mirandese, Murui Huitoto, Muslim Tat, Navajo, North Azerbaijani, Northeastern Dinka, Northern Kissi, Northern Sami, Nuer, Nuuchahnulth, Nyamwezi, Nyemba, Nzima, Otuho, Paraguayan Guaraní, Pite Sami, Páez, Secoya, Sharanahua, Shilluk, Shuar, Siona, Skolt Sami, South Azerbaijani, Southern Dagaare, Talysh, Ticuna, Toba, Tojolabal, Totontepec Mixe, Tsafiki, Tsakhur, Tuvalu, Twi, Umbundu, Ume Sami, Waama, Walser, Waorani, Wasa, Xavánte, Yagua, Yangben, Yanomamö, Zuni
