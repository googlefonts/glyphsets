import yaml
import plistlib
import os
import gflanguages
from fontTools.unicodedata.Scripts import NAMES as SCRIPT_NAMES
import unicodedata
import functools
from glyphsLib.glyphdata import get_glyph
from glyphsets.helpers import Colors, headline

try:
    from ._version import version as __version__  # type: ignore
except ImportError:
    __version__ = "0.0.0+unknown"

root_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data"))
tool_folder = os.path.abspath(os.path.dirname(__file__))


def sort_unicodes(a, b):
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
    yaml_path = os.path.join(os.path.dirname(__file__), "definitions", f"{glyphset_name}.yaml")
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


def languages_per_glyphset(glyphset_name):

    script = get_script(glyphset_name)
    glyphset_definition = get_glyphset_definition(glyphset_name)
    language_codes = glyphset_definition.get("language_codes", [])
    regions = glyphset_definition.get("regions")
    # use_aux = glyphset_definition.get("use_auxiliary", False)
    historical = glyphset_definition.get("historical", False)
    population = glyphset_definition.get("population", False)
    exclude_language_codes = glyphset_definition.get("exclude_language_codes", set())

    # Assemble character sets from gflanguages
    if regions:
        for language in languages.values():
            if language.id in exclude_language_codes:
                continue
            if not historical and language.historical:
                continue
            if population > language.population:
                continue
            if set(language.region).intersection(set(regions)) and SCRIPT_NAMES[language.script] == script:
                language_codes.append(language.id)

    return language_codes


def categorize_glyphs(glyph_names):
    categories = {}

    unicode_sorted_glyph_names = sorted(glyph_names, key=functools.cmp_to_key(sort_unicodes))

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
    exclude_language_codes = glyphset_definition.get("exclude_language_codes", [])

    glyphs_stub_path = os.path.join(root_folder, "definitions", "per_glyphset", f"{glyphset_name}.stub.glyphs")

    warning = False
    md = ""

    md += f"# {glyphset_name.replace('_', ' ')}\n\n"
    if description:
        md += (
            "> _Description partially salvaged from old README, so languages manually listed here (if any) may be "
            + "outdated or irrelevant and need to be replaced by language code lists:_\n> \n> "
            + "\n> ".join(description.split("\n"))
            + "\n\n"
        )
    if regions:
        md += f"`{glyphset_name}` is **dynamically** defined [here](/Lib/glyphsets/definitions/{glyphset_name}.yaml) "
        md += "as:\n\n"
    else:
        md += f"`{glyphset_name}` is **statically** defined [here](/Lib/glyphsets/definitions/{glyphset_name}.yaml) "
        md += "as:\n\n"
    md += f"* Script: {script}\n"

    # Dynamic defintion
    if regions:
        md += "* All languages of the countries `\n" + ",\n".join(sorted(map(add_country, regions))) + "\n`\n"
    if population:
        md += f"* With a population of over {population} speakers\n"
    if historical:
        md += "* Including historical languages\n"
    if use_aux:
        md += "* Including auxiliary characters\n"
    if exclude_language_codes:
        md += (
            "* Excluding the following languages: `\n"
            + ",\n".join(sorted(map(add_language, exclude_language_codes)))
            + "\n`\n"
        )

    if regions and language_codes:
        md += (
            "* Additionally, the following languages are defined **statically**: `\n"
            + ",\n".join(sorted(map(add_language, language_codes)))
            + "\n`\n"
        )

    # Static defintion
    elif not regions and language_codes:
        md += "* List of languages: `\n" + ",\n".join(sorted(map(add_language, language_codes))) + "\n`\n"

    # Additional resources
    if os.path.exists(glyphs_stub_path):
        md += f"* Characters and glyphs defined in [{os.path.basename(glyphs_stub_path)}]"
        md += f"(/data/definitions/per_glyphset/{os.path.basename(glyphs_stub_path)})\n"
    for language_code in language_codes:
        lang_stub_path = os.path.join(root_folder, "definitions", "per_language", f"{language_code}.stub.glyphs")
        if os.path.exists(lang_stub_path):
            md += "* Language-specific characters and glyphs defined for "
            md += (
                f"[{add_language(language_code)}](/data/definitions/per_language/{os.path.basename(lang_stub_path)})\n"
            )

    if not regions and not language_codes:
        md += "\n> [!CAUTION]  \n> Since this glyphset has no defined languages, it can't be checked via "
        md += "Fontbakery's `shape_languages` check.\n> Please add language code definions "
        md += f"[here](/Lib/glyphsets/definitions/{glyphset_name}.yaml).\n"
        warning = True

    md += "\n"

    if regions:
        _languages_per_glyphset = languages_per_glyphset(glyphset_name)
        md += (
            f"\nThe following list of **{len(_languages_per_glyphset)}** languages is computed as a result "
            + "of the dynamic conditions described above:\n\n`\n"
            + ",\n".join(sorted(map(add_language, _languages_per_glyphset)))
            + "\n`\n\n"
        )

    # Content
    md += "### Characters and Glyphs\n\n"
    md += str(describe_glyphset(glyphs_in_glyphset(glyphset_name)))

    # Composed characters
    decomposed_chars = get_decomposed_chars(glyphset_name)
    if decomposed_chars:
        md += "### Character Sequences\n\n"
        md += f"The following {len(decomposed_chars)} composed character sequences are decomposed in the font:\n\n"
        md += "`\n"
        md += " ".join(decomposed_chars)
        md += "\n`\n\n"

    md += "### Resulting Glyphset Files\n\n"
    md += f".nam file (only encoded characters): [{glyphset_name}.nam](/data/results/nam/{glyphset_name}.nam)\n\n"
    md += f"Glyphs.app source file: [{glyphset_name}.glyphs](/data/results/glyphs/{glyphset_name}.glyphs)\n\n"
    md += f"Text files: [{glyphset_name}.txt](/data/results/txt/nice-names/{glyphset_name}.txt) (nice names) and "
    md += f"[{glyphset_name}.txt](/data/results/txt/prod-names/{glyphset_name}.txt) (production names)\n\n"
    md += f"Glyphs.app Custom Filter List (contains all {script} glyphsets): "
    md += f"[CustomFilter_GF_{script}.plist](/data/results/plist/CustomFilter_GF_{script}.plist)\n\n"

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

        if len(res[glyphset]["has"]) > 0 and len(res[glyphset]["missing"]) == 0:
            res[glyphset]["percentage"] = 1
        else:

            # Calculate the percentage supported not in total glyphs in font
            # compared to the total glyphs in the glyphset,
            # but shrink both to the unique set of Unicodes in the glyphset.
            # Compare everything to Latin Core:
            # - Subtract Latin Core from the covered Unicodes
            # - Calculate percentage covered based on that

            if glyphset == "GF_Latin_Core":
                if unicodes_in_glyphset:
                    has = res[glyphset]["has"]
                    res[glyphset]["percentage"] = len(has) / len(unicodes_in_glyphset)
                else:
                    res[glyphset]["percentage"] = 0
            else:
                unicodes_unique_in_glyphset = list(
                    set(unicodes_per_glyphset(glyphset)).difference(set(unicodes_per_glyphset("GF_Latin_Core")))
                )

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
    for lang_code in languages_per_glyphset(glyphset_name):
        lang = languages[lang_code]
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
                    languages = languages_per_glyphset(key)
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


if __name__ == "__main__":
    print(defined_scripts())
