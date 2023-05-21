
from datetime import datetime
import os
import re
import git
import dateparser
import csv
import sys
import shutil
import copy
import tempfile
import hashlib

from ae_article import AEArticle

class AEVersion:

    articles_precedents = None
    articles_vus = []

    @staticmethod
    def reset():
        AEVersion.articles_precedents = None
        AEVersion.articles_vus = []

    def __init__(self, code, repo, commit, verbose, PLTC_method):
        self.code = code
        self.repo = repo
        self.commit = commit
        self.verbose = verbose
        self.PLTC_method = PLTC_method

        self.articles = {}

    def get_version(self):
        sha = self.commit.hexsha
        return self.repo.git.rev_parse(sha, short=7)

    @staticmethod
    def get_date_commit(commit):
        date_fr=" ".join(re.findall('(?<=au).*$',commit.message))
        date = dateparser.parse(date_fr).date().strftime("%Y-%m-%d")
        return date

    def get_date(self):
        return self.get_date_commit(self.commit)

    def get_lignes(self):
        lignes = self.commit.tree[0].data_stream.read().decode('utf-8').splitlines()

        if self.verbose:
            with open(self.code+'-'+date+'.txt', 'w',encoding="utf-8") as verbfile:
                verbfile.write('\n'.join(str(ligne) for ligne in lignes))

        return list(lignes)

    def finalize_and_add(self,article):
        if article is None: return
        if article in self.articles:
            self.articles[article].type_erreur = "Doublon"
        else:
            article.finalize()
            self.articles[article.article] = article

    def get_articles(self):
        #get la version et la date
        date = self.get_date()
        version = self.get_version()
        cursec = [] # section courante
        curlignes = ''
        article = None

        #get lignes du code
        lignes = self.get_lignes()

        for num,ligne in enumerate(lignes):
            if len(ligne) == 0: continue

            # Changement de section
            if ligne[0] == '#':
                level = ligne.count("#")
                cursec = cursec[:level-1]+[re.sub(".*# ","",ligne)]

                if ligne.find("Article") != -1:
                    if article is not None:
                        self.finalize_and_add(article)
                    article = AEArticle(self.code, date, version, cursec, PLTC_method = self.PLTC_method)

            # Pas de changement de section
            else:
                article.lignes += ligne + '\n'

        self.finalize_and_add(article)

        return self.articles

    def process_check(self):
        a = list(self.articles.values())
        for i in range(1,len(a)):
            if a[i].compare_num(a[i-1]) == "lt":
                self.articles[a[i].article].type_erreur = "Inversion"

    def process_diff(self):
        if AEVersion.articles_precedents is None:
            for a in self.articles:
                self.articles[a].type_modification = "Préexistence"
        else:
            for a in self.articles:
                if a in AEVersion.articles_precedents:
                    if not self.articles[a].equals(AEVersion.articles_precedents[a]):
                        self.articles[a].type_modification = "Modification"
                else:
                    self.articles[a].type_modification = "Ajout"
            for a in set(AEVersion.articles_precedents) - set(self.articles):
                AEVersion.articles_precedents[a].type_modification = "Suppression"
                AEVersion.articles_precedents[a].date = self.get_date()
                self.articles[a] = AEVersion.articles_precedents[a]


    def get_shrink(self,traitement,shrink):

        if shrink < 0 or (traitement == "stats" and shrink == 0):
            return self.articles.values()

        resultat = []

        if traitement == "check":
            for a in self.articles:
                if self.articles[a].type_erreur is not None and a not in AEVersion.articles_vus:
                    resultat += [self.articles[a]]
                    AEVersion.articles_vus += a

        elif traitement == "diff" and shrink == 0:
            for a in self.articles:
                if self.articles[a].type_modification is not None:
                    resultat += [self.articles[a]]

        else:
            res = {}
            for a in self.articles.values():
                #(a.partie,a.sous_partie,a.livre,a.titre,a.chapitre,a.article) = \[a.partie,a.sous_partie,a.livre,a.titre,a.chapitre,a.article][0:-shrink] + ["NA"]*shrink
                k = ":".join([a.partie,a.sous_partie,a.livre,a.titre,a.chapitre,a.article][0:-shrink])

                try:
                    stat = res[k]
                    stat.nb_mots += a.nb_mots
                    stat.nb_lignes += a.nb_lignes
                    if a.type_modification != "Suppression": stat.nb_articles += 1
                    try:
                        stat.nb_modifications[a.type_modification] += 1
                    except KeyError:
                        stat.nb_modifications[a.type_modification] = 1
                    # if a.type_modification is not None:
                    #     print(k+' : '+str(a.type_modification)+' : '+str(stat.nb_modifications[a.type_modification]))
                except KeyError:
                    # print("keyerror : "+k+' : '+ str(k in res))
                    a.nb_modifications[a.type_modification] = 1
                    res[k] = a

            resultat = res.values()

        return resultat


    def process(self,traitement):
        """ Traite une version de code
            Arg:
                commit: Commit de version
                traitement: Traitement à appliquer (check ou stats)
                shrink: niveau de compression de la sortie
        """

        self.get_articles()
        self.articles_wo_suppr = self.articles.copy()

        if traitement == "check": self.process_check()
        if traitement == "diff": self.process_diff()
        #if traitement == "stats": self.process_diff()
        AEVersion.articles_precedents = self.articles_wo_suppr

        #             # Ajout à la sortie
        #             if traitement == "check" and article.type_erreur is not None:
        #                 resultat[article.article] = article
        #
        #             if traitement == "hashdiff" and article.lignes != '':
        #                 m = hashlib.sha1()
        #                 m.update(article.lignes.encode('utf-8'))
        #                 article.digest = m.digest
        #
        #                 if article.article in articles_precedents:
        #                     if article.digest != articles_precedents[article.article].digest:
        #                         article.type_modification = "Modification"
        #                 else:
        #                     article.type_modification = "Ajout"
        #
        #                 resultat[article.article] = article
        #
        #             if traitement == "stats" and article.type_erreur != "doublon" and article_precedent != None:
        #                 ap = article_precedent
        #                 nbs[-1] += ap.nb_mots
        #                 nbs[-2] += ap.nb_lignes
        #                 #print(nbs)
        #
        #                 if shrink == 0 or (shrink < 6 and article.get_sections()[0:-(shrink)] != ap.get_sections()[0:-(shrink)]):
        #                     nbs[0:-2-shrink] = ap.get_sections()[0:6-shrink]
        #                     (ap.partie,ap.sous_partie,ap.livre,ap.titre,ap.chapitre,ap.article,ap.nb_lignes,ap.nb_mots) = nbs
        #                     resultat[str(len(resultat))] = ap
        #
        #                     nbs = [0,0,0,0,0,0,0,0]
        #
        #                 for i in range(6-shrink,6):
        #                     if article.get_sections()[i] is None or ap.get_sections()[i] is None:
        #                         continue
        #                     if article.get_sections()[i] != ap.get_sections()[i]:
        #                         nbs[i] += 1
        #                         #print(str(i)+' '+str(nbs)+' : '+article.get_sections()[i]+' vs '+ap.get_sections()[i])
        #
        #             article_precedent = article
        #
        # if traitement == "stats" and article_precedent is not None:
        #     ap = article
        #     nbs[-1] += ap.nb_mots
        #     nbs[-2] += ap.nb_lignes
        #     nbs[0:-2-shrink] = ap.get_sections()[0:6-shrink]
        #     (ap.partie,ap.sous_partie,ap.livre,ap.titre,ap.chapitre,ap.article,ap.nb_lignes,ap.nb_mots) = nbs
        #     resultat[str(len(resultat))] = ap
        #
        # if traitement == "hashdiff":
        #     for a in articles_precedents:
        #         if a not in articles:
        #             article = articles_precedents[a]
        #             article.type_modification = "Suppression"
        #             resultat[a] = article
        #
        # return resultat
