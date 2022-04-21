# Marc notes 2022/03/10:

## Why do we use .glyphs files as a source? (Marc F will see if he can make something format agnostic)

- Because we can visually see what a set looks like in an editor
- because glyphsapp has its own very small glyph database. I think it is called GlyphData.xml


## How do we derive all the data from the .glyphs files?

- Load glyphs
- Gen ttf
- use gftools namlists font.ttf to get the .nam files
- we then manually make the filter lists by hand.


## Future demands:

- We want a list of languages covered by each set
- We want a cli tool (maybe it could be also run inside font editors) which can add glyphs to sources so that they fulfil a glyphset
- The filter lists and nam files should be automatically generated
- What about automatic features. Glyphsapp kinda has this but it would be great to make this .fea

--
Taken from old readme (to rewrite)

Google Fonts 2016 Glyph Sets
============================

Three levels of Latin glyph sets were developed in June 2016 as a new baseline standard for fonts in the Google Fonts library.
Existing fonts in the library can be upgraded to these as part of a drive towards new quality standards.
All new fonts submitted to the library must now support the Plus level as a minumum requirement.

### Acknowledgements:

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
