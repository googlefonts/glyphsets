#!/usr/bin/env python3
#
# Copyright 2017-2022 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Helper APIs for interaction with Google Fonts glyphsets.

Provides APIs to interact with font subsets, codepoints for font or subset.
"""

from __future__ import print_function
from __future__ import unicode_literals

import codecs
import contextlib
import os
import re
import sys
import unittest
from pkg_resources import resource_filename
from warnings import warn
from fontTools import ttLib
from glyphsets import subsets

nam_dir = resource_filename("glyphsets", "encodings")

# Matches 4 or 5 hexadecimal digits that are uppercase at the beginning of the
# test string. The match is stored in group 0, e.g:
# >>> _NAMELIST_CODEPOINT_REGEX.match('1234X').groups()[0]
# '1234'
# >>> _NAMELIST_CODEPOINT_REGEX.match('1234A').groups()[0]
# '1234A'
_NAMELIST_CODEPOINT_REGEX = re.compile('^([A-F0-9]{4,5})')

_PLATFORM_ID_MICROSOFT = 3
_PLATFORM_ENC_UNICODE_BMP = 1
_PLATFORM_ENC_UNICODE_UCS4 = 10
_PLATFORM_ENCS_UNICODE = (_PLATFORM_ENC_UNICODE_BMP, _PLATFORM_ENC_UNICODE_UCS4)

def UnicodeCmapTables(font):
  """Find unicode cmap tables in font.

  Args:
    font: A TTFont.
  Yields:
    cmap tables that contain unicode mappings
  """
  for table in font['cmap'].tables:
    if (table.platformID == _PLATFORM_ID_MICROSOFT and
        table.platEncID in _PLATFORM_ENCS_UNICODE):
      yield table


_displayed_errors = set()
def ShowOnce(msg):
  """Display a message if that message has not been shown already.

  Unlike logging.log_first_n, this will display multiple messages from the same
  file/line if they are different. This helps for things like the same line
  that shows 'missing %s': we'll see each value of %s instead of only the first.

  Args:
    msg: A string message to write to stderr.
  """
  global _displayed_errors
  if msg in _displayed_errors:
    return
  _displayed_errors.add(msg)
  print(msg, file=sys.stderr)


def ListSubsets():
  """Returns a list of all subset names, in lowercase."""
  return subsets.SUBSETS


def SubsetsForCodepoint(cp):
  """Returns all the subsets that contains cp or [].

  Args:
    cp: int codepoint.
  Returns:
    List of lowercase names of subsets or [] if none match.
  """
  _subsets = []
  for subset in ListSubsets():
    cps = CodepointsInSubset(subset, unique_glyphs=True)
    if not cps:
      continue
    if cp in cps:
      _subsets.append(subset)
  return _subsets


def SubsetForCodepoint(cp):
  """Returns the highest priority subset that contains cp or None.

  Args:
    cp: int codepoint.
  Returns:
    The lowercase name of the subset, e.g. latin, or None.
  """
  _subsets = SubsetsForCodepoint(cp)
  if not _subsets:
    return None

  result = _subsets[0]
  for subset in sorted(_subsets):
    # prefer x to x-ext
    if result + '-ext' == subset:
      pass
    elif result == subset + '-ext':
      # prefer no -ext to -ext
      result = subset
    elif subset.startswith('latin'):
      # prefer latin to anything non-latin
      result = subset

  return result


def set_encoding_path(enc_path):
  global nam_dir
  nam_dir = enc_path


def CodepointsInSubset(subset, unique_glyphs=False):
  """Returns the set of codepoints contained in a given subset.

  Args:
    subset: The lowercase name of a subset, e.g. latin.
    unique_glyphs: Optional, whether to only include glyphs unique to subset.
  Returns:
    A set containing the glyphs in the subset.
  """
  if unique_glyphs:
    filenames = [CodepointFileForSubset(subset)]
  else:
    filenames = CodepointFiles(subset)

  filenames = [f for f in filenames if f is not None]

  if not filenames:
    return None

  cps = set()
  for filename in filenames:
    with codecs.open(filename, encoding='utf-8') as f:
      for line in f:
        if not line.startswith('#'):
          match = _NAMELIST_CODEPOINT_REGEX.match(line[2:7])
          if match is not None:
            cps.add(int(match.groups()[0], 16))

  return cps


def CodepointsInFont(font_filename):
  """Returns the set of codepoints present in the font file specified.

  Args:
    font_filename: The name of a font file.
  Returns:
    A set of integers, each representing a codepoint present in font.
  """

  font_cps = set()
  with contextlib.closing(ttLib.TTFont(font_filename)) as font:
    for t in UnicodeCmapTables(font):
      font_cps.update(t.cmap.keys())

  return font_cps


def CodepointFileForSubset(subset):
  """Returns the full path to the file of codepoints unique to subset.

  This API does NOT return additional codepoint files that are normally merged
  into the subset. For that, use CodepointFiles.

  Args:
    subset: The subset we want the codepoint file for.
  Returns:
    Full path to the file containing the codepoint file for subset or None if it
    could not be located.
  """

  filename = os.path.join(nam_dir, '%s_unique-glyphs.nam' % subset)
  if not os.path.isfile(filename):
    ShowOnce('no cp file for %s found at %s' % (subset,
                                                filename[len(nam_dir):]))
    return None

  return filename


def CodepointFiles(subset):
  """Returns the codepoint files that contain the codepoints in a merged subset.

  If a subset X includes codepoints from multiple files, this function
  returns all those files while CodepointFileForSubset returns the single
  file that lists the codepoints unique to the subset. For example, greek-ext
  contains greek-ext, greek, and latin codepoints. This function would return
  all three files whereas CodepointFileForSubset would return just greek-ext.

  Args:
    subset: The subset we want the codepoint files for.
  Returns:
    A list of 1 or more codepoint files that make up this subset.
  """
  files = [subset]

  # y-ext includes y
  # Except latin-ext which already has latin.
  if subset != 'latin-ext' and subset.endswith('-ext'):
    files.append(subset[:-4])

  # almost all subsets include latin.
  if subset not in ('khmer', 'latin'):
    files.append('latin')

  return map(CodepointFileForSubset, files)


def SubsetsInFont(file_path, min_pct, ext_min_pct=None):
  """Finds all subsets for which we support > min_pct of codepoints.

  Args:
    file_path: A file_path to a font file.
    min_pct: Min percent coverage to report a subset. 0 means at least 1 glyph.
    25 means 25%.
    ext_min_pct: The minimum percent coverage to report a -ext
    subset supported. Used to admit extended subsets with a lower percent. Same
    interpretation as min_pct. If None same as min_pct.
  Returns:
    A list of 3-tuples of (subset name, #supported, #in subset).
  """
  all_cps = CodepointsInFont(file_path)

  results = []
  for subset in ListSubsets():
    subset_cps = CodepointsInSubset(subset, unique_glyphs=True)
    if not subset_cps:
      continue

    # Khmer includes latin but we only want to report support for non-Latin.
    if subset == 'khmer':
      subset_cps -= CodepointsInSubset('latin')

    overlap = all_cps & subset_cps

    target_pct = min_pct
    if ext_min_pct is not None and subset.endswith('-ext'):
      target_pct = ext_min_pct

    if 100.0 * len(overlap) / len(subset_cps) > target_pct:
      results.append((subset, len(overlap), len(subset_cps)))

  return results


def _ParseNamelistHeader(lines):
  includes = set()
  for line in lines:
    if not line.startswith('#$'):
      # not functional line, regular comment
      continue
    keyword, args = line.rstrip()[2:].lstrip().split(' ', 1)
    if keyword == 'include':
      includes.add(args)
  return {'lines': list(lines), 'includes': includes}


def GetCodepointFromLine(line):
  assert line.startswith('0x')
  match = _NAMELIST_CODEPOINT_REGEX.match(line[2:7])
  if match is None:
    match = _NAMELIST_CODEPOINT_REGEX.match(line[2:7].upper())
    if match is not None:
      # Codepoints must be uppercase, it's documented
      warn('Found a codepoint with lowercase unicode hex value: 0x{0}'.format(
          match.groups()[0]))
    return None
  return int(match.groups()[0], 16)


def _ParseNamelist(lines):
  cps = set()
  noncodes = set()
  header_lines = []
  reading_header = True
  for line in lines:
    if reading_header:
      if not line.startswith('#'):
        # first none comment line ends the header
        reading_header = False
      else:
        header_lines.append(line)
        continue

    # reading the body, i.e. codepoints
    if line.startswith('0x'):
      codepoint = GetCodepointFromLine(line)
      if codepoint is None:
        # ignore all lines that we don't understand
        continue
      cps.add(codepoint)
      # description
      # line[(2+len(codepoint)),]
    elif line.startswith('      '):
      noncode = line.strip().rsplit(' ')[-1]
      if noncode:
        noncodes.add(noncode)

  header = _ParseNamelistHeader(header_lines)
  return cps, header, noncodes


def ParseNamelist(filename):
  """Parse a given Namelist file.

  Args:
    filename: The path to the Namelist file.

  Returns:
    A tuple of (Codepoints set, header data dict).
  """
  with codecs.open(filename, encoding='utf-8') as nam_file:
    return _ParseNamelist(nam_file)


def _LoadNamelistIncludes(item, unique_glyphs, cache):
  """Load the includes of an encoding Namelist files.

  This is an implementation detail of ReadNameList.

  Args:
    item: A dict representing a loaded Namelist file.
    unique_glyphs: Whether to only include glyphs unique to subset.
    cache: A dict used to cache loaded Namelist files.

  Returns:
    The item with its included Namelists loaded.
  """
  includes = item['includes'] = []
  charset = item['charset'] = set() | item['ownCharset']

  no_charcode = item['noCharcode'] = set() | item['ownNoCharcode']

  dirname = os.path.dirname(item['fileName'])
  for include in item['header']['includes']:
    include_file = os.path.join(dirname, include)
    included_item = None
    try:
      included_item = ReadNameList(include_file, unique_glyphs, cache)
    except NamelistRecursionError:
      continue
    if included_item in includes:
      continue
    includes.append(included_item)
    charset |= included_item['charset']
    no_charcode |= included_item['ownNoCharcode']
  return item


def _ReadNameList(cache, filename, unique_glyphs):
  """Return a dict with the data of an encoding Namelist file.

  This is an implementation detail of ReadNameList.

  Args:
    cache: A dict used to cache loaded Namelist files.
    filename: The path to the  Namelist file.
    unique_glyphs: Whether to only include glyphs unique to subset.

  Returns:
    A dict containing the data of an econding Namelist file.
  """
  if filename in cache:
    item = cache[filename]
  else:
    cps, header, noncodes = ParseNamelist(filename)
    item = {
        'fileName': filename,
        'ownCharset': cps,
        'header': header,
        'ownNoCharcode': noncodes,
        'includes': None,  # placeholder
        'charset': None,  # placeholder
        'noCharcode': None
    }
    cache[filename] = item

  if unique_glyphs or item['charset'] is not None:
    return item

  # full-charset/includes are requested and not cached yet
  _LoadNamelistIncludes(item, unique_glyphs, cache)
  return item


class NamelistRecursionError(Exception):
  """Exception to control infinite recursion in Namelist includes."""
  pass


def _ReadNameListSafetyLayer(currently_including, cache, nam_filename,
                             unique_glyphs):
  """Detect infinite recursion and prevent it.

  This is an implementation detail of ReadNameList.

  Args:
    currently_including: The set of Namelist files that are in the process of
      being included.
    cache: A dict used to cache loaded Namelist files.
    nam_filename: The path to the  Namelist file.
    unique_glyphs: Whether to only include glyphs unique to subset.

  Returns:
    A dict containing the data of an econding Namelist file.

  Raises:
    NamelistRecursionError: If nam_filename is in the process of being included.
  """
  # normalize
  filename = os.path.abspath(os.path.normcase(nam_filename))
  if filename in currently_including:
    raise NamelistRecursionError(filename)
  currently_including.add(filename)
  try:
    result = _ReadNameList(cache, filename, unique_glyphs)
  finally:
    currently_including.remove(filename)
  return result


def ReadNameList(nam_filename, unique_glyphs=False, cache=None):
  """Reads a given Namelist file.

  Args:
    nam_filename: The path to the  Namelist file.
    unique_glyphs: Optional, whether to only include glyphs unique to subset.
    cache: Optional, a dict used to cache loaded Namelist files.

  Returns:
  A dict with following keys:
  "fileName": (string) absolut path to nam_filename
  "ownCharset": (set) the set of codepoints defined by the file itself
  "header": (dict) the result of _ParseNamelistHeader
  "includes":
      (set) if unique_glyphs=False, the resulting dicts of ReadNameList
            for each of the include files
      (None) if unique_glyphs=True
  "charset":
      (set) if unique_glyphs=False, the union of "ownCharset" and all
            "charset" items of each included file
      (None) if unique_glyphs=True

  Raises:
    NamelistRecursionError: If nam_filename is in the process of being included.

  If you are using  unique_glyphs=True and an external cache, don't expect
  the keys "includes" and "charset" to have a specific value.
  Depending on the state of cache, if unique_glyphs=True the returned
  dict may have None values for its "includes" and "charset" keys.
  """
  currently_including = set()
  if not cache:
    cache = {}
  return _ReadNameListSafetyLayer(currently_including, cache, nam_filename,
                                  unique_glyphs)


def CodepointsInNamelist(nam_filename, unique_glyphs=False, cache=None):
  """Returns the set of codepoints contained in a given Namelist file.

  This is a replacement CodepointsInSubset and implements the "#$ include"
  header format.

  Args:
    nam_filename: The path to the  Namelist file.
    unique_glyphs: Optional, whether to only include glyphs unique to subset.
    cache: Optional, a dict used to cache loaded Namelist files.

  Returns:
    A set containing the glyphs in the subset.
  """
  key = 'charset' if not unique_glyphs else 'ownCharset'
  result = ReadNameList(nam_filename, unique_glyphs, cache)
  return result[key]


### unit tests ###


def MakeTestMethod(subset, namelist_filename):
  name = 'test_legacy_subsets_{0}'.format(subset.replace('-', '_'))

  def Test(self):
    """Comapre output of CodepointsInSubset and CodepointsInNamelist.

    The old function CodepointsInSubset and the new function
    CodepointsInNamelist should both output the same sets. This will only work
    as long as the #$inlcude statements in the Namelist files reproduce the old
    dependency logic implemented in CodepointFiles.

    Args:
      self: The test object itself.
    """
    charset_old_method = set(
        hex(c)
        for c in CodepointsInSubset(subset, unique_glyphs=self.unique_glyphs))

    charset_new_method = set(
        hex(c)
        for c in CodepointsInNamelist(
            namelist_filename,
            unique_glyphs=self.unique_glyphs,
            cache=self._cache))
    self.assertTrue(charset_old_method)
    self.assertEqual(charset_old_method, charset_new_method)

  return name, Test


def InitTestProperties(cls):
  initialized = []
  for subset in ListSubsets():
    namelist_filename = CodepointFileForSubset(subset)
    if namelist_filename is None:
      continue
    name, test = MakeTestMethod(subset, namelist_filename)
    setattr(cls, name, test)
    initialized.append(name)
  return initialized


class TestCodepointReading(unittest.TestCase):
  unique_glyphs = True
  _cache = None

  @classmethod
  def setUpClass(cls):
    cls._cache = {}

  @classmethod
  def tearDownClass(cls):
    cls._cache = None


if __name__ == '__main__':
  InitTestProperties(TestCodepointReading)
  unittest.main(argv=sys.argv, verbosity=2)
