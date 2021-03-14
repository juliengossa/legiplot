#!/bin/bash

# Pour un affichage correct des caractères spéciaux
# git config --global core.quotepath off


gitlog2csv () {
  IFS=''
  git log --pretty='format:%as,"%s"' --stat | \
  grep -v README | grep -v changed | grep -v "=>" | \
  while read line; do
    if [ -z "$line" ]; then continue ; fi
    if [ "${line:0:1}" != " " ]; then
      prefix="$line"
    else
      file=`echo $line | tr -s " " | awk '{print $1}'`
      modif=`echo $line | tr -s " " | awk '{print $3}'`
      echo \"$CODE\",$prefix,\"$file\",$modif
    fi
  done
}

if [ -z $1 ]; then
  CODES="code_de_l'éducation"
else
  CODES="$*"
fi

echo "Dossier,Date,Commit,Article,LignesModifiées"

mkdir archeolex 
cd archeolex

for CODE in $CODES
do

  git clone "https://archeo-lex.fr/codes/${CODE}" 1>&2
  cd "${CODE}" 1>&2
  git pull 1>&2
  
  gitlog2csv
  cd ..
  
done

