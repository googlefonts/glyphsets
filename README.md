Glyphsets
=========

This python module provides an API with data about glyph sets for many different scripts and languages. This was crafted to specify the sets of characters that fonts in the Google Fonts collection are expected to provide glyphs for.

GF glyph sets
-------------

If you are a font developer or typeface designer, see the [`GF Glyphsets`](https://github.com/googlefonts/glyphsets/tree/main/GF_glyphsets) subdirectory which provides glyphset definition "standards" that are typically useful sets to draw. The GF_Glyphsets are thought as modules you can accumulate. Therefore the Vietname set only contains additional glyphs to Latin Core to be able to support Vietnamese language.

- Fonts commissioned by Google Fonts must support Latin level 1 to 4: i.e **Latin Core**, **Vietnamese** and **Plus sets**.
- Fonts submitted to Google Fonts must support at least **GF Latin Core**, and designers are strongly encouraged to consider adding the **GF Latin Plus set**.

API Subsets
-----------

On the other hand, the nam files on the [`Lib/glyphsets/encodings`](https://github.com/googlefonts/glyphsets/tree/main/Lib/glyphsets/encodings) directory are probably more useful for expert web developers. Those files explain how the Unicode Range subsets are defined, typically per script (writing system), in the Google Fonts css API.

Glyphsets tool
--------------

You can create your own glyphset filter using the `glyphsets` tool and our database.

You can install the tool with pip:

```
pip install glyphsets
```
We recommend installing it in a virtual environment.

- Main usage:
```
glyphsets filter-list [Set1, Set2,…] -o list-name.txt --prod-names
```
This command will create a filter list using production names. Without the `--prod-names` argument, the result would follow the Glyph's nice name scheme. You can then use these lists into any font editor to create your filter.

- To create a filter list specifically for Glyphs App, you need to change the file extension with `.plist`.
For example:

```
glyphsets filter-list GF_Latin_Core GF_Latin_Plus GF_Cyrillic_Core GF_Cyrillic_Plus -o CustomFilter_ProjectName.plist
```
Add this `.plist` file next to your Glyphs file and you would be ale to see it under your filters.

- If you want to check if your font is missing glyphs from GF_Latin_Core, run:
```
glyphsets missing-in-font font.ttf
```


