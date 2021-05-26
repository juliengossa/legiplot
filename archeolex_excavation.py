import datetime
import argparse
from re import A
import ArcheoLexLog
import sys
import csv

def main(argv):
    parse = argparse.ArgumentParser()
    parse.add_argument("-d","--datelimit", metavar="YYYY-MM-DD",
                        help="Définit une date maximum pour la fouille")
    parse.add_argument("-f","--file", metavar="fichier.csv", type=str,
                        help="Ecrit les données dans un fichier csv (sortie standard par défaut)")
    parse.add_argument("-t","--fulltext",dest='PLTC_method', action='store_const',
                        const="fulltext", default="code",
                        help='Détecte les noms entiers des sections')
    parse.add_argument("traitement", metavar="diff|check", nargs=1,
                        help='Le traitement à effectuer')
    parse.add_argument("codes", metavar="code", nargs='+',
                        help="La liste des codes à fouiller")
    parse.add_argument("-v","--verbose",dest='verbose', action='store_const',
                        const=True, default=False,
                        help='Enregistre tous les fichiers intermédiaires')
    args = parse.parse_args(argv)

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

if __name__=="__main__":
    main(sys.argv[1:])
