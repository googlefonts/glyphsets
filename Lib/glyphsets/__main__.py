import argparse
from glyphsets import GFGlyphData
from glyphsLib import GSFont
from defcon import Font


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

    update_db_parser = subparsers.add_parser("update-db")
    update_db_parser.add_argument("srcs", help="Source file to use", nargs="+")

    update_src_parser = subparsers.add_parser("update-srcs")
    update_src_parser.add_argument("--srcs", help="Source files to update", nargs="+", required=True)
    update_src_parser.add_argument("glyphset")

    filter_lists_parser = subparsers.add_parser("filter-lists")
    filter_lists_parser.add_argument("glyphset")
    filter_lists_parser.add_argument("out", help="output path")

    nam_file_parser = subparsers.add_parser("build-nam-file")
    nam_file_parser.add_argument("--glyphsets", nargs="+", required=True)
    nam_file_parser.add_argument("-o", "--out", help="output path")

    args = parser.parse_args()

    if args.command == "filter-lists":
        GFGlyphData.build_glyphsapp_filter_lists(args.glyphset, args.out)
    
    elif args.command == "update-srcs":
        srcs = [load_source(src) for src in args.srcs]
        for src in srcs:
            GFGlyphData.update_source_glyphset(src, args.glyphset)
            src.save()
    
    elif args.command == "update-db":
        srcs = [load_source(src) for src in args.srcs]
        GFGlyphData.update_db_from_sources(srcs)
        GFGlyphData.save()
    
    elif args.command == "build-nam-file":
        GFGlyphData.build_nam_file(args.glyphsets, args.out)


if __name__ == "__main__":
    main()
