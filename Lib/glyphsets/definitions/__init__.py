# Google Fonts glyphset definitions to be consumed by other tools.
# The "script" value needs to correspond to the folder name
# in /GF_Glyphsets of this repo in order to find the other definition files.

import os
import gflanguages
from fontTools.unicodedata.Scripts import NAMES as SCRIPT_NAMES

glyphset_definitions = {
    "GF_Latin_Kernel": {"script": "Latin"},
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
        "historical": False,
        "population": 1,
        "regions": "AO BF BI BJ BW CD CF CG CI CM CV DJ DZ EA EG EH ER ET GA "
        "GH GM GN GQ GW IC IO KE KM LR LS LY MA MG ML MR MU MW MZ "
        "NA NE NG RE RW SC SD SH SL SN SO SS ST SZ TD TF TG TN TZ "
        "UG YT ZA ZM ZW ".split(),
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


def languages_per_glyphset(glyphset_name):

    script = glyphset_definitions[glyphset_name]["script"]
    language_codes = glyphset_definitions[glyphset_name].get("language_codes", [])
    regions = glyphset_definitions[glyphset_name].get("regions")
    use_aux = glyphset_definitions[glyphset_name].get("use_auxiliary", False)
    historical = glyphset_definitions[glyphset_name].get("historical", False)
    population = glyphset_definitions[glyphset_name].get("population", False)

    # Assemble character sets from gflanguages
    languages = gflanguages.LoadLanguages()
    if regions:
        for language in languages.values():
            if not historical and language.historical:
                continue
            if population > language.population:
                continue
            if (
                set(language.region).intersection(set(regions))
                and SCRIPT_NAMES[language.script] == script
            ):
                language_codes.append(language.id)

    return language_codes


def description_per_glyphset(glyphset_name):
    script = glyphset_definitions[glyphset_name]["script"]
    language_codes = glyphset_definitions[glyphset_name].get("language_codes", [])
    regions = glyphset_definitions[glyphset_name].get("regions")
    use_aux = glyphset_definitions[glyphset_name].get("use_auxiliary", False)
    historical = glyphset_definitions[glyphset_name].get("historical", False)
    population = glyphset_definitions[glyphset_name].get("population", False)

    warning = False
    md = ""

    md += f"## {glyphset_name.replace('_', ' ')}\n\n"
    if regions:
        md += f"{glyphset_name} is defined **in code** as:\n\n"
    else:
        md += f"{glyphset_name} is **manually** defined as:\n\n"
    md += f"* Script: {script}\n"
    if regions:
        md += f"* All languages of the countries `{', '.join(regions)}`\n"
    if population:
        md += f"* With a population of over {population} speakers\n"
    if historical:
        md += "* Including historical languages\n"
    if use_aux:
        md += "* Including auxiliary characters\n"

    if regions and language_codes:
        md += f"* Additionally, the following languages are defined **manually**: `{', '.join(language_codes)}`\n"
    elif not regions and language_codes:
        md += f"* List of languages: `{', '.join(language_codes)}`\n"
    elif not regions and not language_codes:
        md += "\n:warning: Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check. Please add language code definions here.\n"
        warning = True

    md += "\n"

    if regions:
        md += f"\nThe following list of languages is computed as a result of the conditions described above:\n\n`{', '.join(languages_per_glyphset(glyphset_name))}`\n\n"

    md += f"The resulting glyphset can be found here: [{glyphset_name}.nam](/Lib/glyphsets/definitions/nam/{glyphset_name}.nam)\n\n"
    return md, warning


if __name__ == "__main__":
    for key in glyphset_definitions:
        print(description_per_glyphset(key))
