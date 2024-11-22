import copy
import yaml
import plistlib
import os
import gflanguages
from fontTools.unicodedata.Scripts import NAMES as SCRIPT_NAMES
import unicodedata
import functools
from glyphsets.helpers import Colors, headline
import tabulate
import glyphsLib
import youseedee
import random

from glyphsLib.glyphdata import get_glyph, _lookup_attributes_by_unicode

# Call get_glyph once so that GLYPHDATA gets filled in glyphsLib
get_glyph("A")
# If I import GLYPHDATA at the top of the file, it doesn't get filled
from glyphsLib.glyphdata import GLYPHDATA  # noqa E402

assert type(GLYPHDATA) is glyphsLib.glyphdata.GlyphData

root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data"))
tool_folder = os.path.abspath(os.path.dirname(__file__))


def sort_unicodes_by_name(a, b):
    glyph_a = get_glyph(a)
    glyph_b = get_glyph(b)
    if glyph_a.unicode and glyph_b.unicode:
        return int(glyph_a.unicode, 16) - int(glyph_b.unicode, 16)
    elif glyph_a.unicode:
        return -1
    elif glyph_b.unicode:
        return 1
    else:
        return 0


# def sort_unicodes_by_glyphobject(a, b):
#     if a.unicode and b.unicode:
#         return int(a.unicode, 16) - int(b.unicode, 16)
#     elif a.unicode:
#         return -1
#     elif b.unicode:
#         return 1
#     else:
#         return 0


def sort_by_category(a, b):
    info_a = get_glyph(a.name if hasattr(a, "name") else a)
    info_b = get_glyph(b.name if hasattr(b, "name") else b)

    if info_a.category is None:
        return -1
    elif info_b.category is None:
        return 1

    value = sorted([info_a.category, info_b.category]).index(info_a.category)
    if value == 0:
        value = -1
    value *= -1

    return value


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
        print("Prefixing 'CustomFilter' to out path since file is intended for Glyphsapp")
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


REGIONS = gflanguages.LoadRegions()
LANGUAGES = gflanguages.LoadLanguages()
glyphset_cache = {}


