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
