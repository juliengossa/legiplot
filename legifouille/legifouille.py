# MIT License
#
# Copyright (c) 2023 Julien Gossa
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

#!/usr/bin/env python

import json
import os
import sys
from io import StringIO
from datetime import datetime
from bs4 import BeautifulSoup
import csv
import argparse

def get_soup(file):
    try:
        with open(file, "r") as f:
            soup = BeautifulSoup(f.read(),features="xml")
        return soup
    except:
        print("Missing file: "+file, file=sys.stderr)
        return BeautifulSoup()


class LEGI:
    struct_article_keys = [ "num", "etat", "debut", "fin", "id" ]
    struct_article_header = struct_article_keys

    article_keys = [ "NUM", "DATE_DEBUT", "DATE_FIN", "ETAT" ]
    article_header = [ "article_"+a.lower() for a in article_keys ]
    
    lien_keys = [ "id", "typelien", "sens", "datesignatexte", "naturetexte", "numtexte", "num" ]
    lien_header = [ "lien_"+l for l in lien_keys ] + [ "lien_texte", "lien_url" ]

    def __init__(self, liens=False):
        self.liens = liens
        self.csvwriter = csv.writer(sys.stdout)
        if not liens:
            self.csvwriter.writerow(self.struct_article_header)            
        else:
            self.csvwriter.writerow(self.article_keys + self.lien_header)

        self.articles = {}
            
    def parse_code(self, path):
        self.path = path
        self.root = path+"texte/struct/"+os.listdir(path+"texte/struct/")[0]

        self.articles[path] = []

        self.parse_struct(self.root)
    
    def parse_struct(self, node, depth=0):
        #print("  "*depth + node)
        soup = get_soup(node)

        struct_articles = soup.findAll("LIEN_ART")
        for struct_article in struct_articles:
            struct_article_data = [ struct_article[key] for key in self.struct_article_keys ]
            if struct_article['id'] in self.articles[self.path]: continue
            self.articles[self.path].append(struct_article['id'])

            if not self.liens:
                self.csvwriter.writerow(struct_article_data)
            else: 
                if struct_article['etat'] == "VIGUEUR":
                    self.parse_article_liens(struct_article)

        sections = soup.findAll("LIEN_SECTION_TA")
        for section in sections:
            self.parse_struct(self.path + "section_ta" + section['url'], depth+1)

    def parse_article_liens(self, struct_article):
        article = self.get_article(struct_article)

        article_data = [ article.find(key).text for key in self.article_keys ]

        vigueur = (article.find("ETAT").text == "VIGUEUR") 
        for lien in article.findAll("LIEN"):
            if lien['typelien'] != "MODIFIE" and not vigueur: continue
            
            lien_data = [ lien[key] for key in self.lien_keys ]
            if lien_data[-2] == "": lien_data[-2] = lien.text.split(" - ")[0]
            url = "https://www.legifrance.gouv.fr/jorf/id/"+lien['cidtexte']
            self.csvwriter.writerow(article_data + lien_data + [lien.text, url])

    def get_article(self,struct_article):
        num = struct_article['id'].replace("LEGIARTI","")
        sp = "/".join([ num[i:i+2] for i in range(0,10,2) ])

        apath = self.path + "article/"+struct_article['origine']+"/ARTI/" + sp + "/" + struct_article['id'] + ".xml"

        return get_soup(apath)

code_path = {
    'éducation':"LEGI/legi/global/code_et_TNC_en_vigueur/code_en_vigueur/LEGI/TEXT/00/00/06/07/11/LEGITEXT000006071191/"
}

def main():
    parser = argparse.ArgumentParser(description='Parser de la base LEGI')
    parser.add_argument('-l', '--liens', help='extrait les liens des articles en vigueur plutôt que les versions', action='store_true', default=False)
    parser.add_argument('codes', type=str, help='Code to parse', nargs='*', default=['éducation'])
    args = parser.parse_args()

    legi = LEGI(args.liens)
    for code in args.codes:
        legi.parse_code(code_path[code])

if __name__ == "__main__":
    main()
