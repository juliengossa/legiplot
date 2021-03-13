#!/bin/bash

git clone https://github.com/etalab/codes-juridiques-francais.git

echo "Date,Loi,Section,Article,LignesModifiées"

cd "codes-juridiques-francais/codes-en-vigueur/code-de-l-education"
subdirs=`find . -name '*.md' | grep -v README | sed 's/\/[^\/]*\.md//' | uniq`
for dir in $subdirs; do
  git log --pretty='format:%as,"%s"' --stat $dir | \
    grep -v README | grep -v changed | grep -v "=>" | \
    while read line; do
      if [ -z "$line" ]; then continue ; fi
      if [ ${line:0:1} == "2" ]; then
        prefix="$line"
      else
        file=`echo $line | cut -f1 -d" " | sed 's/.*\///g'`
        modif=`echo $line | cut -f3 -d" "`
        echo $prefix,\"$dir\",\"$file\",$modif
      fi
    done
done