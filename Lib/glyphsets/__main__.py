import argparse
from glyphsets import build_glyphsapp_filter_list, compare_glyphsets, analyze_font
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

    # PROCESS
    args = parser.parse_args()

    if args.command == "filter-list":
        build_glyphsapp_filter_list(args.glyphsets, args.out, args.prod_names)

    if args.command == "compare":
        compare_glyphsets(args.glyphsets)

    if args.command == "coverage":
        analyze_font(TTFont(args.font))


if __name__ == "__main__":
    main()
