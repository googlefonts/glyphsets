"""
Read all languages and regions from gflanguages and print out the languages that are supported
in Europe or Americas and have more than 5 million speakers.
"""

import argparse
import gflanguages

SPEAKERS = 5000000


def main(args):
    arg_parser = argparse.ArgumentParser(
        description="Generates a list of language ids based on given requirements."
    )
    arg_parser.add_argument(
        "--regions", nargs="+", help="Region or region groups where languages are used."
    )
    arg_parser.add_argument(
        "--population", help="Minimum speakers’ population.", default=SPEAKERS
    )
    arg_parser.add_argument("--script", help="Script of the languages.")
    arg_parser.add_argument(
        "--include-languages",
        nargs="+",
        default=[],
        help="Languages that should be included even if they don’t match the other requirements.",
    )
    options = arg_parser.parse_args(args)
    options.population = int(options.population)

    regions = gflanguages.LoadRegions()
    languages = gflanguages.LoadLanguages()

    country_codes = set()

    # Go through countries and add them to the set if their region_group is in options.regions or they are in options.regions
    for country_code in regions:
        if set(regions[country_code].region_group).intersection(
            set(options.regions)
        ) or (country_code in options.regions):
            country_codes.add(country_code)

    # Go through languages and add them to the set if their regions are in country_codes
    language_codes = set()

    # Print languages if they are supported through the logic
    for language_code in sorted(languages.keys()):
        if (
            language_code in options.include_languages
            or set(languages[language_code].region).intersection(country_codes)
            and languages[language_code].population >= options.population
            and languages[language_code].script == options.script
        ):
            if not languages[language_code].exemplar_chars:
                print(
                    f"WARNING, {languages[language_code].name} has no character defintions."
                )
            language_codes.add(language_code)
            print(f"  - {language_code}  # {languages[language_code].name}")


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
