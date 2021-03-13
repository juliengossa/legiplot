#!/bin/bash

git clone "https://archeo-lex.fr/codes/code_de_l'éducation" 1>&2
cd "code_de_l'éducation" 1>&2
git pull 1>&2

echo "Date,Loi,Section,Article,LignesModifiées"

git log --pretty='format:%as,"%s"' --stat | \
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