class GlyphSet(object):

    @classmethod
    def load(cls, name, reload=False):
        """
        Class factory method to load a glyphset by name.
        Can later be altered to return different classes based on modifiers."""

        global glyphset_cache

        if reload:
            glyphset_cache = {}

        if name in glyphset_cache:
            return glyphset_cache[name]
        else:
            glyphset = cls(name)
            glyphset_cache[name] = glyphset
            return glyphset

    def __init__(self, name):
        if " " in name:
            self.name = name.split(" ")[0]
            name_length = len(self.name) + 1
            self.modifier = name[name_length:]
        else:
            self.name = name
            self.modifier = None

        # Read definition
        yaml_path = os.path.join(os.path.dirname(__file__), "definitions", f"{self.name}.yaml")
        with open(yaml_path, "r", encoding="utf8") as f:
            self.definition = yaml.load(f, Loader=yaml.FullLoader)

        # Read definitions and set defaults
        self.description = self.definition.get("description", None)
        self.language_codes = self.definition.get("language_codes", [])
        self.exclude_language_codes = self.definition.get("exclude_language_codes", set())
        self.regions = self.definition.get("regions", [])
        self.use_aux = self.definition.get("use_auxiliary", False)
        self.historical = self.definition.get("historical", False)
        self.population = self.definition.get("population", False)
        self.include_glyphsets = self.definition.get("include_glyphsets", [])

        self.script = get_script(self.name)

    def complete_name(self):
        if self.modifier:
            return f"{self.name} {self.modifier}"
        else:
            return self.name

    def __str__(self):
        return f"<GlyphSet {self.complete_name()}>"

    def get_included_glyphsets(self):
        """Compute list of all included glyphsets"""

        included_glyphsets = copy.copy(self.include_glyphsets)

        for glyphset in self.include_glyphsets:
            for glyphset_name in GlyphSet.load(glyphset).get_included_glyphsets():
                if glyphset_name not in included_glyphsets:
                    included_glyphsets.append(glyphset_name)

        if included_glyphsets:
            included_glyphsets = reversed(included_glyphsets)

        return list(included_glyphsets)

    def get_extended_glyphsets(self):
        """Compute list of dynamically spawned glyphsets"""

        extended_glyphsets = []

        # Glyphsets that contain just glyphs exclusive to this set in case of inheritances
        if self.get_included_glyphsets():
            extended_glyphsets.append(self.name + " Exclusive")

        # Cyrillic Roman/Italic variants
        if self.script == "Cyrillic" and GlyphSet.load(f"{self.name} Roman Localizations").get_final_glyphnames():
            extended_glyphsets.append(f"{self.name} Roman Localizations")
        if self.script == "Cyrillic" and GlyphSet.load(f"{self.name} Italic Localizations").get_final_glyphnames():
            extended_glyphsets.append(f"{self.name} Italic Localizations")

        return extended_glyphsets

    def get_language_codes(self):
        """Compute the language codes for this glyphset"""

        language_codes = copy.copy(self.language_codes)

        # Include glyphset dependencies
        for glyphset in self.include_glyphsets:
            for language_code in GlyphSet.load(glyphset).get_language_codes():
                if language_code not in language_codes:
                    language_codes.append(language_code)

        # Assemble character sets from gflanguages
        if self.regions:
            for language in LANGUAGES.values():
                if language.id in self.exclude_language_codes:
                    continue
                if not self.historical and language.historical:
                    continue
                if self.population > language.population:
                    continue
                if (
                    set(language.region).intersection(set(self.regions))
                    and SCRIPT_NAMES[language.script] == self.script
                ):
                    language_codes.append(language.id)

        return language_codes

    def get_characters(self):
        """Compute list of characters for this glyphset"""

        character_set = set()

        for language_code in self.get_language_codes():
            chars = LANGUAGES[language_code].exemplar_chars
            # chars.base.upper() is important because many Latin languages don't
            # contain a complete set of uppercase letters in "index"
            # Filter for control characters and format characters
            character_set.update(
                {
                    ord(c)
                    for c in list(
                        set(chars.base)
                        | set(chars.base.upper())
                        | set(chars.index)
                        | set(chars.marks)
                        | set(chars.numerals)
                        | set(chars.punctuation)
                        | (set(chars.auxiliary) if self.use_aux else set())
                    )
                    if (c not in (" ", "{", "}", "◌") and unicodedata.category(c) not in ("Cc", "Cf"))
                }
            )

        return list(sorted(character_set))

    def get_stub_characters(self):
        """Collect list of encoded characters from .stub.glyphs file"""

        character_set = []

        # Include glyphset dependencies
        for glyphset in self.include_glyphsets:
            for unicode in GlyphSet.load(glyphset).get_stub_characters():
                if unicode not in character_set:
                    character_set.append(unicode)

        glyphs_stub_path = os.path.join(root_folder, "definitions", "per_glyphset", f"{self.name}.stub.glyphs")
        if os.path.exists(glyphs_stub_path):
            font = get_glyphs_file(glyphs_stub_path)
            for glyph in font.glyphs:
                if glyph.unicodes:
                    for unicode in glyph.unicodes:
                        character_set.append(int(unicode, 16))

        return character_set

    def get_stub_glyph_objects(self):
        """Collect list of all glyphs from .stub.glyphs file"""

        glyph_set = []

        # Include glyphset dependencies
        for glyphset in self.include_glyphsets:
            for glyph in GlyphSet.load(glyphset).get_stub_glyph_objects():
                if glyph.name not in [g.name for g in glyph_set]:
                    glyph_set.append(glyph)

        glyphs_stub_path = os.path.join(root_folder, "definitions", "per_glyphset", f"{self.name}.stub.glyphs")
        if os.path.exists(glyphs_stub_path):
            font = get_glyphs_file(glyphs_stub_path)
            for glyph in font.glyphs:
                glyph_set.append(Glyph(glyph.name, glyph.unicode))

        return glyph_set

    def get_final_glyphs_font(self):
        """Collect list of all glyphs for this glyphset in a GSFont object"""

        if hasattr(self, "_final_glyphs_font"):
            return self._final_glyphs_font

        else:

            glyphs_empty_path = os.path.join(root_folder, "empty_font.glyphs")

            # Create or open glyphs file and add characters
            font = glyphsLib.load(glyphs_empty_path)
            font.familyName = self.name

            # Start assembly
            character_set = set(self.get_characters())
            character_set.update(set(self.get_stub_characters()))
            # glyph_set = self.get_stub_glyphs()

            # Call get_glyph once so that GLYPHDATA gets filled in glyphsLib
            get_glyph("A")
            # If I import GLYPHDATA at the top of the file, it doesn't get filled
            from glyphsLib.glyphdata import GLYPHDATA

            assert type(GLYPHDATA) is glyphsLib.glyphdata.GlyphData

            def _font_has_unicode(font, unicode):
                if type(unicode) is str:
                    unicode = int(unicode, 16)
                for glyph in font.glyphs:
                    if glyph.unicode:
                        if int(glyph.unicode, 16) == unicode:
                            return True

            def add_stub_glyphs(font, stub_path):
                stub_font = glyphsLib.load(stub_path)

                for glyph in stub_font.glyphs:

                    # Add encoded characters to character_set
                    if glyph.unicodes:
                        for unicode in glyph.unicodes:
                            character_set.update({int(unicode, 16)})

                    # Add to glyphs to .glyphs file
                    if (
                        glyph.unicode
                        and not _font_has_unicode(font, glyph.unicode)
                        or not glyph.unicode
                        and not font.glyphs[glyph.name]
                    ):
                        new_glyph = glyphsLib.GSGlyph(glyph.name)
                        if glyph.unicode:
                            new_glyph.unicode = glyph.unicodes[0]
                        font.glyphs.append(new_glyph)

            # Add language-specific glyphs
            for language_code in self.get_language_codes():
                stub_path = os.path.join(root_folder, "definitions", "per_language", f"{language_code}.stub.glyphs")
                if os.path.exists(stub_path):
                    add_stub_glyphs(font, stub_path)

            # Add script-specific glyphs
            stub_path = os.path.join(root_folder, "definitions", "per_script", f"{self.script}.stub.glyphs")
            if os.path.exists(stub_path):
                add_stub_glyphs(font, stub_path)

            # Add stub for all glyphsets
            stub_path = os.path.join(root_folder, "definitions", "all", "all.stub.glyphs")
            if os.path.exists(stub_path):
                add_stub_glyphs(font, stub_path)

            # TODO:
            # Make sure this code isn't a duplicate of the .stub.glyphs handling above
            # Add encoded characters to .glyphs file
            # That pertains to all of character_set handling
            for _i, unicode in enumerate(sorted(list(character_set))):
                if not _font_has_unicode(font, unicode):
                    unicode = f"{unicode:#0{6}X}".replace("0X", "")
                    glyph_info = _lookup_attributes_by_unicode(unicode, GLYPHDATA)
                    if "name" in glyph_info:
                        new_glyph = glyphsLib.GSGlyph(glyph_info["name"])
                    else:
                        new_glyph = glyphsLib.GSGlyph(f"uni{unicode}")
                    new_glyph.unicode = unicode
                    font.glyphs.append(new_glyph)

            # Add stub glyphs to .glyphs file
            for glyph in self.get_stub_glyph_objects():
                if (
                    glyph.unicode
                    and not _font_has_unicode(font, glyph.unicode)
                    or not glyph.unicode
                    and not font.glyphs[glyph.name]
                ):
                    new_glyph = glyphsLib.GSGlyph(glyph.name)
                    font.glyphs.append(new_glyph)

            # Sort into categories
            font.glyphs = sorted(font.glyphs, key=functools.cmp_to_key(sort_by_category))

            # Arabic presentation forms
            glyphs = []
            if self.script == "Arabic":
                for glyph in font.glyphs:
                    glyphs.append(glyph)
                    if glyph.unicode:
                        unicode = int(glyph.unicode, 16)
                        ucd = youseedee.ucd_data(unicode)
                        if ucd["Script"] == "Arabic":
                            if (
                                ucd["General_Category"] == "Lo"
                                and "Joining_Type" in ucd
                                and ucd["Joining_Type"] in ("D")
                            ):
                                glyphs.append(glyphsLib.GSGlyph(f"{glyph.name}.init"))
                                glyphs.append(glyphsLib.GSGlyph(f"{glyph.name}.medi"))
                                glyphs.append(glyphsLib.GSGlyph(f"{glyph.name}.fina"))
                            elif (
                                ucd["General_Category"] == "Lo"
                                and "Joining_Type" in ucd
                                and ucd["Joining_Type"] == "R"
                            ):
                                glyphs.append(glyphsLib.GSGlyph(f"{glyph.name}.fina"))

                font.glyphs = glyphs

            self._final_glyphs_font = font

            return font

    def get_final_glyph_objects(self):
        # return sorted(self.get_final_glyphs_font().glyphs, key=functools.cmp_to_key(sort_unicodes_by_glyphobject))
        return self.get_final_glyphs_font().glyphs

    def get_final_unicodes(self):
        return [glyph.unicode for glyph in self.get_final_glyph_objects() if glyph.unicode]

    def get_final_glyphnames(self, exclusive=True):

        glyph_names = [glyph.name for glyph in self.get_final_glyph_objects()]

        if self.script == "Cyrillic" and self.modifier in ("Roman Localizations", "Italic Localizations"):
            font = glyphsLib.load(
                os.path.join(
                    root_folder, "definitions", "misc", f"cyrillic_locl_{self.modifier.split(' ')[0].lower()}.glyphs"
                )
            )
            locl_glyphs = []
            for glyph in font.glyphs:
                if glyph.name.split(".")[0] in glyph_names:
                    locl_glyphs.append(glyph.name)
            return locl_glyphs

        if self.modifier == "Exclusive" and exclusive:

            inherited_glyphs = set()
            for glyphset in self.include_glyphsets:
                inherited_glyphset = GlyphSet.load(glyphset)
                this_inherited_glyphs = set(inherited_glyphset.get_final_glyphnames())
                inherited_glyphs.update(this_inherited_glyphs)

            # Subtract own glyphs
            complete_glyphs = set(self.get_final_glyphnames(exclusive=False))
            glyph_names = sorted(list(set(complete_glyphs) - inherited_glyphs))

            return sorted(glyph_names, key=functools.cmp_to_key(sort_by_category))

        else:
            return glyph_names

    def get_final_productionglyphnames(self):
        return [get_glyph(glyph_name).production_name for glyph_name in self.get_final_glyphnames()]

    def get_description(self):

        glyphs_stub_path = os.path.join(root_folder, "definitions", "per_glyphset", f"{self.name}.stub.glyphs")

        warning = False
        md = ""

        md += f"# {self.name.replace('_', ' ')}\n\n"
        if self.description:
            md += (
                "> _Description partially salvaged from old README, so languages manually listed here (if any) may be "
                + "outdated or irrelevant and need to be replaced by language code lists:_\n> \n> "
                + "\n> ".join(self.description.split("\n"))
                + "\n\n"
            )
        if self.regions:
            md += f"`{self.name}` is **dynamically** defined [here](/Lib/glyphsets/definitions/{self.name}.yaml) "
            md += "as:\n\n"
        else:
            md += f"`{self.name}` is **statically** defined [here](/Lib/glyphsets/definitions/{self.name}.yaml) "
            md += "as:\n\n"
        md += f"* Script: {self.script}\n"

        def make_link(text, bracket="`"):
            return f"[{bracket}{text}{bracket}](#{text.lower().replace('_', '-')})"

        if self.get_included_glyphsets():
            md += "* Includes glyphsets \n" + ",\n".join(map(make_link, self.get_included_glyphsets())) + "\n\n"
        # Dynamic defintion
        if self.regions:
            md += "* All languages of the countries `\n" + ",\n".join(sorted(map(add_country, self.regions))) + "\n`\n"
        if self.population:
            md += f"* With a population of over {self.population} speakers\n"
        if self.historical:
            md += "* Including historical languages\n"
        if self.use_aux:
            md += "* Including auxiliary characters\n"
        if self.exclude_language_codes:
            md += (
                "* Excluding the following languages: `\n"
                + ",\n".join(sorted(map(add_language, self.exclude_language_codes)))
                + "\n`\n"
            )

        if self.regions and self.language_codes:
            md += (
                "* Additionally, the following languages are defined **statically**: `\n"
                + ",\n".join(sorted(map(add_language, self.language_codes)))
                + "\n`\n"
            )

        # Static defintion
        elif not self.regions and self.language_codes:
            md += "* List of languages: `\n" + ",\n".join(sorted(map(add_language, self.language_codes))) + "\n`\n"

        # Additional resources
        if os.path.exists(glyphs_stub_path):
            md += f"* Characters and glyphs defined in [{os.path.basename(glyphs_stub_path)}]"
            md += f"(/data/definitions/per_glyphset/{os.path.basename(glyphs_stub_path)})\n"
        for language_code in self.language_codes:
            lang_stub_path = os.path.join(root_folder, "definitions", "per_language", f"{language_code}.stub.glyphs")
            if os.path.exists(lang_stub_path):
                md += "* Language-specific characters and glyphs defined for "
                md += f"[{add_language(language_code)}]"
                md += f"(/data/definitions/per_language/{os.path.basename(lang_stub_path)})\n"

        if not self.regions and not self.language_codes:
            md += "\n> [!CAUTION]  \n> Since this glyphset has no defined languages, it can't be checked via "
            md += "Fontbakery's `shape_languages` check.\n> Please add language code definions "
            md += f"[here](/Lib/glyphsets/definitions/{self.name}.yaml).\n"
            warning = True

        md += "\n"

        if self.regions:
            _languages_per_glyphset = GlyphSet.load(self.name).get_language_codes()
            md += (
                f"\nThe following list of **{len(_languages_per_glyphset)}** languages is computed as a result "
                + "of the dynamic conditions described above:\n\n`\n"
                + ",\n".join(sorted(map(add_language, _languages_per_glyphset)))
                + "\n`\n\n"
            )

        # Content
        md += "### Characters and Glyphs\n\n"
        md += str(describe_glyphset(glyphs_in_glyphset(self.name)))

        # Composed characters
        decomposed_chars = get_decomposed_chars(self.name)
        if decomposed_chars:
            md += "### Character Sequences\n\n"
            md += f"The following {len(decomposed_chars)} composed character sequences are decomposed in the font:\n\n"
            md += "`\n"
            md += " ".join(decomposed_chars)
            md += "\n`\n\n"

        md += "### Resulting Glyphset Files\n\n"
        md += f".nam file (only encoded characters): [{self.name}.nam](/data/results/nam/{self.name}.nam)\n\n"
        md += f"Glyphs.app source file: [{self.name}.glyphs](/data/results/glyphs/{self.name}.glyphs)\n\n"
        md += f"Text files: [{self.name}.txt](/data/results/txt/nice-names/{self.name}.txt) (nice names) and "
        md += f"[{self.name}.txt](/data/results/txt/prod-names/{self.name}.txt) (production names)\n\n"
        md += f"Glyphs.app Custom Filter List (contains all {self.script} glyphsets): "
        md += f"[CustomFilter_GF_{self.script}.plist](/data/results/plist/CustomFilter_GF_{self.script}.plist)\n\n"
        md += " or [CustomFilter_GF_All.plist](/data/results/plist/CustomFilter_GF_All.plist)"
        md += " for the complete list.\n\n"

        return md, warning


