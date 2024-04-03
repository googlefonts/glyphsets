"""
GF Glyph Database
"""

import yaml
import plistlib
import os
import gflanguages
from fontTools.unicodedata.Scripts import NAMES as SCRIPT_NAMES
import copy
import json
import logging

try:
    from ._version import version as __version__  # type: ignore
except ImportError:
    __version__ = "0.0.0+unknown"


DATA_FP = os.path.join(os.path.dirname(__file__), "data.json")
TEST_STRINGS_DATA = os.path.join(os.path.dirname(__file__), "test_strings.json")
log = logging.getLogger(__file__)
data = json.load(open(DATA_FP, encoding="utf8"))


class _GFGlyphData:
    def __init__(self, data=data):
        self._data = copy.copy(data)
        self._in_use = set(g["nice_name"] for g in self._data["glyphs"])

    def save(self, fp=DATA_FP):
        with open(fp, "w") as db:
            json.dump(self._data, db, indent=2)

    @classmethod
    def from_json(cls, fp):
        with open(fp) as db:
            data = json.load(db)
            return cls(data)

    def __getitem__(self, k):
        return self._data[k]

    def glyphsets_in_font(self, ttFont):
        glyphs_in_font = set(ttFont.getGlyphOrder())
        unicodes_in_font = set(ttFont.getBestCmap().keys())
        res = {}
        for g in self["glyphs"]:
            for glyphset in g["glyphsets"]:
                if glyphset not in res:
                    res[glyphset] = {"has": [], "missing": []}
                if any(
                    [
                        g["nice_name"] in glyphs_in_font,
                        g["production_name"] in glyphs_in_font,
                        g["unicode"] in unicodes_in_font,
                    ]
                ):
                    res[glyphset]["has"].append(g)
                else:
                    res[glyphset]["missing"].append(g)
        return res

    def glyphsets_fulfilled(self, ttFont):
        res = self.glyphsets_in_font(ttFont)
        return {
            k: len(v["has"]) / (len(v["has"]) + len(v["missing"]))
            for k, v in res.items()
        }

    def missing_glyphsets_in_font(self, ttFont, threshold=0.8):
        res = self.glyphsets_in_font(ttFont)
        fulfilled = {
            k: len(v["has"]) / (len(v["has"]) + len(v["missing"]))
            for k, v in res.items()
        }
        missing = {}
        for k, v in fulfilled.items():
            if v == 1.0 or v < threshold:
                continue
            missing[k] = res[k]["missing"]
        return missing

    def glyphs_in_glyphsets(self, glyphsets):
        res = []
        seen = set()
        for g in self["glyphs"]:
            for glyphset in g["glyphsets"]:
                if glyphset not in glyphsets or g["nice_name"] in seen:
                    continue
                res.append(g)
                seen.add(g["nice_name"])
        return res


# def update_db_from_sources(self, sources):
#     """Update the database by using the glyphsets from source files.

#     Please note that you may need to edit some data by hand"""
#     for src in sources:
#         if isinstance(src, GSFont):
#             glyphset = os.path.basename(src.filepath).split(".")[0]
#             for g in src.glyphs:
#                 if not g.export:
#                     continue
#                 self.add_glyph(glyphset, g.name, unicodes=g.unicode)
#         elif isinstance(src, Font):
#             glyphset = os.path.basename(src.path).split(".")[0]
#             for g in src:
#                 self.add_glyph(glyphset, g.name, unicodes=g.unicode)
#         else:
#             raise NotImplementedError(f"{src} not supported yet!")

# def add_glyph(self, glyphset, nice_name=None, unicodes=None):
#     if nice_name in self._in_use:
#         entry = next(
#             (g for g in self._data["glyphs"] if g["nice_name"] == nice_name), None
#         )
#         if glyphset in entry["glyphsets"]:
#             log.warning(f"Skipping {glyphset}.{nice_name}. Already exists!")
#             return
#         entry["glyphsets"].append(glyphset)
#     else:
#         # glyphsapp use hex strings for the unicode val. Convert these to ints
#         if unicodes:
#             uni_char = unicodes if isinstance(unicodes, int) else int(unicodes, 16)
#             character = chr(uni_char)
#         else:
#             uni_char = None
#             character = None
#         glyphslib_data = get_glyph(nice_name)
#         glyphslib_unicode = (
#             None if not glyphslib_data.unicode else int(glyphslib_data.unicode, 16)
#         )
#         self._data["glyphs"].append(
#             {
#                 "nice_name": nice_name,
#                 "production_name": glyphslib_data.production_name,
#                 "character": character,
#                 "unicode": uni_char or glyphslib_unicode,
#                 "glyphsets": [glyphset],
#             }
#         )
#         self._in_use.add(nice_name)

