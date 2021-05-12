import datetime  
import argparse
from re import A
import ArcheoLexLog
import os

if __name__=="__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("-d","--datelimit",type=datetime.date.fromisoformat,help="donne une date à ne pas dépasser")
    parse.add_argument("-csv","--file",type=str,help="spécifier une fichier csv pour écrire la sortie s'il existe pas,on le créer")
    parse.add_argument("-codes","--codesList",nargs='+',help="un list de codes",required=True)
    args =parse.parse_args()
    
    ArcheoLexLog.ArcheoLexLog.create_csv(args.file)
          
    for code in args.codesList:
        archeoLexLog =ArcheoLexLog.ArcheoLexLog(code)
        archeoLexLog.processCode(args.datelimit,args.file)
