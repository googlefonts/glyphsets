"""
Read all languages and regions from gflanguages and print out the languages that are supported
in Europe or Americas and have more than 5 million speakers.
"""

import gflanguages

regions = gflanguages.LoadRegions()
languages = gflanguages.LoadLanguages()

SPEAKERS = 5000000

if __name__ == "__main__":
    country_codes = set()

    # Go through countries and add them to the set if they are in Europe or Americas
    for country_code in regions:
        if set(regions[country_code].region_group).intersection(
            set(("Europe", "Americas"))
        ):
            country_codes.add(country_code)

    # Go through languages and add them to the set if they are in Europe or Americas
    language_codes = set()

    # Print languages if they are supported through the logic
    for language_code in sorted(languages.keys()):
        if (
            set(languages[language_code].region).intersection(country_codes)
            and languages[language_code].population > SPEAKERS
            and languages[language_code].script == "Latn"
        ):
            if not languages[language_code].exemplar_chars:
                print(
                    f"WARNING, {languages[language_code].name} has no character defintions."
                )
            language_codes.add(language_code)
            print(f"  - {language_code}  # {languages[language_code].name}")