# def get_glyph(self, nice_name=None, production_name=None, character=None, uni=None):
#     if nice_name:
#         return next(
#             (g for g in self._data["glyphs"] if g["nice_name"] == nice_name), None
#         )
#     elif production_name:
#         return next(
#             (
#                 g
#                 for g in self._data["glyphs"]
#                 if g["production_name"] == production_name
#             ),
#             None,
#         )
#     elif character:
#         return next(
#             (g for g in self._data["glyphs"] if g["character"] == character), None
#         )
#     elif uni:
#         return next((g for g in self._data["glyphs"] if g["unicode"] == uni), None)
#     return None

# def build_glyphsapp_filter_list(
#     self, glyphsets, use_production_names=False, out=None
# ):
#     """Build filter lists"""
#     glyphs = self.glyphs_in_glyphsets(glyphsets)
#     if out and out.endswith("plist"):
#         # glyphsapp need a prefix for the out file of "CustomFilter"
#         if not os.path.basename(out).startswith("CustomFilter"):
#             print(
#                 "Prefixing 'CustomFilter' to out path since file is intended for Glyphsapp"
#             )
#             out = os.path.join(
#                 os.path.dirname(out), "CustomFilter" + os.path.basename(out)
#             )
#         res = {k: [] for k in glyphsets}
#         for glyphset in glyphsets:
#             for glyph in glyphs:
#                 if glyphset in glyph["glyphsets"]:
#                     if use_production_names:
#                         res[glyphset].append(glyph["production_name"])
#                     else:
#                         res[glyphset].append(glyph["nice_name"])

#         res = [{"name": k, "list": v} for k, v in res.items()]
#         res = [plistlib.dumps(res).decode("utf-8")]
#     else:
#         if use_production_names:
#             res = [g["production_name"] for g in glyphs]
#         else:
#             res = [g["nice_name"] for g in glyphs]

#     if out:
#         with open(out, "w") as doc:
#             doc.write("\n".join(res))
#     return res

# def build_nam_file(self, glyphsets, out=None):
#     "Build GF nam files from glyphsets"
#     glyphs = [g for g in self.glyphs_in_glyphsets(glyphsets) if g["unicode"]]
#     res = []
#     for glyph in glyphs:
#         code = (
#             "0x" + hex(ord(glyph["character"])).replace("0x", "").zfill(4).upper()
#         )
#         res.append(f"{code} {uni.name(glyph['character'])}")
#     res.sort()
#     if out:
#         with open(out, "w") as doc:
#             doc.write("\n".join(res))
#     return res

# def update_source_glyphset(self, src, glyphsets):
#     """Add glyphs to a source file"""
#     glyphs = self.glyphs_in_glyphsets(glyphsets)
#     if isinstance(src, Font):
#         glyphs_in_font = set(g.name for g in src)
#         for glyph in glyphs:
#             if glyph["nice_name"] in glyphs_in_font:
#                 continue
#             new_glyph = src.newGlyph(glyph["nice_name"])
#             new_glyph.color = "Red"
#             glyphs_in_font.add(glyph["nice_name"])
#     elif isinstance(src, GSFont):
#         glyphs_in_font = set(g.name for g in src.glyphs)
#         for glyph in glyphs:
#             if glyph["nice_name"] in glyphs_in_font:
#                 continue
#             new_glyph = GSGlyph(glyph["nice_name"])
#             new_glyph.color = 1
#             src.glyphs.append(new_glyph)
#             glyphs_in_font.add(glyph["nice_name"])
#     else:
#         raise NotImplementedError(f"Cannot add glyphs font source not supported!")

# def build_fea(self, glyphset):
#     """Generate a .fea file based on a glyphset"""
#     # TODO this is 2022 Q3/4 goal
#     raise NotImplementedError()


GFGlyphData = _GFGlyphData()


class _TestDocData:
    def __init__(
        self,
        data=json.load(open(TEST_STRINGS_DATA, encoding="utf8")),
        glyphsets=GFGlyphData,
    ):
        self._data = data
        self._glyphsets = glyphsets

    def test_strings_in_font(self, ttFont, threshold=0.95):
        res = {}
        glyphsets_in_font = self._glyphsets.glyphsets_fulfilled(ttFont)
        for glyphset, coverage in glyphsets_in_font.items():
            if coverage < threshold:
                continue
            test_strings = self._data.get(glyphset)
            if not test_strings:
                continue
            res[glyphset] = test_strings
        return res


GFTestData = _TestDocData()


