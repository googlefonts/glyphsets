#!/bin/sh
set -e

# Go the sources directory to run commands
SOURCE="${BASH_SOURCE[0]}"
DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
cd $DIR

echo "clean-up"
rm -rf ./*/nam/*.nam ./*/txt/*/*.txt ./*/glyphs/*.plist

echo "Updating lists"

scripts=$(ls -d */ | cut -f1 -d'/')

for script in $scripts
do
    echo $script
    sets=$(ls ./$script/glyphs/*.glyphs | xargs -n 1 basename | sed -e 's/\.glyphs$//')
    if [[ $sets == *GF_Latin_Core* ]]
    then
        glyphsets filter-list $sets -o $script/glyphs/CustomFilter_GF_$script.plist
    elif [[ $sets == *GF_TransLatin* ]]
    then
        glyphsets filter-list GF_Latin_Kernel $sets -o $script/glyphs/CustomFilter_GF_$script.plist
    else
        glyphsets filter-list GF_Latin_Core $sets -o $script/glyphs/CustomFilter_GF_$script.plist
    fi
    for set in $sets
    do
        glyphsets nam-file $set -o $script/nam/$set.nam
        glyphsets filter-list $set -o $script/txt/nice-names/$set.txt
        glyphsets filter-list $set -o $script/txt/prod-names/$set.txt --prod-names
    done
done

# Language definition overhaul:
# After all the files were created using the old approach,
# now use the new approach to replace files for those glyphsets
# that are supported under the new approach
python ../scripts/assemble_charactersets.py