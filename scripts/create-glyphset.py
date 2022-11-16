"""Create a new glyphset for a script, by listing all glyphs
with that script code in Unicode."""
import os
import csv
import argparse
import youseedee


EVERYONE_GETS_THESE = [0x00, 0x0D, 0x20, 0x00A0]

parser = argparse.ArgumentParser(description='Add a new glyphset')
parser.add_argument('--no-label', action="store_true", help="Don't emit a representative glyph, just the name")
parser.add_argument('scriptname', metavar='SCRIPTNAME',
                    help='The UCD name for this script')

args = parser.parse_args()
scripts = youseedee.database["Scripts.txt"]["reader"]("Scripts.txt")
script_extensions = youseedee.database["ScriptExtensions.txt"]["reader"]("ScriptExtensions.txt")

aliases = {}
with open(os.path.join(youseedee.ucd_dir(), "PropertyValueAliases.txt"), "r", newline='') as f:
  reader = csv.reader(f, delimiter=';',skipinitialspace=True)
  for row in reader:
    if len(row) != 3:
      continue
    category, short, long_name = row
    if category.strip() != "sc":
      continue
    aliases[long_name.strip()] = short.strip()

if args.scriptname not in aliases:
  print(f"Are you sure {args.scriptname} is a Unicode script? It has no short alias")
  sys.exit(1)

shortname = aliases[args.scriptname]
todo = EVERYONE_GETS_THESE

for start, end, script in scripts:
  if script == args.scriptname:
    todo.extend(list(range(start, end+1)))

for start, end, scripts in script_extensions:
  if shortname in scripts:
    todo.extend(list(range(start, end+1)))

for codepoint in sorted(set(todo)):
  data = youseedee.ucd_data(codepoint)
  name = data.get("Name")
  if args.no_label or codepoint in EVERYONE_GETS_THESE:
    label = ""
  else:
    label = chr(codepoint)
    if data.get("General_Category") == "Mn":
      label = chr(0x25CC) + label
  print("0x%04X  %s %s" % (codepoint, label, name))