## NEW SYSTEM:

root_folder = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "data")
)


def read_nam_file(path):
    character_set = set()
    with open(path, "r") as f:
        nam_lines = f.readlines()
    for line in nam_lines:
        unicode = line.split(" ")[0]
        if unicode.startswith("0x"):
            character_set.add(int(unicode[2:], 16))
    return list(sorted(character_set))


def build_glyphsapp_filter_list(glyphsets, out, use_production_names=False):
    """Build filter lists"""
    glyphsets = sorted(glyphsets)

    if not out.endswith(".plist"):
        raise ValueError("Only .plist files are supported")

    # glyphsapp need a prefix for the out file of "CustomFilter"
    if not os.path.basename(out).startswith("CustomFilter"):
        print(
            "Prefixing 'CustomFilter' to out path since file is intended for Glyphsapp"
        )
        out = os.path.join(os.path.dirname(out), "CustomFilter" + os.path.basename(out))

    # Make .plist
    plist = []

    for glyphset_name in glyphsets:
        plist.append(
            {
                "name": glyphset_name,
                "list": glyphs_in_glyphset(glyphset_name, use_production_names),
            }
        )

    with open(out, "wb") as f:
        plistlib.dump(plist, f)
        print("Wrote", out)


regions = gflanguages.LoadRegions()
languages = gflanguages.LoadLanguages()


def defined_glyphsets():
    definitions_path = os.path.join(os.path.dirname(__file__), "definitions")
    yaml_files = [
        os.path.splitext(f)[0]
        for f in os.listdir(definitions_path)
        if os.path.isfile(os.path.join(definitions_path, f)) and f.endswith(".yaml")
    ]
    return sorted(yaml_files)


def get_script(glyphset_name):
    return glyphset_name.split("_")[1]


def defined_scripts():
    scripts = set()
    for glyphset_name in defined_glyphsets():
        scripts.update([get_script(glyphset_name)])
    return sorted(list(scripts))


def glyphsets_per_script(script):
    glyphsets = []
    for glyphset_name in defined_glyphsets():
        if get_script(glyphset_name) == script:
            glyphsets.append(glyphset_name)
    return glyphsets


