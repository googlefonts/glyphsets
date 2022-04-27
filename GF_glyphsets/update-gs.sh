#!/bin/sh
set -e

echo "Updating lists"

scripts=$(ls -d */ | cut -f1 -d'/')

for script in $scripts
do
    echo $script
    sets=$(ls ./$script/glyphs/*.glyphs | xargs -n 1 basename | sed -e 's/\.glyphs$//')
    glyphsets filter-list GFLatin_Core $sets -o $script/glyphs/GF$script.plist

    for set in $sets
    do
        glyphsets nam-file $set -o $script/nam/$set.nam
        glyphsets filter-list $set -o $script/txt/$set.txt --prod-names
    done
done
