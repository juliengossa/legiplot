import datetime
import argparse
from re import A
import sys
import csv

from ae_log import AELog
from ae_article import AEArticle

def main(argv):
    parse = argparse.ArgumentParser()
    parse.add_argument("-d","--datelimit", metavar="YYYY-MM-DD|last [YYYY-MM-DD...]", nargs='+',
                        help="Définit une date maximum pour la fouille. 'last' pour n'avoir que la dernière version.",
                        default=["0000-00-00"])
    parse.add_argument("-j","--jump", dest='jump', action='store_const',
                        const=True, default=False,
                        help="Ne compare qu'entre les dates données")
    parse.add_argument("-f","--file", metavar="fichier.csv", type=str,
                        help="Ecrit les données dans un fichier csv (sortie standard par défaut)")
    parse.add_argument("-i","--ifile", metavar="fichier2.csv", type=str,
                        help="Ecrit les données intermédiaires (avant compression) dans un fichier csv")
    parse.add_argument("-t","--fulltext", dest='PLTC_method', action='store_const',
                        const="fulltext", default="code",
                        help='Détecte les noms entiers des sections')
    parse.add_argument("traitement", metavar="diff|check|stats", nargs=1,
                        help='Le traitement à effectuer')
    parse.add_argument("-s","--shrink", metavar="niveau", type=int, default=0,
                        help="Définit un niveau de réduction de la sortie entre 0 et 6 (défaut 1)")
    parse.add_argument("codes", metavar="code [code...]", nargs='+',
                        help="La liste des codes à fouiller")
    parse.add_argument("-v","--verbose", dest='verbose', action='store_const',
                        const=True, default=False,
                        help='Enregistre tous les fichiers intermédiaires')
    args = parse.parse_args(argv)

    args.shrink = min(args.shrink,6)


    if args.file is None:
        fh = sys.stdout
    else:
        fh = open(args.file, 'w', newline='',encoding='utf-8')
    csvwriter = csv.writer(fh)
    csvwriter.writerow(AEArticle.get_header(args.traitement[0],args.shrink))

    csvwriter2 = None
    if args.ifile is not None:
        fh2 = open(args.ifile, 'w', newline='',encoding='utf-8')
        csvwriter2 = csv.writer(fh2)
        csvwriter2.writerow(AEArticle.get_header(args.traitement[0],0))

    for code in args.codes:
        aelog = AELog(code, csvwriter, csvwriter2, args.verbose, args.file is not None)
        aelog.process_code(args.traitement[0], args.datelimit, args.shrink, args.PLTC_method, args.jump)

    fh.close()
    if csvwriter2 is not None: fh2.close()

if __name__=="__main__":
    main(sys.argv[1:])
