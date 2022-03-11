"""
Tools to generate the GF Glyph Database
"""
import json
import os
from re import L
from glyphsLib import GSFont
from defcon import Font
import logging


DATA = os.path.join(os.path.dirname(__file__), "data.json")
log = logging.getLogger(__file__)


class GFGlyphData:
    def __init__(self, data=json.load(open(DATA))):
        self._data = data
        self._in_use = set(g["nice_name"] for g in self._data["glyphs"])

    def save(self, fp=DATA):
        with open(fp, "w") as db:
            json.dump(self._data, db, indent=2)

    @classmethod
    def from_json(cls, fp):
        with open(fp) as db:
            data = json.load(db)
            return cls(data)

    def __getitem__(self, k):
        return self._data[k]

    def update_from_sources(self, sources):
        """Update the database by using the glyphsets from source files.

        Please note that you may need to edit some data by hand"""
        for src in sources:
            if isinstance(src, GSFont):
                glyphset = os.path.basename(src.filepath).split(".")[0]
                for g in src.glyphs:
                    self._add_glyph(glyphset, g.name, unicodes=g.unicode)
            elif isinstance(src, Font):
                glyphset = os.path.basename(src.path).split(".")[0]
                for g in src:
                    self._add_glyph(glyphset, g.name, unicodes=g.unicode)
            else:
                raise NotImplementedError(f"{src} not supported yet!")

    def _add_glyph(self, glyphset, nice_name=None, unicodes=None):
        if nice_name in self._in_use:
            entry = next(
                (g for g in self._data["glyphs"] if g["nice_name"] == nice_name), None
            )
            if glyphset in entry["glyphsets"]:
                log.warning(f"Skipping {glyphset}.{nice_name}. Already exists!")
                return
            entry["glyphsets"].append(glyphset)
        else:
            self._data["glyphs"].append(
                {"nice_name": nice_name, "unicode": unicodes, "glyphsets": [glyphset]}
            )

    def build_glyphsapp_filter_lists(self, glyphset, type="production_name"):
        "Build filter lists for glyphs app"
        pass

    def build_nam_files(self, glyphset):
        "Build GF nam files"
        pass

    def update_source_glyphset(self, src, glyphset):
        """Add glyphs to a source file"""
        if isinstance(src, Font):
            glyphs_in_font = set(g.name for g in src)
            for g in self._data["glyphs"]:
                if g["nice_name"] not in glyphs_in_font and glyphset in g["glyphsets"]:
                    new_glyph = src.newGlyph(g["nice_name"])
                    new_glyph.color = "Red"
            src.save()
        else:
            raise NotImplementedError()

    def build_fea(self, glyphset):
        """Generate a .fea file based on a glyphset"""
        # TODO this is 2022 Q3/4 goal
        raise NotImplementedError()


src = Font("demo.ufo")
data = GFGlyphData()
data.update_source_glyphset(src, "GFLatinPlus")
print()
