Below are the most important changes from each release.

## 0.2.1 (2021-Dec-17)
  - Quick bugfix: undefined var `enc_path` (should be `nam_dir` instead!)

## 0.2.0 (2021-Dec-17)
### Noteworthy code-changes
  - Added function `set_encoding_path` that allows one to use `.nam` files from a different directory, other than the files shipped with the `glyphsets` module.
  - Minor code cleanup
  - This release includes a few tweaks needed to support usage in `gftools`.


## 0.1.0 (2021-Dec-14)
### Release notes
  - Initial release of the `glyphsets` python module.
  - Most of the code was migrated from the `gftools` repository (https://github.com/googlefonts/gftools/) so that glyphset data can be easily available to all our tools without having to also get the large dependency tree of `gftools`. The most immediate user of this module is `Font Bakery`, which needs to validate conformance of the Google Fonts glyphsets on font binaries being checked. (see https://github.com/googlefonts/fontbakery/issues/3533)
  - The second obvious user of this `glyphsets` module will be `gftools` itself. I'll be sending a pull request soon. All GFonts glyphset definitions will then be defined here on the `glyphsets` module, to avoid data duplication and to guarantee uniformity across tools.
