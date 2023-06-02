"""
Browse through all gflanguages and find the input character.

Syntax:
python scripts/find_language_for_character.py <character>
(<character> can be either a single 0x0000 string or unicode character.)

Please manually install tabulate if not present: pip install tabulate
"""

import sys
import gflanguages
import sys
import tabulate
import unicodedata

regions = gflanguages.LoadRegions()
languages = gflanguages.LoadLanguages()

# print(regions)

if __name__ == "__main__":
    input_character = sys.argv[-1]
    if input_character.startswith("0x"):
        input_character = chr(int(input_character, 16))
    unicode_string = f"{ord(input_character):#0{6}X}".replace("0X", "0x")
    print(
        f"Character: {input_character}  ({unicode_string} {unicodedata.name(input_character)})"
    )

    found_languages = []

    # Read language definitions
    for lang_code in languages:
        lang = languages[lang_code]
        if lang.exemplar_chars:
            chars = lang.exemplar_chars
            for category in ("base", "index", "marks", "numerals", "punctuation"):
                if (
                    input_character in getattr(chars, category)
                    or input_character in getattr(chars, category).upper()
                ):
                    # Find regions
                    found_regions = set()
                    for country_code in regions:
                        if country_code in lang.region:
                            found_regions.update(
                                set(regions[country_code].region_group)
                            )

                    found_languages.append(
                        (
                            lang_code,
                            lang.name,
                            category,
                            lang.population,
                            lang.script,
                            ", ".join(list(found_regions)),
                        )
                    )

    found_languages = sorted(found_languages, key=lambda x: x[3], reverse=True)
    print(
        tabulate.tabulate(
            found_languages,
            headers=["Language", "Name", "Category", "Speakers", "Script", "Regions"],
        )
    )
