# Google Fonts glyphset definitions to be consumed by other tools.
# The "script" value needs to correspond to the folder name
# in /GF_Glyphsets of this repo in order to find the other definition files.

import os

glyphset_definitions = {
    "GF_Latin_Kernel": {"script": "Latin", "language_codes": []},
    "GF_Latin_Core": {
        "script": "Latin",
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
    "GF_Latin_African": {
        "script": "Latin",
        "use_auxiliary": True,
        "language_codes": [
            "aa_Latn"  # Afar
            "abi_Latn"  # Abidji
            "abn_Latn"  # Abua
            "abr_Latn"  # Abron
            "acd_Latn"  # Gikyode
            "ach_Latn"  # Acoli
            "ada_Latn"  # Adangme
            "ade_Latn"  # Adele
            "adj_Latn"  # Adioukrou
            "aeb_Latn"  # Tunisian Darija
            "af_Latn"  # Afrikaans
            "agc_Latn"  # Agatu
            "agq_Latn"  # Aghem
            "aha_Latn"  # Ahanta
            "ahl_Latn"  # Igo
            "ahs_Latn"  # Ashe
            "ajg_Latn"  # Aja
            "akp_Latn"  # Siwu
            "ala_Latn"  # Alago
            "amo_Latn"  # Amo
            "anc_Latn"  # Ngas
            "ank_Latn"  # Goemai
            "ann_Latn"  # Obolo
            "anv_Latn"  # Denya
            "anw_Latn"  # Anaang
            "any_Latn"  # Anyin
            "apd_Latn"  # Sudanese Arabic
            "asa_Latn"  # Asu
            "asg_Latn"  # Cishingini
            "atg_Latn"  # Ivbie North-Okpela-Arhe
            "ati_Latn"  # Attié
            "avn_Latn"  # Avatime
            "avu_Latn"  # Avokaya
            "awc_Latn"  # Cicipu
            "awo_Latn"  # Awak
            "ayb_Latn"  # Ayizo Gbe
            "azo_Latn"  # Awing
            "bas_Latn"  # Basaa
            "bav_Latn"  # Vengo
            "bax_Latn"  # Bamun, Latin
            "bba_Latn"  # Baatonum
            "bbj_Latn"  # Ghomala
            "bbo_Latn"  # Northern Bobo Madaré
            "bbp_Latn"  # Banda, West Central
            "bci_Latn"  # Baoulé
            "bcn_Latn"  # Bali
            "bcq_Latn"  # Bench
            "bcw_Latn"  # Bana
            "bcy_Latn"  # Bacama
            "bdh_Latn"  # Baka
            "beh_Latn"  # Baka
            "bej_Latn"  # Bedawiyet
            "bem_Latn"  # Bemba
            "bet_Latn"  # Bété, Guiberoua
            "bev_Latn"  # Bété, Daloa
            "bex_Latn"  # Jur Modo
            "bez_Latn"  # Bena
            "bfa_Latn"  # Bari
            "bfd_Latn"  # Bafut
            "bfo_Latn"  # Malba Birifor
            "bhy_Latn"  # Bhele
            "bib_Latn"  # Bissa
            "bim_Latn"  # Bimoba
            "bin_Latn"  # Bini
            "biv_Latn"  # Birifor, Southern
            "bjt_Latn"  # Balanta-Ganja
            "bjv_Latn"  # Bedjond
            "bkc_Latn"  # Baka
            "bkm_Latn"  # Kom
            "bkv_Latn"  # Bekwarra
            "blo_Latn"  # Anii
            "bm_Latn"  # Bambara
            "bmq_Latn"  # Bomu
            "bng_Latn"  # Benga
            "bnm_Latn"  # Bapuku
            "bom_Latn"  # Berom
            "bov_Latn"  # Tuwuli
            "box_Latn"  # Buamu
            "boz_Latn"  # Tiéyaxo Bozo
            "bqc_Latn"  # Boko
            "bqj_Latn"  # Bandial
            "bqp_Latn"  # Bisã
            "bqv_Latn"  # Koro Wachi
            "bsc_Latn"  # Bassari
            "bsc_Latn_GN"  # Bassari
            "bsj_Latn"  # Bangwinji
            "bsp_Latn"  # Baga Sitemu
            "bsq_Latn"  # Bassa
            "bss_Latn"  # Akoose
            "btt_Latn"  # Bete-Bendi
            "buc_Latn"  # Bushi
            "bud_Latn"  # Ntcham
            "bum_Latn"  # Bulu
            "bus_Latn"  # Bokobaru
            "buu_Latn"  # Budu
            "buw_Latn"  # gevové
            "bvb_Latn"  # Bube
            "bvi_Latn"  # Belanda Viri, Latin
            "bwj_Latn"  # Láá Láá Bwamu
            "bwq_Latn"  # Southern Bobo Madaré
            "bwr_Latn"  # Bura-Pabir
            "byn_Latn"  # Bilen
            "bys_Latn"  # Burak
            "byv_Latn"  # Medumba
            "bza_Latn"  # Bandi
            "bze_Latn"  # Jenaama Bozo
            "bzw_Latn"  # Basa
            "bzx_Latn"  # Bozo, Hainyaxo
            "cae_Latn"  # Lehar
            "cbj_Latn"  # Ede Cabe
            "cch_Latn"  # Atsam
            "cdr_Latn"  # Kamuku
            "cfa_Latn"  # Dikaka
            "cgg_Latn"  # Chiga
            "cjk_Latn"  # Chokwe
            "ckl_Latn"  # Kibaku
            "cko_Latn"  # Anufo
            "cky_Latn"  # Cakfem-Mushere
            "cla_Latn"  # Ron
            "cme_Latn"  # Cerma
            "cou_Latn"  # Wamey
            "cri_Latn"  # Sãotomense
            "crs_Latn"  # Seselwa Creole French
            "csk_Latn"  # Jola-Kasa
            "cwe_Latn"  # Kwere
            "daa_Latn"  # Dangaléat
            "dag_Latn"  # Dagbani
            "dav_Latn"  # Taita
            "dbd_Latn"  # Dadiya
            "dbq_Latn"  # Daba
            "ddn_Latn"  # Dendi
            "dga_Latn"  # Dagaare, Southern
            "dgh_Latn"  # Dghwede
            "dgi_Latn"  # Northern Dagara
            "did_Latn"  # Didinga
            "din_Latn"  # Dinka
            "dip_Latn"  # Dinka, Northeastern
            "dje_Latn"  # Zarma
            "dnj_Latn"  # Dan
            "dnj_Latn_LR"  # Dan
            "dno_Latn"  # Ndrulo
            "dop_Latn"  # Lukpa
            "dow_Latn"  # Doyayo
            "dri_Latn"  # C’Lela
            "dtm_Latn"  # Tomo Kan Dogon
            "dts_Latn"  # Dogon, Toro So
            "dua_Latn"  # Duala
            "dug_Latn"  # Chiduruma
            "dur_Latn"  # Dii
            "dwr_Latn"  # Dawro
            "dya_Latn"  # Dyan
            "dyi_Latn"  # Sénoufo, Djimini
            "dyo_Latn"  # Jola-Fonyi
            "dyu_Latn"  # Dyula
            "dzg_Latn"  # Dazaga
            "ebu_Latn"  # Embu
            "ee_Latn"  # Ewe
            "efi_Latn"  # Efik
            "eka_Latn"  # Ekajuk
            "ekm_Latn"  # Elip
            "ekp_Latn"  # Ekpeye
            "ema_Latn"  # Emai-Iuleha-Ora
            "emk_Latn"  # Maninkakan, Eastern
            "enn_Latn"  # Engenni
            "eto_Latn"  # Eton (Cameroon)
            "etu_Latn"  # Ejagham
            "etx_Latn"  # Iten
            "ewo_Latn"  # Ewondo
            "eza_Latn"  # Ezaa
            "fan_Latn"  # Fang
            "fat_Latn"  # Fanti
            "ff_Latn"  # Fulah
            "ffm_Latn"  # Maasina Fulfulde
            "flr_Latn"  # Fuliiru
            "fmp_Latn"  # Fe’fe’
            "fod_Latn"  # Foodo
            "fon_Latn"  # Fon
            "fub_Latn"  # Fulfulde, Adamawa
            "fuc_Latn"  # Pulaar
            "fue_Latn"  # Fulfulde, Borgu
            "fuf_Latn"  # Pular
            "fuh_Latn"  # Fulfulde, Western Niger
            "fuq_Latn"  # Central-Eastern Niger Fulfulde
            "fuv_Latn"  # Nigerian Fulfulde
            "fvr_Latn"  # Fur
            "gaa_Latn"  # Ga
            "gby_Latn"  # Gbari
            "gde_Latn"  # Gude
            "gej_Latn"  # Gen
            "gel_Latn"  # ut-Ma’in
            "ggn_Latn"  # Eastern Gurung, Latin
            "giz_Latn"  # Southern Giziga
            "gjn_Latn"  # Gonja
            "gkn_Latn"  # Gokana
            "gkp_Latn"  # Kpelle, Guinea
            "gmm_Latn"  # Gbaya-Mbodomo
            "gmv_Latn"  # Gamo
            "gna_Latn"  # Kaansa
            "gnd_Latn"  # Zulgo-Gemzek
            "gng_Latn"  # Ngangam
            "goa_Latn"  # Guro
            "god_Latn"  # Godié
            "gof_Latn"  # Gofa
            "gov_Latn"  # Goo
            "gqr_Latn"  # Gor
            "grb_Latn"  # Grebo
            "gud_Latn"  # Dida, Yocoboué
            "guk_Latn"  # Gumuz
            "gur_Latn"  # Frafra
            "guw_Latn"  # Gun
            "gux_Latn"  # Gourmanchéma
            "guz_Latn"  # Gusii
            "gvl_Latn"  # Gulay
            "gyi_Latn"  # Gyele
            "ha_Latn"  # Hausa
            "hag_Latn"  # Hanga
            "har_Latn"  # Harari
            "hia_Latn"  # Lamang
            "hig_Latn"  # Kamwe
            "hna_Latn"  # Mina
            "hz_Latn"  # Herero
            "ibb_Latn"  # Ibibio
            "iby_Latn"  # Ibani
            "ica_Latn"  # Ede Ica
            "ich_Latn"  # Etkywan
            "idd_Latn"  # Ede Idaca
            "idu_Latn"  # Idoma
            "ife_Latn"  # Ifè
            "ig_Latn"  # Igbo
            "igb_Latn"  # Ebira
            "ige_Latn"  # Igede
            "ijj_Latn"  # Ede Ije
            "ijs_Latn"  # Ijo, Southeast
            "ikk_Latn"  # Ika
            "ikw_Latn"  # Ikwere
            "ikx_Latn"  # Ik
            "iqw_Latn"  # Ikwo
            "iri_Latn"  # Rigwe
            "ish_Latn"  # Esan
            "izr_Latn"  # Izere
            "izz_Latn"  # Izii
            "jab_Latn"  # Hyam
            "jbu_Latn"  # Jukun Takum
            "jen_Latn"  # Dza
            "jgk_Latn"  # Gwak
            "jgo_Latn"  # Ngomba
            "jib_Latn"  # Jibu
            "jmc_Latn"  # Machame
            "kab_Latn"  # Kabyle
            "kad_Latn"  # Adara
            "kai_Latn"  # Karekare
            "kaj_Latn"  # Jju
            "kam_Latn"  # Kamba
            "kao_Latn"  # Xaasongaxango
            "kbp_Latn"  # Kabiyé
            "kby_Latn"  # Kanuri, Manga
            "kcg_Latn"  # Tyap
            "kck_Latn"  # Kalanga
            "kdc_Latn"  # Kutu
            "kde_Latn"  # Makonde
            "kdh_Latn"  # Tem
            "kdl_Latn"  # Tsikimba
            "kea_Latn"  # Kabuverdianu
            "ken_Latn"  # Kenyang
            "keu_Latn"  # Akebu
            "kez_Latn"  # Kukele
            "kfo_Latn"  # Koro
            "kg_Latn"  # Kongo
            "khq_Latn"  # Koyra Chiini
            "ki_Latn"  # Kikuyu
            "kia_Latn"  # Kim
            "kib_Latn"  # Koalib
            "kj_Latn"  # Kuanyama
            "kkj_Latn"  # Kako
            "kln_Latn"  # Kalenjin
            "kmb_Latn"  # Kimbundu
            "kmy_Latn"  # Koma
            "knc_Latn"  # Kanuri, Central
            "knf_Latn"  # Mankanya
            "knp_Latn"  # Kwanja
            "koo_Latn"  # Konjo
            "kpe_Latn"  # Kpelle
            "kpo_Latn"  # Ikposo
            "kqn_Latn"  # Kaonde
            "kqp_Latn"  # Kimré
            "kqs_Latn"  # Kissi, Northern
            "kr_Latn"  # Kanuri
            "kri_Latn"  # Krio
            "krs_Latn"  # Gbaya (Sudan)
            "ksb_Latn"  # Shambala
            "ksf_Latn"  # Bafia
            "ksp_Latn"  # Kabba
            "kss_Latn"  # Southern Kisi
            "kst_Latn"  # Winyé
            "ktj_Latn"  # Krumen, Plapo
            "ktu_Latn"  # Kituba
            "ktz_Latn"  # Juǀʼhoan
            "kub_Latn"  # Kutep
            "kuj_Latn"  # Kuria
            "kun_Latn"  # Kunama
            "kus_Latn"  # Kusaal
            "kvf_Latn"  # Kabalai
            "kye_Latn"  # Krache
            "kyf_Latn"  # Kouya
            "kyq_Latn"  # Kenga
            "kzc_Latn"  # Bondoukou Kulango
            "kzr_Latn"  # Karang
            "lag_Latn"  # Langi
            "laj_Latn"  # Lango [Uganda]
            "lam_Latn"  # Lamba
            "las_Latn"  # Lama (Togo)
            "ldb_Latn"  # Duya
            "led_Latn"  # Lendu
            "lee_Latn"  # Lyélé
            "lem_Latn"  # Nomaande
            "les_Latn"  # Lese
            "lg_Latn"  # Ganda
            "lgg_Latn"  # Lugbara
            "lia_Latn"  # Limba, West-Central
            "lig_Latn"  # Ligbi
            "lip_Latn"  # Sekpele
            "lln_Latn"  # Lele
            "lmp_Latn"  # Limbum
            "ln_Latn"  # Lingala
            "lnl_Latn"  # South Central Banda
            "lns_Latn"  # Lamnso’
            "lnu_Latn"  # Longuda
            "lob_Latn"  # Lobi
            "log_Latn"  # Logo
            "lok_Latn"  # Loko
            "lol_Latn"  # Mongo
            "loq_Latn"  # Lobala
            "lor_Latn"  # Téén
            "lot_Latn"  # Otuho
            "loz_Latn"  # Lozi
            "lu_Latn"  # Luba-Katanga
            "lua_Latn"  # Luba-Lulua
            "lue_Latn"  # Luvale
            "lun_Latn"  # Lunda
            "luo_Latn"  # Luo
            "luy_Latn"  # Luyia
            "lwo_Latn"  # Luwo
            "maf_Latn"  # Mafa
            "man_Latn"  # Mandingo
            "mas_Latn"  # Masai
            "maw_Latn"  # Mampruli
            "mbo_Latn"  # Mbo
            "mbu_Latn"  # Mbula-Bwazza
            "mcn_Latn"  # Masana
            "mcp_Latn"  # Makaa
            "mcu_Latn"  # Mambila, Cameroon
            "mda_Latn"  # Mada
            "mdj_Latn"  # Mangbetu
            "mdt_Latn"  # Mbere
            "men_Latn"  # Mende
            "meq_Latn"  # Merey
            "mer_Latn"  # Meru
            "mev_Latn"  # Mano
            "mey_Latn"  # Hassaniyya
            "mfd_Latn"  # Mendankwe-Nkwen
            "mfe_Latn"  # Morisyen
            "mfi_Latn"  # Wandala
            "mfn_Latn"  # Mbembe, Cross River
            "mfo_Latn"  # Mbe
            "mfq_Latn"  # Moba
            "mfv_Latn"  # Mandjak
            "mg_Latn"  # Malagasy
            "mgc_Latn"  # Morokodo
            "mge_Latn"  # Mango
            "mgh_Latn"  # Makhuwa-Meetto
            "mgo_Latn"  # Metaʼ
            "mgy_Latn"  # Mbunga
            "mhi_Latn"  # Ma’di
            "mkl_Latn"  # Mokole
            "mls_Latn"  # Masalit
            "mmu_Latn"  # Mmaala
            "mnf_Latn"  # Mundani
            "mnk_Latn"  # Mandinka
            "moa_Latn"  # Mwan
            "mor_Latn"  # Moro
            "mos_Latn"  # Mossi
            "mqb_Latn"  # Mbuko
            "mql_Latn"  # Mbelime
            "msc_Latn"  # Maninka, Sankaran
            "mua_Latn"  # Mundang
            "muh_Latn"  # Mündü
            "mur_Latn"  # Murle
            "muy_Latn"  # Muyang
            "mwk_Latn"  # Kita Maninkakan
            "mwm_Latn"  # Sar
            "mxc_Latn"  # Manyika
            "myk_Latn"  # Mamara Senoufo
            "mym_Latn"  # Me’en
            "myx_Latn"  # Masaaba
            "mzk_Latn"  # Mambila, Nigeria
            "mzm_Latn"  # Mumuye
            "mzw_Latn"  # Deg
            "naq_Latn"  # Nama
            "nat_Latn"  # Cahungwarya
            "naw_Latn"  # Nawuri
            "nba_Latn"  # Nyemba
            "ncu_Latn"  # Chumburung
            "nd_Latn"  # North Ndebele
            "ndc_Latn"  # Ndau
            "ndj_Latn"  # Ndamba
            "ndv_Latn"  # Ndut
            "ndz_Latn"  # Ndogo
            "neb_Latn"  # Toura
            "nfr_Latn"  # Nafaanra
            "nfu_Latn"  # Mfumte
            "ng_Latn"  # Ndonga
            "nga_Latn"  # Ngbaka
            "ngb_Latn"  # Ngbandi, Northern
            "ngh_Latn"  # Nǁng
            "ngl_Latn"  # Lomwe
            "ngp_Latn"  # Ngulu
            "nhb_Latn"  # Beng
            "nhu_Latn"  # Noone
            "nin_Latn"  # Ninzo
            "niy_Latn"  # Ngiti
            "nko_Latn"  # Nkonya
            "nku_Latn"  # Kulango, Bouna
            "nmg_Latn"  # Kwasio
            "nmz_Latn"  # Nawdm
            "nnh_Latn"  # Ngiemboon
            "nnq_Latn"  # Ngindo
            "nnw_Latn"  # Southern Nuni
            "nr_Latn"  # South Ndebele
            "nrb_Latn"  # Nara
            "nso_Latn"  # Northern Sotho
            "ntm_Latn"  # Nateni
            "ntr_Latn"  # Delo
            "nui_Latn"  # Kombe
            "nup_Latn"  # Nupe-Nupe-Tako
            "nus_Latn"  # Nuer
            "nuv_Latn"  # Nuni, Northern
            "nwb_Latn"  # Nyabwa
            "ny_Latn"  # Nyanja
            "nyb_Latn"  # Nyangbo
            "nym_Latn"  # Nyamwezi
            "nyn_Latn"  # Nyankole
            "nyo_Latn"  # Nyoro
            "nza_Latn"  # Tigon Mbembe
            "nzi_Latn"  # Nzima
            "nzk_Latn"  # Nzakara
            "ogc_Latn"  # Ogbah
            "oki_Latn"  # Okiek
            "okr_Latn"  # Kirike
            "om_Latn"  # Oromo
            "ozm_Latn"  # Koonzime
            "pbi_Latn"  # Parkwa
            "pcm_Latn"  # Nigerian Pidgin
            "pil_Latn"  # Yom
            "pip_Latn"  # Pero
            "pkb_Latn"  # Pokomo
            "pko_Latn"  # Pökoot
            "png_Latn"  # Pangu
            "pnz_Latn"  # Pana (Central African Republic)
            "pov_Latn"  # Crioulo, Upper Guinea
            "poy_Latn"  # Pogolo
            "pug_Latn"  # Phuie
            "puu_Latn"  # Punu
            "pym_Latn"  # Pyam
            "rcf_Latn"  # Réunion Creole French
            "rel_Latn"  # Rendille
            "res_Latn"  # Reshe
            "rif_Latn"  # Riffian (Latin)
            "rn_Latn"  # Rundi
            "rng_Latn"  # Ronga
            "rof_Latn"  # Rombo
            "rub_Latn"  # Gungu
            "ruf_Latn"  # Luguru
            "rw_Latn"  # Kinyarwanda
            "rwk_Latn"  # Rwa
            "sad_Latn"  # Sandawe
            "saf_Latn"  # Safaliba
            "saq_Latn"  # Samburu
            "sav_Latn"  # Saafi-Saafi
            "sba_Latn"  # Ngambay
            "sbd_Latn"  # Southern Samo
            "sbp_Latn"  # Sangu
            "sef_Latn"  # Cebaara Senoufo
            "seh_Latn"  # Sena
            "ses_Latn"  # Koyraboro Senni
            "sg_Latn"  # Sango
            "she_Latn"  # Sheko
            "shi_Latn"  # Tachelhit (Latin)
            "shk_Latn"  # Shilluk
            "shu_Latn"  # Arabic, Chadian Spoken
            "shz_Latn"  # Syenara Senoufo
            "sid_Latn"  # Sidamo
            "sig_Latn"  # Paasaal
            "sil_Latn"  # Sisaala, Tumulung
            "sld_Latn"  # Sissala
            "sn_Latn"  # Shona
            "snf_Latn"  # Noon
            "snk_Latn"  # Soninke
            "snw_Latn"  # Selee
            "so_Latn"  # Somali
            "sok_Latn"  # Sokoro
            "soy_Latn"  # Miyobe
            "spp_Latn"  # Sénoufo, Supyire
            "srr_Latn"  # Serer
            "ss_Latn"  # Swati
            "ssy_Latn"  # Saho
            "st_Latn"  # Southern Sotho
            "suk_Latn"  # Sukuma
            "suq_Latn"  # Suri, Tirmaga-Chai
            "sur_Latn"  # Mwaghavul
            "sus_Latn"  # Susu
            "sw_Latn"  # Swahili
            "swb_Latn"  # Maore Comorian, Latin
            "swc_Latn"  # Swahili, Congo
            "sxb_Latn"  # Suba
            "sxw_Latn"  # Saxwe Gbe
            "syi_Latn"  # Seki
            "tal_Latn"  # Tal
            "tan_Latn"  # Tangale
            "taq_Latn"  # Tamasheq, Latin
            "tbz_Latn"  # Ditammari
            "tcd_Latn"  # Tafi
            "ted_Latn"  # Krumen, Tepo
            "tem_Latn"  # Timne
            "teo_Latn"  # Teso
            "tfi_Latn"  # Gbe, Tofin
            "tik_Latn"  # Tikar
            "tiv_Latn"  # Tiv
            "tke_Latn"  # Takwane
            "tlj_Latn"  # Talinga-Bwisi
            "tmh_Latn"  # Tamashek
            "tn_Latn"  # Tswana
            "tnr_Latn"  # Ménik
            "tod_Latn"  # Toma
            "tog_Latn"  # Nyasa Tonga
            "toi_Latn"  # Tonga
            "toq_Latn"  # Toposa
            "tpm_Latn"  # Tampulma
            "ts_Latn"  # Tsonga
            "tsw_Latn"  # Tsishingini
            "ttj_Latn"  # Tooro
            "ttq_Latn"  # Tawallammat Tamajaq
            "ttr_Latn"  # Tera
            "tul_Latn"  # Tula
            "tum_Latn"  # Tumbuka
            "tuq_Latn"  # Tedaga
            "tuz_Latn"  # Turka
            "tvd_Latn"  # Tsuvadi
            "tvu_Latn"  # Tunen
            "tw_akuapem_Latn"  # Akuapem Twi
            "twq_Latn"  # Tasawaq
            "tzm_Latn"  # Central Atlas Tamazight
            "udu_Latn"  # Uduk
            "umb_Latn"  # Umbundu
            "uth_Latn"  # ut-Hun
            "utr_Latn"  # Etulo
            "vag_Latn"  # Vagla
            "vai_Latn"  # Vai (Latin)
            "ve_Latn"  # Venda
            "vid_Latn"  # Vidunda
            "vmw_Latn"  # Makhuwa
            "vun_Latn"  # Vunjo
            "vut_Latn"  # Vute
            "wal_Latn"  # Wolaytta
            "wan_Latn"  # Wan
            "wci_Latn"  # Gbe, Waci
            "wib_Latn"  # Toussian, Southern
            "wja_Latn"  # Waja
            "wji_Latn"  # Warji
            "wmw_Latn"  # Mwani
            "wo_Latn"  # Wolof
            "wob_Latn"  # Wè Northern
            "wwa_Latn"  # Waama
            "xed_Latn"  # Hdi
            "xh_Latn"  # Xhosa
            "xog_Latn"  # Soga
            "xon_Latn"  # Konkomba
            "xrb_Latn"  # Karaboro, Eastern
            "xsm_Latn"  # Kasem
            "xsm_Latn_BF"  # Kasem
            "xuo_Latn"  # Kuo
            "xwe_Latn"  # Gbe, Xwela
            "yal_Latn"  # Yalunka
            "yam_Latn"  # Yamba
            "yao_Latn"  # Yao
            "yas_Latn"  # Nugunu
            "yat_Latn"  # Yambeta
            "yav_Latn"  # Yangben
            "yay_Latn"  # Agwagwune
            "yaz_Latn"  # Lokaa
            "yba_Latn"  # Yala
            "ybb_Latn"  # Yemba
            "yer_Latn"  # Tarok
            "yko_Latn"  # Yasa
            "yo_Latn"  # Yoruba
            "yre_Latn"  # Yaouré
            "zag_Latn"  # Zaghawa
            "zay_Latn"  # Zayse
            "zdj_Latn"  # Comorian, Ngazidja
            "ziw_Latn"  # Zigula
            "zne_Latn"  # Zande
            "zu_Latn"  # Zulu
        ],
    },
    "GF_Arabic_Core": {
        "script": "Arabic",
        "language_codes": [
            "ar_Arab",  # Arabic
            "fa_Arab",  # Persian
            "ur_Arab",  # Urdu
        ],
    },
    "GF_Arabic_Plus": {
        "script": "Arabic",
        "language_codes": [
            "ckb_Arab",  # Kurdish
            "ms_Arab",  # Malay
            "ps_Arab",  # Pashto
            "ps_Arab",  # Sindhi
            "ug_Arab",  # Uyghur
        ],
    },
}


def unicodes_per_glyphset(glyphset_name):
    character_set = set()
    # Read .nam file
    nam_path = os.path.join(os.path.dirname(__file__), "nam", f"{glyphset_name}.nam")
    if os.path.exists(nam_path):
        with open(nam_path, "r") as f:
            nam_stub_lines = f.readlines()
        for line in nam_stub_lines:
            unicode = line.split(" ")[0]
            if unicode.startswith("0x"):
                character_set.add(int(unicode[2:], 16))
    return list(sorted(character_set))
