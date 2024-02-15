Attention: Repository under transition
======================================

The assembly of character sets is currently undergoing a transition from the previous approach of using the `glyphsets` command and `data.json` as a database to using the `gflanguages` package as the database and assembling `.nam` and other files from that.

> [!NOTE]  
> Please see [GLYPHSETS.md](GLYPHSETS.md) for an up-to-date description of the state of the new language definitions.

How to assemble glyphs and characters using the new approach
------------------------------------------------------------

1. Define the glyphset in the Python module in `Lib/glyphsets/definitions/__init__.py` with language codes for your character set.
2. Optional: Have a `.stub.nam` file under `GF_Glyphsets/*/definitions/` for your character set, containing _encoded_ characters that you want to see included that can't be inferred from the `gflanguages` definitions.
3. Optional: Have a `.stub.glyphs` file under `GF_Glyphsets/*/definitions/` for your character set, containing _unencoded_ glyphs that you want to see included.
4. Update all glyphsets using `sh build.sh`, see below for details.

The final `.glyphs` files are the sum of `gflanguages` + `.stub.nam` + `.stub.glyphs`. See chart below.

> [!NOTE]  
> *glyphsets* uses the version of *gflanguages* that's currently installed on your system to query for characters per language. This enables you working on both packages locally at once. In any case, make sure that the *gflanguages* package is up-to-date on your system.

> [!NOTE]  
> _Bonus points:_ Sadly, in the creation of the `.glyphs` files, it's not possible to exactly recreate the glyph sorting that Glyphs.app uses by default, so the `.glyphs` files look a bit different from what's expected. If you care, please open every freshly adjusted `.glyphs` file in Glyphs.app, select all glyphs, and run "Update Glyph Info" from the "Glyphs" menu on them to sort them and save the file. But the files will work as-is in any case.

Data flow visualization
-----------------------

Visualizes in a simplified way how the various data sources are combined into a final glyphset, then rendered out to various format.
This process is repeated for every glyphset defined in `Lib/glyphsets/definitions/__init__.py`.

Read this top to bottom.

```
┌──────────────────┐
│ Language codes   │
│ "en_Latn"        │
│ "de_Latn"        │
│ ...              │
└──────────────────┘
         │
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│ gflanguages      │   │ .stub.nam        │   │ .stub.glyphs     │
│ (Python package) │   │ (optional)       │   │ (optional)       │
└──────────────────┘   └──────────────────┘   └──────────────────┘
         │                      │                      │
         ╰──────────────────────┼──────────────────────╯
                                │
                ╔═══════════════════════════════╗
                ║ complete glyphset             ║ 
                ╚═══════════════════════════════╝
                                │
         ╭──────────────────────┼──────────────────────┬──────────────────────╮
         │                      │                      │                      │
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│ .txt             │   │ .nam             │   │ .glyphs          │   │ .plist           │
│ (nice & prod)    │   │                  │   │                  │   │                  │
└──────────────────┘   └──────────────────┘   └──────────────────┘   └──────────────────┘
```


Acknowledgements
----------------

GF Greek Glyph Sets defined by Irene Vlachou @irenevl and Thomas Linard @thlinard. Documented by Alexei Vanyashin @alexeiva January 2017.

GF Glyph Sets defined by Alexei Vanyashin (@alexeiva) and Kalapi Gajjar (@kalapi) from 2016-06-27 to 2016-10-11, with input from
Dave Crossland,
Denis Jacquerye,
Frank Grießhammer,
Georg Seifert,
Gunnar Vilhjálmsson,
Jacques Le Bailly,
Michael Everson,
Nhung Nguyen (Vietnamese lists),
Pablo Impallari (Impallari Encoding),
Rainer Erich Scheichelbauer (@mekkablue),
Thomas Jockin,
Thomas Phinney
(Adobe Cyrillic lists), and
Underware (Latin Plus Encoding)
