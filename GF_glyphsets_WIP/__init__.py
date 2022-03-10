"""
Tools to generate the GF Glyph Database
"""
from glob import glob
import json


# Glyph data schema
database = {
    "glyphs": [
        {"production_name": "A", "human_name": "A", "unicode": 0x0030, "glyphsets": ["LatinCore", "LatinKernel"]},
        {"production_name": "A.alt", "human_name": "A.alt", "unicode": None, "glyphsets": ["LatinCore"]},
        {"production_name": "f", "human_name": "f", "unicode": 0x0013, "glyphsets": ["Latin"]}

    ],
    # This needs work. Aim is to allow us to auto gen OT features from a glyphset
    "features": [
        {
            "glyphs_in_use": ["A", "A.alt"],
            "fea": "sub A by A.alt;",
            "feature": "ss01",
        },
        {
            "glyphs_in_use": ["f", "f_f"],
            "fea": "sub f f by f_f",
            "feature": "liga",
        }
    ]
}


class GFGlyphData:
    def __init__(self, db="path/to/data"):
        self.data = db if isinstance(db, dict) else self._read_data(db)
    
    def _read_data(self, path):
        with open(path) as db:
            json.load(db)
    
    def save(self):
        pass

    def update_database_from_sources(self, sources):
        """Update the database by using the glyphsets from source files.
        
        Please note that you may need to edit some data by hand"""
        for src in sources:
            pass

    def build_glyphsapp_filter_lists(self, glyphset, type="production_name"):
        "Build filter lists for glyphs app"
        pass

    def build_nam_files(self, glyphset):
        "Build GF nam files"
        pass

    def update_source_glyphset(self,src, glyphset):
        """Add glyphs to a source file"""
        pass
    
    def build_fea(self, glyphset):
        """Generate a .fea file based on a glyphset"""
        pass


glyph_data = GFGlyphData()
glyph_data.build_glyphsapp_filter_lists("LatinCore", "nice_names")
glyph_data.build_glyphsapp_filter_lists("LatinCore", "prod_names")