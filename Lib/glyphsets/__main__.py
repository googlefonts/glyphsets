import argparse
from glyphsets import build_glyphsapp_filter_list, compare_glyphsets, analyze_font, find_character, GlyphSet
from fontTools.ttLib import TTFont


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Filter List
    filter_lists_parser = subparsers.add_parser("filter-list", help="Ouput Glyphs.app filter from given glyphset(s).")
    filter_lists_parser.add_argument("glyphsets", nargs="+")
    filter_lists_parser.add_argument("--prod-names", action="store_true", default=False)
    filter_lists_parser.add_argument("-o", "--out", required=True, help="output path")

    # Compare
    compare_parser = subparsers.add_parser(
        "compare",
        help="Compare two or more glyhsets to each other; with later glyphsets being compared to the former.",
    )
    compare_parser.add_argument("glyphsets", nargs="+")

    # Analyze
    analyze_parser = subparsers.add_parser(
        "coverage",
        help="Analyze glyphsets covered by a font binary.",
    )
    analyze_parser.add_argument("font", help="Font binary to analyze")

    # Find character
    find_parser = subparsers.add_parser(
        "find",
        help="Find a character in the language definitions and glyphsets.",
    )
    find_parser.add_argument("character", help="0xABCD hex string or Unicode character")

    # Print unicodes
    printunicodes_parser = subparsers.add_parser(
        "print-unicodes",
        help="Print comma-separated list of unicodes for given glyphsets, to be used for subsetting",
    )
    printunicodes_parser.add_argument(
        "-s", "--separator", dest="separator", help="List separator, default is `,`", default=","
    )
    printunicodes_parser.add_argument(
        "-d", "--decorator", dest="decorator", help="Hex Unicode decorator, default is U+", default="U+"
    )
    printunicodes_parser.add_argument("glyphsets", nargs="+", help="List of glyphset names")

    # PROCESS
    args = parser.parse_args()

    if args.command == "filter-list":
        build_glyphsapp_filter_list(args.glyphsets, args.out, args.prod_names)

    if args.command == "compare":
        compare_glyphsets(args.glyphsets)

    if args.command == "coverage":
        analyze_font(TTFont(args.font))

    if args.command == "find":
        find_character(args.character)

    if args.command == "print-unicodes":
        unicodes = set()
        for glyphset in args.glyphsets:
            unicodes.update(set(GlyphSet.load(glyphset).get_final_unicodes()))

        print(args.separator.join([f"{args.decorator}{unicode}" for unicode in unicodes]))


if __name__ == "__main__":
    main()