class Glyph(object):
    def __init__(self, name, unicode=None):
        self.name = name
        self.unicode = unicode


def get_glyphs_file(file_path):
    font = glyphsLib.load(file_path)
    for glyph in font.glyphs:
        if glyph.unicode:
            glyph_info = _lookup_attributes_by_unicode(glyph.unicode, GLYPHDATA)
            if "name" in glyph_info and glyph_info["name"] != glyph.name:
                glyph.name = glyph_info["name"]
    return font


def defined_glyphsets():
    """Return a list of defined glyphsets"""

    definitions_path = os.path.join(os.path.dirname(__file__), "definitions")
    yaml_files = [
        os.path.splitext(f)[0]
        for f in os.listdir(definitions_path)
        if os.path.isfile(os.path.join(definitions_path, f)) and f.endswith(".yaml")
    ]
    return sorted(yaml_files)


def extended_glyphsets():
    """
    Return a list of glyphsets, both explicitly defined as well as implicitly generated
    for instance when glyphsets have inheritances, to accomodate for exclusive glyphsets
    """

    glyphsets = []
    for glyphset in defined_glyphsets():
        glyphsets.append(glyphset)
        glyphsets.extend(GlyphSet.load(glyphset).get_extended_glyphsets())

    return glyphsets


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
    yaml_path = os.path.join(os.path.dirname(__file__), "definitions", f"{glyphset_name}.yaml")
    with open(yaml_path, "r", encoding="utf8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


# Rewrite this to be calculated live
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


# def glyphs_in_glyphsets(glyphset_names, production_names=False):
#     glyphs = set()
#     for glyphset_name in glyphset_names:
#         glyphs.update(glyphs_in_glyphset(glyphset_name, production_names))

#     return sorted(list(glyphs))


# Public API (used by fontbakery, gftools, etc.)
def languages_per_glyphset(glyphset_name):
    return GlyphSet.load(glyphset_name).get_language_codes()


# Public API (used by fontbakery, gftools, etc.)
# TODO:
# Rewrite this to be calculated live
def glyphs_in_glyphset(glyphset_name, production_names=False):
    # script = glyphset_name.split("_")[1]

    with open(
        os.path.join(
            tool_folder,
            "results",
            "txt",
            "nice-names",
            f"{glyphset_name}.txt",
        ),
        "r",
    ) as f:
        glyph_names = [line.strip() for line in f.readlines() if not line.startswith("#")]

    return sorted(glyph_names)


def categorize_glyphs(glyph_names):
    categories = {}

    unicode_sorted_glyph_names = sorted(glyph_names, key=functools.cmp_to_key(sort_unicodes_by_name))

    for glyph_name in unicode_sorted_glyph_names:
        glyph = get_glyph(glyph_name)
        if not glyph.category:
            category = "Uncategorized"
        else:
            category = glyph.category
            if category == "Mark" and glyph.subCategory == "Nonspacing":
                category = "Mark, nonspacing"
            elif category == "Mark":
                category = "Mark, spacing"
        if category not in categories:
            categories[category] = []

        if glyph.unicode:
            categories[category].append(chr(int(glyph.unicode, 16)))
        else:
            categories[category].append("/" + glyph_name)

    return dict(sorted(categories.items()))


def add_dotted_circle(character):
    return "◌" + character


def describe_glyphset(glyph_names, target="markdown", color=""):
    md = ""
    categories = categorize_glyphs(glyph_names)
    for category, characters in categories.items():
        md += f"{Colors.BOLD if target=='console' else ''}{category}{Colors.END if target=='console' else ''} "
        md += f"({len(characters)} glyphs): \n"

        if category == "Mark, nonspacing":
            string = " ".join(map(add_dotted_circle, characters))
        else:
            string = " ".join(characters)
        if target == "markdown":
            string = string.replace("`", "/grave")
        md += (
            f"`{color if target=='console' and color else ''}"
            + string
            + f"{Colors.END if target=='console' and color else ''}`\n\n"
        )
    return md


def compare_glyphsets(glyphsets):
    """
    Compare the contents of glyphsets to each other,
    with the first glyphset being the reference.
    Each consecutive glyphset gets compares to each former.
    """

    if len(list(set(glyphsets))) != len(glyphsets):
        raise ValueError("Please provide unique glyphsets to compare.")

    reference_glyphset = glyphsets[0]
    reference_glyphs = set(glyphs_in_glyphset(reference_glyphset))

    if not reference_glyphs:
        raise ValueError(f"Glyphset {reference_glyphset} is empty.")

    headline(reference_glyphset)
    print(f"Total glyphs: {len(reference_glyphs)}\n")
    print(describe_glyphset(reference_glyphs, target="console"))

    for i, _glyphset in enumerate(glyphsets):
        if i == 0:
            continue

        this_glyphs = set(glyphs_in_glyphset(glyphsets[i]))
        if not this_glyphs:
            raise ValueError(f"Glyphset {glyphsets[i]} is empty.")

        if i > 1:
            previous_glyphs = set(glyphs_in_glyphset(glyphsets[i - 1]))
        else:
            previous_glyphs = reference_glyphs

        headline(glyphsets[i])
        print(f"Total glyphs: {len(this_glyphs)}\n")

        missing = previous_glyphs.difference(this_glyphs)
        extra = this_glyphs.difference(previous_glyphs)

        if extra:
            print(
                f"{Colors.BOLD}{glyphsets[i]}{Colors.END} has {len(extra)} {Colors.GREEN}{Colors.BOLD}additional"
                + f"{Colors.END} glyphs compared to {Colors.BOLD}{glyphsets[i - 1]}{Colors.END}:\n"
            )
            print(describe_glyphset(extra, target="console", color=Colors.GREEN))

        if missing:
            print(
                f"{Colors.BOLD}{glyphsets[i]}{Colors.END} is {Colors.RED}{Colors.BOLD}missing{Colors.END} "
                + f"{len(missing)} glyphs compared to {Colors.BOLD}{glyphsets[i - 1]}{Colors.END}:\n"
            )
            print(describe_glyphset(missing, target="console", color=Colors.RED))


def add_country(code):
    if code in REGIONS:
        return f"{REGIONS[code].name} ({code})"
    return code


def add_language(code):
    if code in LANGUAGES:
        return f"{LANGUAGES[code].name} ({code})"
    return code


def get_unicodes_unique_in_glyphset(glyphset_name, compare_against_glyphset):
    unicodes_in_glyphset = set(unicodes_per_glyphset(glyphset_name))
    unicodes_in_compare_against = set(unicodes_per_glyphset(compare_against_glyphset))
    return unicodes_in_glyphset.difference(unicodes_in_compare_against)


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

        if len(res[glyphset]["has"]) > 0 and len(res[glyphset]["missing"]) == 0:
            res[glyphset]["percentage"] = 1
        else:

            # Calculate the percentage supported not in total glyphs in font
            # compared to the total glyphs in the glyphset,
            # but shrink both to the unique set of Unicodes in the glyphset.
            # Compare everything to Latin Core:
            # - Subtract Latin Core from the covered Unicodes
            # - Calculate percentage covered based on that

            if glyphset in ("GF_Latin_Kernel", "GF_Latin_Core"):
                if unicodes_in_glyphset:
                    has = res[glyphset]["has"]
                    res[glyphset]["percentage"] = len(has) / len(unicodes_in_glyphset)
                else:
                    res[glyphset]["percentage"] = 0
            else:
                if get_unicodes_unique_in_glyphset(glyphset, "GF_Latin_Core") > get_unicodes_unique_in_glyphset(
                    glyphset, "GF_Latin_Kernel"
                ):
                    unicodes_unique_in_glyphset = list(get_unicodes_unique_in_glyphset(glyphset, "GF_Latin_Core"))
                else:
                    unicodes_unique_in_glyphset = list(get_unicodes_unique_in_glyphset(glyphset, "GF_Latin_Kernel"))

                if unicodes_unique_in_glyphset:

                    has = set(res[glyphset]["has"]).intersection(set(unicodes_unique_in_glyphset))
                    res[glyphset]["percentage"] = len(has) / len(unicodes_unique_in_glyphset)

                    # res[glyphset]["has_unique"] = list(has)
                    # res[glyphset]["unique_in"] = unicodes_unique_in_glyphset
                else:
                    res[glyphset]["percentage"] = 0
    return dict(sorted(res.items(), key=lambda x: x[1]["percentage"], reverse=True))


def get_decomposed_chars(glyphset_name):
    allchars = set()
    for lang_code in GlyphSet.load(glyphset_name).get_language_codes():
        lang = LANGUAGES[lang_code]
        allchars.update(getattr(getattr(lang, "exemplar_chars", {}), "base", "").split(" "))
        if get_glyphset_definition(glyphset_name).get("use_auxiliary"):
            allchars.update(getattr(getattr(lang, "exemplar_chars", {}), "auxiliary", "").split(" "))
    decomposed_chars = sorted(
        [
            g[1:-1]
            for g in allchars
            if any(unicodedata.combining(c) for c in g) and g.startswith("{") and g.endswith("}")
        ]
    )

    return decomposed_chars


def analyze_font(ttFont):
    results = get_glyphsets_fulfilled(ttFont)

    def print_support(lower=0, upper=1):

        if lower >= 0.8:
            print(
                (
                    f"{Colors.BROWN}These glyphsets will {Colors.ITALIC}implicitly{Colors.END}{Colors.BROWN} be part "
                    f"of Fontbakery's {Colors.ITALIC}shape_languages{Colors.END}{Colors.BROWN} check:{Colors.END}"
                )
            )
            print()

        found = 0
        for key in results:
            if (lower < upper and lower <= results[key]["percentage"] < upper) or (
                lower == upper and results[key]["percentage"] == lower
            ):

                color = color = Colors.RED if results[key]["percentage"] < 0.8 else Colors.GREEN

                found += 1

                not_covered = ""
                if lower >= 0.8:
                    languages = GlyphSet.load(key).get_language_codes()
                    if not languages:
                        not_covered = (
                            f"{Colors.BROWN}(Not part of {Colors.ITALIC}shape_languages{Colors.END}"
                            f"{Colors.BROWN} because of missing language definitions){Colors.END}"
                        )
                print(
                    (
                        f"{Colors.BOLD}{key}{Colors.END} {color}{int(results[key]['percentage']*100)}%"
                        f"{Colors.END} {not_covered}"
                    )
                )
                if results[key]["missing"]:
                    print(f"Missing: {' '.join([chr(x) for x in results[key]['missing']])}")
                    if "unique" in results[key]:
                        print(f"Unique: {' '.join([chr(x) for x in results[key]['unique']])}")
                    if "has_unique" in results[key]:
                        print(f"Unique in font: {' '.join([chr(x) for x in results[key]['has_unique']])}")
                    print()
        if not found:
            print("———")

    headline("Fully supported glyphsets:")
    print_support(1, 1)

    print()
    headline("Partially supported glyphsets (>80%):")
    print_support(0.8, 1)

    print()
    headline("Unsupported glyphsets (<80%):")
    print_support(0, 0.8)


def find_character(input_character):
    if input_character.startswith("0x"):
        input_character = chr(int(input_character, 16))
    unicode_string = f"{ord(input_character):#0{6}X}".replace("0X", "0x")
    print(f"Character: [{input_character}]  ({unicode_string} {unicodedata.name(input_character)})")

    found_languages = []

    # Read language definitions
    for lang_code in LANGUAGES:
        lang = LANGUAGES[lang_code]
        if lang.exemplar_chars:
            chars = lang.exemplar_chars
            for category in ("base", "index", "marks", "numerals", "punctuation", "auxiliary"):
                if input_character in getattr(chars, category) or input_character in getattr(chars, category).upper():
                    # Find regions
                    found_regions = set()
                    for country_code in REGIONS:
                        if country_code in lang.region:
                            found_regions.update(set(REGIONS[country_code].region_group))

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
    print()

    if found_languages:
        print(
            tabulate.tabulate(
                found_languages,
                headers=["Language", "Name", "Category", "Speakers", "Script", "Regions"],
            )
        )
    else:
        print("The character was not found in any of the language definitions.")
    print()

    found_in_glyphsets = []
    for glyphset in defined_glyphsets():
        for unicode in unicodes_per_glyphset(glyphset):
            if unicode == ord(input_character):
                found_in_glyphsets.append(glyphset)
                break

    if found_in_glyphsets:
        print("Character is part of the following glyphsets:")
        print("---------------------------------------------")
        print("\n".join(found_in_glyphsets))
    else:
        print("The character is not part of any glyphset.")


if __name__ == "__main__":
    print(defined_scripts())
