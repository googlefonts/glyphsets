Below are the most important changes from each release.

### v1.?.0 (2024-?)
#### Changes since last release

- 

### v1.1.0 (2024-12-20)
#### Changes since last release

- Added Ⓓ (design right symbol) to **GF_Latin_Plus** (issue #217)
- Revised **GF_Cyrillic_Core** and **Plus** glyphset definitions with language definitions and descriptions
- Removed Python 3.8 support from tests
- Implemented `glyphsets find` to find characters in the language and glyphset definitions
- Remove invisible control and format characters from glyphsets (Unicode `Cc` and `Cf` categories)
- In `.nam` files, separate names from unicodes with a `#` to make the files consumable as-is in subsetting applications (issue #232)
- Include glyphset inheritance, defined in child glyphsets (e.g. **GF_Cyrillic_Plus** is set to include **GF_Cyrillic_Core**)
- Following inheritance, put out “Exclusive” glyphsets (for `.plist` files for now); may be extended to other outputs later
- Add `CustomFilter_GF_All.plist` to results
- Manually added **GF_Latin_Kernel** to all modern **Arabic**, **Cyrillic** glyphsets as well as **GF_Greek_Core**
- Added dynamic Cyrillic Roman/Italic localization glyphsets to `.plist` files based on manually curated files in `definitions/misc/`
- Added `glyphsets print-unicodes` command that prints a list of unicodes of several defined glyphsets that can be piped into command line arguments, for instance for `pyftsubset font.ttf --unicodes=$(glyphsets print-unicodes GF_Latin_Core GF_Cyrillic_Core)`
- Added a list of Arabic characters that either commonly included in fonts but are not in the Arabic language definitions (`alefWasla-ar`) or are commonly used as components (`behDotless-ar`)
- Added automatic Arabic `.init/.medi/.fina` presentation forms (and changed sortin for all glyphsets as an implication)
- Switched **GF_Cyrillic_Historical** from manual to language defintions, including Church Slavic (`cu_Cyrl`).

### v1.0.0 (2024-05-03)
#### Changes since last release

- Removed all remaining old code after diffenator2 got refactored
- Pulled in 3 additional African language definitions from `gflanguages v0.6.0`. **GF_Latin_African** glyphset didn’t change as a result of that, only its "Character Sequences" definitions increased from 722 to 746 (commit [8b93034](https://github.com/googlefonts/glyphsets/commit/8b930342005868b6d192c789aef154d715bcf0c0)).

### v0.6.20 (2024-4-24)
#### Changes since last release

- Added `language_code` definition for **GF_Latin_PriAfrican** to allow shaping tests
- Added `glyphsets coverage` CLI command that prints a font's glyphset coverages
- Reworked glyphset coverage calculation in `get_glyphsets_fulfilled()`; now based on characters per glyphset that are unique **when compared to GF_Latin_Core**.

**Coverage Calculation Changes in Detail:**

_Previously_, the coverage percentage as returned by `get_glyphsets_fulfilled()` would calculate all the font’s characters as a percentage of a glyphset’s total characters. Fontbakery (among others) would then treat a glyphset as covered as soon as 80% of characters are present.

This generally worked, but created unwelcome overlaps as soon as glyphsets were too similar to each other. The newly redefined **GF_Latin_PriAfrican** glyphset, for example, has only 34 additional characters compared to **GF_Latin_Core**, as revealed by the command `glyphsets compare GF_Latin_Core GF_Latin_PriAfrican`.

**GF_Latin_Core** on the other hand currently has 324 glyphs, and so a font that covers **GF_Latin_Core** also covers 90% of **GF_Latin_PriAfrican** and would therefore be counted as supporting **GF_Latin_PriAfrican** _by accident_, without _actually_ supporting it, resulting in loads of unwelcome reports by Fontbakery’s `shape_languages` check.

The _new_ calculation is based solely on **additional characters when compared to GF_Latin_Core**. Similar to the `compare` command, additional characters are calculated in a first step (`Ŋ ŋ Ɓ Ɔ Ɗ Ɛ Ƙ ƙ Ɲ Ƴ ƴ Ǹ ǹ ɓ ɔ ɗ ɛ ɲ Ḿ ḿ Ṅ ṅ Ṣ ṣ Ẹ ẹ Ị ị Ọ ọ Ụ ụ` for **GF_Latin_PriAfrican** vs **GF_Latin_Core**), and then it is calculated how many of _those_ characters a font supports, which is a significantly more accurate calculation.

Since `get_glyphsets_fulfilled()` is hosted here inside `glyphsets`, no changes to external implementations are required as the API didn't change, only the calculation of the percentage. Fontbakery still uses 80% as the threshold, but now based on a more accurate calculation.

### v0.6.19 (2024-4-17)
#### Changes since last release

- Removed unnecessary glyphsLib import that caused trouble on fontbakery.com

### v0.6.18 (2024-4-10)
#### Changes since last release

- Added back a few unencoded glyphs to **Latin_Plus** and **Latin_Vietnamese** that went missing in the recent data transition (Issue #166)
- Added `language_code` definition for **Latin_Vietnamese** to allow shaping tests
- Added `glyphsets compare` CLI command

### v0.6.17 (2024-Apr-3)
#### Changes since last release

Reinstated deleted GFTestData for compatibility with diffenator2

### v0.6.16 (2024-Apr-3)
#### Changes since last release

Actually nothing changed. Release was triggered prematurely.

### v0.6.15 (2024-Apr-3)
#### Changes since last release

- Excluded colonizer languages from African glyphset via new `exclude_language_codes` to prevent unnecessary glyphs (e.g. "ß") from appearing in the African Latin glyphset
- Reintroduced `glyphsets filter-list` command to generate custom filter lists

### v0.6.14 (2024-Feb-15)
#### Changes since last release

Added language codes for additional glyphsets that can be now covered in Fontbakery's shape_languages check.

In total, these glyphsets are now covered:
- Latin African+Core
- Cyrillic Core
- Greek Core
- Arabic Core+Plus

### v0.6.13 (2024-Feb-9)
#### Changes since last release

- Made human-readable description available in /GLYPHSETS.md
- Changed API, consequently updated Fontbakery's usage of the API
- Includes the new GF African Latin glyphset

### v0.6.11 (2023-Dec-15)
#### Changes since last release

- Transitioned GF_Arabic_Plus to new approach

### v0.6.5..10 (?)
#### Changes since last release

- Introduced new assembly approach of defining glyphsets as language code rather than codepoints, with codepoints being assembled from gflanguages

#### New Contributors
@yanone becomes repository maintainer

### v0.6.4 (2023-Sep-21)
#### Changes since last release

- [Symbols] new codepoints added to support Playpen Sans by @vv-monsalve in #127
- Add Aegean separator codepoints to Cypriot by @simoncozens in #128

#### New Contributors
@vv-monsalve made their first contribution in #127

### v0.6.3 (2023-Sep-20)
#### Changes since last release:
- [glyphsets] deprecated IJ/ij in GF_glyphsets by @RosaWagner in #111
- Update README.md by @davelab6 in #116
- [nam] Add Old Hungarian punctuation by @simoncozens in #113
- [nam] Add two dot punctuation to Old Turkic by @simoncozens in #114
- README: typo in 'Vietnamese' by @moyogo in #125

#### New Contributors
@davelab6 made their first contribution in #116
Full Changelog: v0.6.2...v0.6.3

### v0.6.2 (2023-Jun-21)
#### Changes since last release:

- Add combining marks to the latin, latin ext, and vietnamese glyphsets. by @garretrieger in #110

#### New Contributors
@garretrieger made their first contribution in #110

Full Changelog: v0.6.1...v0.6.2


### v0.6.1 (2023-May-3)
#### Changes since last release:

- [glyphsets]Added Okina in Beyond set by @RosaWagner in #103
- [nam] Add Kawi by @simoncozens in #106
- [nam] Add Nag Mundari by @simoncozens in #105
- [nam] Add Chorasmian glyphset by @simoncozens in #90
- [nam] Add Braille glyphset by @simoncozens in #91
- [nam] Add more yi codepoints by @simoncozens in #100
- [nam] Fill various holes by @simoncozens in #97
- [nam] Add UCAS Extended A codepoints by @simoncozens in #93
- [nam] Add IPA extensions by @simoncozens in #94
- Add missing Unicode 15.0 scripts by @simoncozens in #107
- [nam] Add all Arabic codepoints by @simoncozens in #92
- [nam] Add Ottoman Siyaq Numbers by @simoncozens in #108

Full Changelog: v0.6.0...v0.6.1


### v0.6.0 (2023-Mar-21)
#### Changes since previous release:

- Add SignWriting #84
- Improve coverage test name reporting #89
- Build subsets.SUBSETS dynamically #95
- Add test strings (attempt 2) #104

### v0.5.4 (2022-Nov-16)
#### Changes since last release:

- #83 Add Toto and Tangsa nam files

### v0.5.3 (2022-Oct-7)
#### Changes since previous release:

- #82: Removed U+20A4 (lira) from GF_Laptin_Plus
- #81: Replaced Minorities by Beyond
- #80 #79 #77 #73: adds missing glyphs to subsets
- #78: Removed A/a caron from Latin_Core
- #74 #72 #71 #70: Improved Phonetic glyphsets
- #63: Corrected African glyphset
- #69 #67: added missing glyphs to subsets (Armenian and Myanmar)

### v0.5.2 (2022-Jun-28)
#### Changes since previous release:

- missing_glyphsets_in_font: check keys not values #f0a1af223401271dc737f0003f37a67a63006f71


### v0.5.1 (2022-Jun-23)
#### Changes since last release:

- Small changes Latin #60
- Fixed threshold #62


### v0.5.0 (2022-Apr-29)
#### Changes since previous release:

- Removed WIP from directory name #49
- Gf glyphset update #50
- Updated bash script #51
- Updated Latin's readme.md #52
- Changed naming scheme, updated database and added translatin dir #53
- Updated readme.md with instructions to use `glyphsets` tool #54
- Add get_glyph method and refactor missing_glyphs #55


### v0.4.0 (2022-Apr-21)
#### Changes since previous release:

- Update `glyphsets` #45
- Update-db: skip glyphs which are non-exportable #48
- filter-lists: output glyphsapp plist files #47
- Update db 5d7b788

### v0.3.1 (2022-Apr-11)
#### Changes since previous release:

- Fix pypi upload `a2907eb` pointing at glyphsets tooling

### v0.3.0 (2022-Apr-11)
#### Changes since previous release:

- Add `glyphsets` tooling #43 to update the database

### 0.2.1 (2021-Dec-17)
  - Quick bugfix: undefined var `enc_path` (should be `nam_dir` instead!)

### 0.2.0 (2021-Dec-17)
#### Noteworthy code-changes
  - Added function `set_encoding_path` that allows one to use `.nam` files from a different directory, other than the files shipped with the `glyphsets` module.
  - Minor code cleanup
  - This release includes a few tweaks needed to support usage in `gftools`.


### 0.1.0 (2021-Dec-14)
#### Release notes
  - Initial release of the `glyphsets` python module.
  - Most of the code was migrated from the `gftools` repository (https://github.com/googlefonts/gftools/) so that glyphset data can be easily available to all our tools without having to also get the large dependency tree of `gftools`. The most immediate user of this module is `Font Bakery`, which needs to validate conformance of the Google Fonts glyphsets on font binaries being checked. (see https://github.com/googlefonts/fontbakery/issues/3533)
  - The second obvious user of this `glyphsets` module will be `gftools` itself. I'll be sending a pull request soon. All GFonts glyphset definitions will then be defined here on the `glyphsets` module, to avoid data duplication and to guarantee uniformity across tools.
