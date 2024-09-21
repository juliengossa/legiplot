#! /bin/bash

mkdir LEGI
cd LEGI

alreadydl=`ls *.tar.gz`

wget -r --no-parent -A.tar.gz -nc --no-directories -P . https://echanges.dila.gouv.fr/OPENDATA/LEGI/ 

if [ `ls Freemium* | wc -l` -ne 1 ]; then
    echo "Plusieurs global: supprimez les anciens"
    exit -1
fi

if [[ $alreadydl != *Freemium* ]]; then
    tar -xvf  Freemium* ./legi/global/code_et_TNC_en_vigueur
fi

for f in `ls -1 LEGI*.tar.gz`; do
    if [[ $alreadydl != *$f* ]]; then
        echo $f
        tar -xvf $f --wildcards '*legi/global/code_et_TNC_en_vigueur' --strip-components 1 > /dev/null
    fi
done