Google Fonts Glyphset Definitions
=================================

What is this?
-------------

This repository contains curated glyphsets that Google Fonts hands out to **designers of commissioned fonts** for font authoring.

What is this _not_?
-------------------

These _glyphsets_ are not to be confused with the _subsets_ that the [Google Fonts API](https://developers.google.com/fonts/docs/getting_started#specifying_script_subsets) uses to minimize traffic by serving partial fonts based on subsets.

These subset definitions used to be hosted here in this repository but are now found over in the separate [nam-files](https://github.com/googlefonts/nam-files) repository. 

What’s the difference?
----------------------

As a user of the [Google Fonts API](https://developers.google.com/fonts/docs/getting_started#specifying_script_subsets) you may request a multi-script font to be served limited to a _subset_ of glyphs, usually a certain script, such as `https://fonts.googleapis.com/css?family=Roboto+Mono&subset=cyrillic`, to speed up file transfer by leaving out unnecessary glyphs.

_Glyphsets_ on the other hand are what Google Fonts requires font authors to put into fonts when _designing_ them, and they’re not identical to subsets. You can get a font’s complete glyphset by manually downloading a TTF on [fonts.google.com](https://fonts.google.com/), but you typically don’t get the same glyphs in a font accessed through the Google Fonts API because these are subsetted.


Glyphsets for font authoring
----------------------------

**If you are a font author** and you want to merely get your hands on ready-made glyphsets, pick your files straight out of the [`/data/results`](/data/results) folder, such as `.glyphs` files with empty placeholder glyphs, or `.plist` files that are so-called _Custom Filters_ that will show up in the Glyphs.app sidebar when placed alongside your source files. Alternatively, you can cook your own Custom Filters with the `glyphsets` tool, see the _Glyphsets Tool_ section at the bottom of this document.

The rest of this README is addressing people who are **editing** glyphset and language definitions.

Editing glyphsets
-----------------

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

> [!NOTE]  
> When making PRs, the glyphsets will automatically be rendered depending on defintion changes (which is useful for dependency update PRs such as `glyphsLib` or `gflanguages`). This means that you don’t _need to_ supply updated glyphsets and `GLYPHSETS.md` as part of your PR (as rendered by `sh build.sh`). A PR may be as simple as adding a language to a `.yaml` defintion and the changes to glyphsets will automatically be added in a commit to your PR where you can review the changed glyphsets.


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

> [!NOTE]  
> Previously existing commands of the `glyphsets` tool are currently deactivated after the transition to the new database. These are: `update-srcs`, `nam-file`, `missing-in-font`. Please report if you need to use these.

## Custom Filters

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

## Compare Glyphsets

You can compare the contents of two or more glyphsets against each other. Each consecutive glyphset will be compared to the previous one.

This command lists the complete contents of `GF_Latin_Kernel` first, and then lists only extra (or missing) glyphs for `GF_Latin_Core` when compared to `GF_Latin_Kernel`:
```
glyphsets compare GF_Latin_Kernel GF_Latin_Core
```

Output:

```
GF_Latin_Kernel:
===============

Total glyphs: 116

Letter (52 glyphs): 
`A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z`

...


GF_Latin_Core:
=============

Total glyphs: 324

GF_Latin_Core has 208 **extra** glyphs compared to GF_Latin_Kernel:

Letter (168 glyphs): 
`ª º À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö Ø Ù Ú Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ø ù ú û ü ý þ ÿ Ā ā Ă ă Ą ą Ć ć Ċ ċ Č č Ď ď Đ đ Ē ē Ė ė Ę ę Ě ě Ğ ğ Ġ ġ Ģ ģ Ħ ħ Ī ī Į į İ ı Ķ ķ Ĺ ĺ Ļ ļ Ľ ľ Ł ł Ń ń Ņ ņ Ň ň Ő ő Œ œ Ŕ ŕ Ř ř Ś ś Ş ş Š š Ť ť Ū ū Ů ů Ű ű Ų ų Ŵ ŵ Ŷ ŷ Ÿ Ź ź Ż ż Ž ž Ș ș Ț ț ȷ Ẁ ẁ Ẃ ẃ Ẅ ẅ ẞ Ỳ ỳ /idotaccent`

...

```

## Find characters

To help authoring glyphsets, use `glyphsets find ſ` or `glyphsets find 0x017F` to see in which language definitions (and under which category therein) and glyphsets a character is defined. As usual, the definitions are pulled from the `glyphsets` and `gflanguages` modules that are currently installed on your machine or venv

```
glyphsets % glyphsets find ß
Character: [ß]  (0x00DF LATIN SMALL LETTER SHARP S)

Language    Name           Category      Speakers  Script    Regions
----------  -------------  ----------  ----------  --------  ---------------------------------------
fr_Latn     French         auxiliary    272965534  Latn      Asia, Americas, Oceania, Europe, Africa
de_Latn     German         base         134799567  Latn      Asia, Americas, Europe, Africa
tr_Latn     Turkish        auxiliary     80191488  Latn      Europe, Asia
it_Latn     Italian        auxiliary     70743415  Latn      Oceania, Europe, Americas
pl_Latn     Polish         auxiliary     38273562  Latn      Europe, Asia
nds_Latn    Low German     base          11520008  Latn      Europe
fi_Latn     Finnish        auxiliary      5736841  Latn      Europe
lb_Latn     Luxembourgish  auxiliary       421015  Latn      Europe
ksh_Latn    Colognian      base            240479  Latn      Europe
hsb_Latn    Upper Sorbian  auxiliary        12825  Latn      Europe
wae_Latn    Walser         auxiliary        11376  Latn      Europe
dsb_Latn    Lower Sorbian  auxiliary         6973  Latn      Europe

Character is part of the following glyphsets:
---------------------------------------------
GF_Latin_Core
```

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


Housekeeping
============

Since v1.0.0, use these rules for **version updates** in line with semver:

- Major versions for API changes (v**1**.0.0)
- Minor versions for language data changes (v1.**1**.0)
- Patch version for non-breaking miniscule code or language data fixes (v1.1.**1**)
