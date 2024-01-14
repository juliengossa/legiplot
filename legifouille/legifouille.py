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
from io import StringIO
from datetime import datetime
from bs4 import BeautifulSoup

def get_soup(file):
    with open(file, "r") as f:
        soup = BeautifulSoup(f.read(),features="xml")
    return soup



class Code:
    def __init__(self, path):
        self.path = path
        self.struct_articles = self.get_struct_articles(path+"texte/struct/"+os.listdir(path+"texte/struct/")[0])

    def get_struct_articles(self,structfile):
        soup = get_soup(structfile)
        struct_articles = soup.findAll("LIEN_ART")

        sections = soup.findAll("LIEN_SECTION_TA")
        for section in sections:
            struct_articles += self.get_struct_articles(self.path + "section_ta" + section['url'])

        return struct_articles

    def get_article(self,struct_article):
        num = struct_article['id'].replace("LEGIARTI","")
        sp = "/".join([ num[i:i+2] for i in range(0,10,2) ])

        apath = self.path + "article/"+struct_article['origine']+"/ARTI/" + sp + "/" + struct_article['id'] + ".xml"

        return get_soup(apath)

    def get_liens_modif(self,article):
        liens = article.findAll("LIEN")
        return [ lien for lien in liens if lien['typelien']=="MODIFIE" and lien['sens'] == "cible" ]

    def get_modifs(self):
        modifs = {}
        for struct_article in self.struct_articles:
            article = self.get_article(struct_article)
            for modif in self.get_liens_modif(article):
                modifs[modif['cidtexte']] = modif

        return modifs


def main():
    code = Code("./LEGI/TEXT/00/00/06/07/11/LEGITEXT000006071191/")

    print(",".join(["Date","Type","Texte","Article","URL"]))
    modifs = code.get_modifs()
    for m in modifs:
        modif = modifs[m]
        text = modif.text.replace("\n","").split(" - ")

        print(",".join([modif['datesignatexte'],modif['naturetexte'],text[0],text[1],"https://www.legifrance.gouv.fr/jorf/id/"+modif['cidtexte']]))

if __name__ == "__main__":
    main()
