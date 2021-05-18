#!/usr/bin/env python
# -*- coding: utf-8 -*
# But:Imprimer les lignes différentes de une version d'un code dans un file
# les paramètres entrés par l'utilisateur: -v version -code nom du code -file nom du file

import ArcheoLexLog
import argparse
  
if __name__=="__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("-v","--version",help="donne une version à traiter",required=True)
    parse.add_argument("-csv","--file",type=str,help="spécifier une fichier csv pour écrire la sortie s'il existe pas,on le créer")
    parse.add_argument("-code",help="un code à traiter",required=True)
    args =parse.parse_args()

    archeoLexLog =ArcheoLexLog.ArcheoLexLog(args.code)
    archeoLexLog.createRepo()
    archeoLexLog.create_csv(args.file)
    archeoLexLog.getDiff(args.version,args.file)