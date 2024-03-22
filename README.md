Google Fonts Glyphset Definitions
=================================

This repository contains curated glyphsets that Google Fonts hands out to designers of commissioned fonts.

> [!NOTE]  
> **If you are a user** and you want to merely get your hands on ready-made glyphsets, pick your files straight out of the [`/data/results`](/data/results) folder, such as `.glyphs` files with empty placeholder glyphs, or `.plist` files that are so-called _Custom Filters_ that will show up in the Glyphs.app sidebar when placed alongside your source files. Alternatively, you can cook your own Custom Filters with the `glyphsets` tool, see the _Glyphsets Tool_ section at the bottom of this document.
>
> The rest of this README is addressing people who are **editing** glyphset and language definitions.

The repository recently (end of 2023/start of 2024) underwent a bigger overhaul in how the glyphsets are assembled. 
The current approach has become part of a bigger network of tools that is also comprised of [gflanguages](https://github.com/googlefonts/lang/) and [shaperglot](https://github.com/googlefonts/shaperglot), as well as [fontbakery’s](https://github.com/fonttools/fontbakery) `shape_languages` check.

In the ideal scenario, glyphsets are defined merely by lists of language codes (such as `tu_Latn`).
During the build process (`sh build.sh`), the `gflanguages` database will be queried for all characters defined for those languages, then combined into a single glyphset.
_Optionally_, encoded characters as well as unencoded glyphs may be defined in glyphset-specific or language-specific files here in `gfglyphsets`, whose contents will also be added to the final glyphsets.

Later during font QA (as part of font onboarding work, just FYI), Fontbakery's `shape_languages` check first determines which glyphsets a font supports, then uses the languages defined for each glyphset to invoke `shaperglot`, which checks whether each language _shapes_ correctly or not.
This presents quite a leap forward in font QA where `shaperglot` invokes the `harfbuzz` shaping engine to prove the entire OpenType-stack to be funtioning at once, including mark attachment and character sequences.
`shaperglot` contains its own sets of script- or language-specific definitions, such as a check to see whether the `ı` and `i` shape into distinct letters in small-caps for Turkish.

> [!NOTE]  
> See [GLYPHSETS.md](GLYPHSETS.md) for an up-to-date description of the state of the new glyphset definitions. Many glyphsets have not been transitioned to the new approach and still exist as manually curated lists of characters and unencoded glyphs.

How to assemble glyphsets
=========================

Prerequisites
-------------

In order for the build command to correctly assemble glyphsets using language defintions, make sure that your work environment sports the latest version of [gflanguages](https://github.com/googlefonts/lang/). If unsure, update it with `pip install -U gflanguages`.

Oftentimes you may want to adjust language definitions in `gflanguages` _at the same time_ as you’re adjusting other parts of the glyphsets. In this case you may clone the `gflanguages` repository to your computer and install it using `pip install -e .` from within its root folder. This will expose your `gflanguages` clone to your entire system (or virtual environment) and changes in `gflanguages` will automatically be reflected in other tools that use it, such as `gfglyphsets`, without the need of re-installing it after every code or data change. Thus, running `sh build.sh` will automatically use your latest language definitions, even before you have PR’d your language definition changes back to the repository.

Where are glyphsets defined?
------------------

Inside this repository, data is defined in two different places.
One place is inside the `glyphsets` Python package (`/Lib/glyphsets/definitions`). This data that needs to be exposed to third-party tools such as `fontbakery`.
The other place is in `/data/definitions`. This data is only used for authoring glyphsets and need not be distributed as part of the Python package.

1. **Inside Python package:** Glyphsets are defined in `.yaml` files inside the Python package folder at [`/Lib/glyphsets/definitions`](/Lib/glyphsets/definitions).

2. **Outside of Python package:** Additional files in the `/data/definitions` sub-folders will become part of the glyphsets as soon as they are found to exist under a certain filename. If a file that you need doesn't exist there, create it in its place.

Where are characters and glyphs defined?
------------------

In order to determine where _characters_ (encoded with a Unicode) or _glyphs_ (unencoded) are defined, follow this logic:
1. Is it a **language-specific encoded character**? Then it goes into the `gflanguages` database (which is a separate package) for example [here](https://github.com/googlefonts/lang/blob/main/Lib/gflanguages/data/languages/nl_Latn.textproto). `gflanguages` holds only encoded characters, not unencoded glyphs. Prepare a separate PR for `gflanguages` if you are changing those definitions as well.
1. Is it a **language-specific unencoded glyph**? Then it goes into `/data/definitions/per_language`
1. Is it a more general **glyphset-specific character or glyph**? Then it goes into `/data/definitions/per_glyphset`

If you find that you need additional separate definitions _per script_, contact @yanone to implement it.

(Re-) Building glyphsets
-----------------------

Once your language and glyphset definitions are set up and edited, run `sh build.sh` from the command line. This command sources characters from `gflanguages` as well as characters and glyphs from the various files in the `/data/definitions` folder, and combines them into one comprehensive list per glyphset, which are then rendered out into various different data formats into the `/data/results` folder.

Additionally, the [GLYPHSETS.md](GLYPHSETS.md) document is updated, which contains a human-readable overview of the state of each glyphset.


Data flow visualization
-----------------------

Here’s a visual overview of the data definitions that go into each glyphset, and the files that are created as results.

Read this top to bottom.

```

DEFINITIONS:

┌──────────────────┐
│ Language codes   │
│ "en_Latn"        │
│ "de_Latn"        │
│ ...              │
└──────────────────┘
         │
┌──────────────────┐                          ┌──────────────────┐
│ gflanguages      │                          │ .stub.glyphs     │
│ (Python package) │                          │ (optional)       │
└──────────────────┘                          └──────────────────┘
         │                                             │
         ╰──────────────────────┬──────────────────────╯
                                │
BUILD PROCESS:                  │
                                │
                ╔═══════════════════════════════╗
                ║ complete glyphset             ║ 
                ╚═══════════════════════════════╝
                                │
RESULTS:                        │
                                │
         ╭──────────────────────┼──────────────────────┬──────────────────────╮
         │                      │                      │                      │
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│ .txt             │   │ .nam             │   │ .glyphs          │   │ .plist           │
│ (nice & prod)    │   │                  │   │                  │   │                  │
└──────────────────┘   └──────────────────┘   └──────────────────┘   └──────────────────┘
```


Glyphsets Tool
==============

You can create your own Glyphs.app _Custom Filters_ using the `glyphsets` tool.

Install or update the tool with pip, if you haven’t already:

```
pip install -U glyphsets
```

Create a filter list for Glyph.app:

```
glyphsets filter-list -o myfilter.plist GF_Latin_Core GF_Latin_Plus
```
Add this `.plist` file next to your Glyphs file and (after restart) you would be able to see it in the filters sidebar.

> [!NOTE]  
> Previously existing commands of the `glyphsets` tool are currently deactivated after the transition to the new database. These are: `update-srcs`, `nam-file`, `missing-in-font`. Please report if you need to use these.


Acknowledgements
================

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
