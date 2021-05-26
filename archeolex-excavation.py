import datetime
import argparse
from re import A
import ArcheoLexLog
import sys
import csv

if __name__=="__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("-d","--datelimit",help="donne une date à ne pas dépasser")
    parse.add_argument("-f","--file", type=str,
                        help="spécifier une fichier csv pour écrire la sortie s'il existe pas,on le créer")
    parse.add_argument("-t","--fulltext",dest='PLTC_method', action='store_const',
                        const="fulltext", default="code",
                        help='Produit des informations de debug')
    parse.add_argument("traitement", metavar="diff|check", nargs=1, help='Traitement à effectuer')
    parse.add_argument("codes", metavar="code", nargs='+',help="une list de codes")
    parse.add_argument("-v","--verbose",dest='verbose', action='store_const',
                        const=True, default=False,
                        help='Produit des informations de debug')
    args = parse.parse_args()

    if args.file is None:
        fh = sys.stdout
    else:
        fh = open(args.file, 'w', newline='',encoding='utf-8')
    csvwriter = csv.writer(fh)
    ArcheoLexLog.ArcheoLexLog.outputHeader(csvwriter)

    for code in args.codes:
        archeoLexLog = ArcheoLexLog.ArcheoLexLog(code, args.verbose, args.PLTC_method)
        archeoLexLog.processCode(args.datelimit, csvwriter, args.traitement[0], args.file is not None)

    fh.close()
