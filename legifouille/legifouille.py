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
        # Remove duplicates
        self.struct_articles = list(dict.fromkeys(self.struct_articles))

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

    def print_modifs(self):
        print(",".join(["Date","Type","Texte","Article","URL"]))
        modifs = self.get_modifs()
        for m in modifs:
            modif = modifs[m]
            text = modif.text.replace("\n","").split(" - ")

            print(",".join([modif['datesignatexte'],modif['naturetexte'],text[0],text[1],"https://www.legifrance.gouv.fr/jorf/id/"+modif['cidtexte']]))


    def print_liens(self, allversions = True):
        article_keys = [ "ID", "NUM", "DATE_DEBUT", "ETAT" ]
        lien_keys = [ "id", "typelien", "sens", "datesignatexte", "naturetexte", "numtexte", "num" ]

        header = [ "article_"+a.lower() for a in article_keys ]
        header += [ "lien_"+l for l in lien_keys ]
        header += [ "lien_texte", "lien_url" ]
        print(",".join(header))

        for struct_article in self.struct_articles:
            article = self.get_article(struct_article)
            article_data = [ article.find(key).text for key in  article_keys ]
            if article.find("ETAT").text != "VIGUEUR" and not allversions: continue
            for lien in article.findAll("LIEN"):
                #print(lien)
                lien_data = [ lien[key] for key in lien_keys ]
                if lien_data[-2] == "": lien_data[-2] = '"'+lien.text.split(" - ")[0]+'"'
                url = "https://www.legifrance.gouv.fr/jorf/id/"+lien['cidtexte']
                print(",".join(article_data + lien_data + ['"'+lien.text+'"', url]))


def main():
    code = Code("./LEGI/TEXT/00/00/06/07/11/LEGITEXT000006071191/")

    code.print_liens()


if __name__ == "__main__":
    main()