def get_glyphset_definition(glyphset_name):
    yaml_path = os.path.join(
        os.path.dirname(__file__), "definitions", f"{glyphset_name}.yaml"
    )
    with open(yaml_path, "r", encoding="utf8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def unicodes_per_glyphset(glyphset_name):
    # Read .nam file
    nam_path = os.path.join(
        os.path.dirname(__file__),
        "results",
        "nam",
        f"{glyphset_name}.nam",
    )
    if os.path.exists(nam_path):
        return read_nam_file(nam_path)


def glyphs_in_glyphsets(glyphset_names, production_names=False):
    glyphs = set()
    for glyphset_name in glyphset_names:
        glyphs.update(glyphs_in_glyphset(glyphset_name, production_names))

    return sorted(list(glyphs))


def glyphs_in_glyphset(glyphset_name, production_names=False):
    script = glyphset_name.split("_")[1]

    with open(
        os.path.join(
            root_folder,
            "results",
            "txt",
            "prod-names" if production_names else "nice-names",
            f"{glyphset_name}.txt",
        ),
        "r",
    ) as f:
        glyph_names = [
            line.strip() for line in f.readlines() if not line.startswith("#")
        ]

    return sorted(glyph_names)


def languages_per_glyphset(glyphset_name):

    script = get_script(glyphset_name)
    glyphset_definition = get_glyphset_definition(glyphset_name)
    language_codes = glyphset_definition.get("language_codes", [])
    regions = glyphset_definition.get("regions")
    use_aux = glyphset_definition.get("use_auxiliary", False)
    historical = glyphset_definition.get("historical", False)
    population = glyphset_definition.get("population", False)
    exclude_language_codes = glyphset_definition.get("exclude_language_codes", set())

    # Assemble character sets from gflanguages
    languages = gflanguages.LoadLanguages()
    if regions:
        for language in languages.values():
            if language.id in exclude_language_codes:
                continue
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


def add_country(code):
    if code in regions:
        return f"{regions[code].name} ({code})"
    return code


def add_language(code):
    if code in languages:
        return f"{languages[code].name} ({code})"
    return code


def description_per_glyphset(glyphset_name):
    script = get_script(glyphset_name)
    glyphset_definition = get_glyphset_definition(glyphset_name)
    language_codes = glyphset_definition.get("language_codes", [])
    regions = glyphset_definition.get("regions")
    use_aux = glyphset_definition.get("use_auxiliary", False)
    historical = glyphset_definition.get("historical", False)
    population = glyphset_definition.get("population", False)
    description = glyphset_definition.get("description", None)

    glyphs_stub_path = os.path.join(
        root_folder, "definitions", "per_glyphset", f"{glyphset_name}.stub.glyphs"
    )

    warning = False
    md = ""

    md += f"# {glyphset_name.replace('_', ' ')}\n\n"
    if description:
        md += (
            "> _Description partially salvaged from old README, so languages manually listed here (if any) may be outdated or irrelevant and need to be replaced by language code lists:_\n> \n> "
            + "\n> ".join(description.split("\n"))
            + "\n\n"
        )
    if regions:
        md += f"`{glyphset_name}` is **dynamically** defined [here](/Lib/glyphsets/definitions/{glyphset_name}.yaml) as:\n\n"
    else:
        md += f"`{glyphset_name}` is **statically** defined [here](/Lib/glyphsets/definitions/{glyphset_name}.yaml) as:\n\n"
    md += f"* Script: {script}\n"
    if os.path.exists(glyphs_stub_path):
        md += f"* Characters and glyphs defined in [{os.path.basename(glyphs_stub_path)}](/data/definitions/per_glyphset/{os.path.basename(glyphs_stub_path)})\n"
    for language_code in language_codes:
        lang_stub_path = os.path.join(
            root_folder, "definitions", "per_language", f"{language_code}.stub.glyphs"
        )
        if os.path.exists(lang_stub_path):
            md += f"* Characters and glyphs defined in [{os.path.basename(lang_stub_path)}](/data/definitions/per_language/{os.path.basename(lang_stub_path)})\n"
    if regions:
        md += (
            "* All languages of the countries `\n"
            + ",\n".join(sorted(map(add_country, regions)))
            + "\n`\n"
        )
    if population:
        md += f"* With a population of over {population} speakers\n"
    if historical:
        md += "* Including historical languages\n"
    if use_aux:
        md += "* Including auxiliary characters\n"

    if regions and language_codes:
        md += (
            "* Additionally, the following languages are defined **statically**: `\n"
            + ",\n".join(sorted(map(add_language, language_codes)))
            + "\n`\n"
        )
    elif not regions and language_codes:
        md += (
            "* List of languages: `\n"
            + ",\n".join(sorted(map(add_language, language_codes)))
            + "\n`\n"
        )
    elif not regions and not language_codes:
        md += f"\n> [!CAUTION]  \n> Since this glyphset has no defined languages, it can't be checked via Fontbakery's `shape_languages` check.\n> Please add language code definions [here](/Lib/glyphsets/definitions/{glyphset_name}.yaml).\n"
        warning = True

    md += "\n"

    if regions:
        _languages_per_glyphset = languages_per_glyphset(glyphset_name)
        md += (
            f"\nThe following list of **{len(_languages_per_glyphset)}** languages is computed as a result of the dynamic conditions described above:\n\n`\n"
            + ",\n".join(sorted(map(add_language, _languages_per_glyphset)))
            + "\n`\n\n"
        )

    md += f"The resulting glyphset can be found here: [.nam](/data/results/nam/{glyphset_name}.nam) (only encoded characters), [.glyphs](/data/results/glyphs/{glyphset_name}.glyphs)/[.txt (nice names)](/data/results/txt/nice-names/{glyphset_name}.txt)/[.txt (production names)](/data/results/txt/prod-names/{glyphset_name}.txt) (all glyphs), as well as part of [CustomFilter_GF_{script}.plist](/data/results/plist/CustomFilter_GF_{script}.plist)\n\n"
    return md, warning


def get_glyphsets_fulfilled(ttFont):
    """Returns a dictionary of glyphsets that are fulfilled by the font,
    and the percentage of glyphs in the font that are in the glyphset.
    This is following the new glyphset definitions in glyphsets
    """

    res = {}
    unicodes_in_font = set(ttFont.getBestCmap().keys())
    for glyphset in defined_glyphsets():
        unicodes_in_glyphset = unicodes_per_glyphset(glyphset)
        if glyphset not in res:
            res[glyphset] = {"has": [], "missing": [], "percentage": 0}
        for unicode in unicodes_in_glyphset:
            if unicode in unicodes_in_font:
                res[glyphset]["has"].append(unicode)
            else:
                res[glyphset]["missing"].append(unicode)
        if unicodes_in_glyphset:
            res[glyphset]["percentage"] = len(res[glyphset]["has"]) / len(
                unicodes_in_glyphset
            )
        else:
            res[glyphset]["percentage"] = 0
    return res


if __name__ == "__main__":
    print(defined_scripts())
