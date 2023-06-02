"""
Assemble .nam files from .nam stub files and language definitions.
"""

import yaml
import os
import gflanguages
import unicodedata


def assemble_characterset(nam_stub_path, nam_path, languages_yaml_path):
    character_set = set()

    # Read language definitions
    with open(languages_yaml_path, "r") as stream:
        language_definitions = yaml.safe_load(stream)

    # Assemble character sets from gflanguages
    languages = gflanguages.LoadLanguages()
    for language_code in language_definitions["language_codes"]:
        chars = languages[language_code].exemplar_chars
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
                    # | set(chars.auxiliary)
                )
                if c not in (" ", "{", "}")
            }
        )

    # Read .nam stub file
    with open(nam_stub_path, "r") as f:
        nam_stub_lines = f.readlines()
    for line in nam_stub_lines:
        unicode = line.split(" ")[0]
        if unicode.startswith("0x"):
            character_set.add(int(unicode[2:], 16))

    # Output sorted character set to .nam file
    with open(nam_path, "w") as f:
        for unicode in sorted(list(character_set)):
            unicode_string = f"{unicode:#0{6}X}".replace("0X", "0x")
            f.write(f"{unicode_string} {unicodedata.name(chr(unicode))}\n")


if __name__ == "__main__":
    for root, dir, files in os.walk(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "GF_Glyphsets"))
    ):
        for file in files:
            if file.endswith(".stub.nam"):
                # .nam stub file
                nam_stub_path = os.path.join(root, file)
                nam_path = os.path.join(root, file).replace(".stub.nam", ".nam")

                # corresponding languages .yaml file
                languages_yaml_path = os.path.abspath(
                    os.path.join(
                        root, "..", "languages", file.replace(".stub.nam", ".yaml")
                    )
                )

                if all(
                    [os.path.exists(x) for x in [nam_stub_path, languages_yaml_path]]
                ):
                    assemble_characterset(nam_stub_path, nam_path, languages_yaml_path)
