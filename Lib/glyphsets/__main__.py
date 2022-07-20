import argparse
from glyphsets import GFGlyphData
from glyphsLib import GSFont
from defcon import Font
from fontTools.ttLib import TTFont


def load_source(fp):
    if fp.endswith(".glyphs"):
        src = GSFont(fp)
    elif fp.endswith(".ufo"):
        src = Font(fp)
    else:
        raise NotImplementedError()
    return src


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command", required=True)

    update_db_parser = subparsers.add_parser(
        "update-db",
        help="Update the database by using the glyphsets from source files.",
    )
    update_db_parser.add_argument("srcs", help="Source file to use", nargs="+")

    update_src_parser = subparsers.add_parser(
        "update-srcs", help="Add missing glyphs to font source."
    )
    update_src_parser.add_argument(
        "--srcs", help="Source files to update", nargs="+", required=True
    )
    update_src_parser.add_argument("glyphsets", nargs="+")

    filter_lists_parser = subparsers.add_parser(
        "filter-list", help="Ouput Glyphs.app filter from given glyphset(s)."
    )
    filter_lists_parser.add_argument("glyphsets", nargs="+")
    filter_lists_parser.add_argument("--prod-names", action="store_true", default=False)
    filter_lists_parser.add_argument("-o", "--out", required=True, help="output path")

    nam_file_parser = subparsers.add_parser(
        "nam-file", help="Ouput .nam file from given glyphset(s)."
    )
    nam_file_parser.add_argument("glyphsets", nargs="+")
    nam_file_parser.add_argument("-o", "--out", required=True, help="output path")

    font_file_parser = subparsers.add_parser(
        "missing-in-font",
        help="Report missing glyphs in font binary needed to cover glyphsets.",
    )
    font_file_parser.add_argument("font", help="Path for font binary")
    font_file_parser.add_argument(
        "-t",
        "--threshold",
        help="Show missing glyphs if glyph count is greater than",
        default=0.8,
        type=float,
    )
    args = parser.parse_args()

    if args.command == "filter-list":
        GFGlyphData.build_glyphsapp_filter_list(
            args.glyphsets, args.prod_names, args.out
        )

    elif args.command == "update-srcs":
        srcs = [load_source(src) for src in args.srcs]
        for src in srcs:
            GFGlyphData.update_source_glyphset(src, args.glyphsets)
            src.save()

    elif args.command == "update-db":
        srcs = [load_source(src) for src in args.srcs]
        GFGlyphData.update_db_from_sources(srcs)
        GFGlyphData.save()

    elif args.command == "nam-file":
        GFGlyphData.build_nam_file(args.glyphsets, args.out)

    elif args.command == "missing-in-font":
        ttFont = TTFont(args.font)
        missing = GFGlyphData.missing_glyphsets_in_font(ttFont, args.threshold)
        if not missing:
            print("No missing glyphs from glyph sets")
        else:
            for k, v in missing.items():
                if v:
                    print(f"{k} Missing glyphs:")
                    print("\n".join([f"  {i['nice_name']}" for i in v]))
                    print()
        print(
            "Please note: Unencoded glyphs may be falsely reported due "
            "to the glyph names in the font using a custom naming schema!"
        )


if __name__ == "__main__":
    main()
