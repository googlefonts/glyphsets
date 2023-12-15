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
