from Article import Article
from datetime import datetime
import os
import re
import git
import dateparser
import csv
import sys
import string
import shutil
import copy
import tempfile

class ArcheoLexLog:
    def __init__(self, code, verbose=False, PLTC_method="code"):
        self.code=code
        self.verbose=verbose
        self.PLTC_method=PLTC_method

        self.word_translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))

    def createRepo(self):
        """Créer ou mettre à jour un dossier contenant les codes requises
        on clone les codes requis sur git et les place dqns les dossier
        correspondant de archeo_lex,Si un code existe déjà,exécute git pull
        Arg:
        returns: le dépôt GIT du code
        Raises：
        IOError:une erreur se produit lorsque on entre les mauvais noms
        GitCommandError:une erreur se produit lorsque il y a un merge
        """
        dir_path=sys.path[0]
        path=dir_path+'/archeo_lex/'+self.code

        try:
            repo = git.Repo.clone_from(url ='https://archeo-lex.fr/codes/'+self.code,to_path=path)
        except git.GitCommandError as gce:
            if "already exists and is not an empty directory" in gce.stderr:
                try:
                    repo = git.Repo(path)
                    repo.git.fetch()
                    repo.git.reset("--hard")
                except git.InvalidGitRepositoryError as gre:
                    sys.stderr.write("Problème avec le dossier "+path+"\n")
                    sys.exit(1)
            else:
                sys.stderr.write("Erreur avec "+self.code+" : "+gce.stderr+"\n")
                sys.exit(1)

        return repo


    def getVersion(self,commit):
        sha=commit.hexsha
        short_sha=self.repo.git.rev_parse(sha, short=7)
        version = short_sha
        return version

    def getDate(self,commit):
        date_fr=" ".join(re.findall('(?<=au).*$',commit.message))
        date=dateparser.parse(date_fr).date().strftime("%Y-%m-%d")
        return date

    def getDifflines(self,commit):
        """Obtenir les différences entre cette version et la version précédentes

            Arg:
                commit:Commit(type) numéro de version

            return:
                lines:list des informations différentes
        """
        diff = commit.parents[0].diff(commit, create_patch=True, unified=100000000).pop()
        cmp = diff.diff.decode('utf-8').splitlines()
        return list(cmp)

    def getLines(self,commit):
        """Obtenir les lignes de cette version

            Arg:
                commit:Commit(type) numéro de version

            return:
                lines:liste des lignes
        """
        lignes = commit.tree[0].data_stream.read().decode('utf-8').splitlines()
        return list(lignes)

    @staticmethod
    def _getTypeLine(line):
        if line.startswith('-'):             # -######Article est Supression
            type_line = "Suppression"
        elif line.startswith('+'):           # +######Article est Ajout
            type_line = "Ajout"
        else:
            type_line = None
        return type_line

    def processDiff(self,commit):
        """Obtenez toutes les modifications d'une version d'un code

            Parcourez les informations de différence, nous extrayons les informations
            correspondantes du nom de l'article

            Arg:
                commit: Commit de version

            return:
                mods:dict qui répresente une modification(un dict)
        """
        #get la version et la date
        date = self.getDate(commit)
        version = self.getVersion(commit)
        #get lines in diff
        lines=self.getDifflines(commit)
        if self.verbose:
            tf = tempfile.NamedTemporaryFile(suffix='.csv', prefix=os.path.basename(__file__))
            tf_dir = os.path.dirname(tf.name)

            with open(tf_dir+'/'+self.code+'-'+date+'.txt', 'w',encoding="utf-8") as verbfile:
                verbfile.write('\n'.join(str(line) for line in lines))

        curmod = None # modification courante
        cursec = [] # section courante
        mods = {}

        for num,line in enumerate(lines):
            # Détection du type de la ligne
            type_line = self._getTypeLine(line)

            # Si changement de section, enregistrer la nouvelle section
            if (len(line) > 2 and line[1] == '#'):
                level = line.count("#")
                cursec = cursec[:level-1]+[re.sub(".*# ","",line)]

                # Si changement d'article
                if line.find("Article") != -1:
                    # Si une modification a été détectée, l'enregistrer
                    if curmod is not None and curmod.type_modification is not None:
                        if curmod.article in mods:
                            nbm = mods[curmod.article].nb_modifications + curmod.nb_modifications
                            if nbm == 0:
                                del mods[curmod.article]
                            else:
                                mods[curmod.article].type_modification = "Modification"
                                mods[curmod.article].nb_modifications = nbm
                        else:
                            mods[curmod.article] = curmod

                    # Réinitialiser la modification courante
                    curmod = Article(self.code, date, version, cursec, self.PLTC_method)
                    curmod.type_modification = type_line


            # Si pas de changement de section, on vérifie juste s'il n'y a pas de modifications,
            # dans une ligne non vide
            elif type_line is not None and len(line[1:].strip()) > 0 and curmod is not None:
                if curmod.type_modification is None : curmod.type_modification = "Modification"
                curmod.nb_modifications += 1

        if curmod is not None and curmod.type_modification is not None:
            if curmod.article not in mods:
                mods[curmod.article] = curmod

        return mods

    def processVersion(self,commit,traitement,shrink=0):
        """Obtenez toutes les erreurs d'une version d'un code
            Arg:
                commit: Commit de version
                traitement: Traitement à appliquer (check ou stats)
        """
        #get la version et la date
        date = self.getDate(commit)
        version = self.getVersion(commit)
        cursec = [] # section courante
        resultat = {}
        article_precedent = None

        #get lines du code
        lines=self.getLines(commit)
        if self.verbose:
            with open(self.code+'-'+date+'.txt', 'w',encoding="utf-8") as verbfile:
                verbfile.write('\n'.join(str(line) for line in lines))

        nbs = [1,1,1,1,1,1,1,1]
        article_precedent = None

        for num,line in enumerate(lines):
            # Si changement de section, enregistrer la nouvelle section
            if len(line) == 0: continue

            # Si c'est une ligne normale on fait les statistiques
            if line[0] != '#': # and traitement == "stats" or traitement == "finestats":
                article.nb_lignes += 1
                article.nb_mots += len(line.translate(self.word_translator).split())

            # Si c'est un changement de section
            else:
                level = line.count("#")
                cursec = cursec[:level-1]+[re.sub(".*# ","",line)]

                # Si changement d'article
                if line.find("Article") != -1:
                    article = Article(self.code, date, version, cursec, PLTC_method = self.PLTC_method)

                    # Test erreurs
                    cmp = article.compareNum(article_precedent)
                    if cmp == "eq":
                        article.type_erreur = "doublon"
                    if cmp == "lt":
                        article.type_erreur = "inversion"
                        article.info_erreur = article_precedent.article

                    # Ajout à la sortie
                    if traitement == "check" and article.type_erreur is not None:
                        resultat[article.article] = article

                    if traitement == "stats" and article.type_erreur != "doublon" and article_precedent != None:
                        ap = article_precedent
                        nbs[-1] += ap.nb_mots
                        nbs[-2] += ap.nb_lignes
                        #print(nbs)

                        if shrink == 0 or (shrink < 6 and article.getSections()[0:-(shrink)] != ap.getSections()[0:-(shrink)]):
                            nbs[0:-2-shrink] = ap.getSections()[0:6-shrink]
                            (ap.partie,ap.sous_partie,ap.livre,ap.titre,ap.chapitre,ap.article,ap.nb_lignes,ap.nb_mots) = nbs
                            resultat[str(len(resultat))] = ap

                            nbs = [0,0,0,0,0,0,0,0]

                        for i in range(6-shrink,6):
                            if article.getSections()[i] is None or ap.getSections()[i] is None:
                                continue
                            if article.getSections()[i] != ap.getSections()[i]:
                                nbs[i] += 1
                                #print(str(i)+' '+str(nbs)+' : '+article.getSections()[i]+' vs '+ap.getSections()[i])

                    article_precedent = article

        if traitement == "stats" and article_precedent is not None:
            ap = article
            nbs[-1] += ap.nb_mots
            nbs[-2] += ap.nb_lignes
            nbs[0:-2-shrink] = ap.getSections()[0:6-shrink]
            (ap.partie,ap.sous_partie,ap.livre,ap.titre,ap.chapitre,ap.article,ap.nb_lignes,ap.nb_mots) = nbs
            resultat[str(len(resultat))] = ap

        return resultat


    def processCode(self,datelimit,csvwriter,traitement="check",shrink=0,print_progression=False):
        """Obtenir tous les versions d'un et pour chaque version on fonction getDiff()
        """
        self.repo = self.createRepo()

        #obtenir tous les version
        commit_log = self.repo.git.log('--pretty={"%h"}')
        log_list = commit_log.split("\n")

        if traitement == "diff":
            log_list.pop()  #supprimer la version la plus ancienne

        if traitement == "check":
            log_list.reverse()  #ordre chronologique

        articles = {}
        seen_articles = []

        for log in log_list:
            commit_number ="".join(re.findall(r"{\"(.+?)\"}",log))
            commit=self.repo.commit(commit_number)
            date=self.getDate(commit)

            if print_progression:
                sys.stderr.write("\r"+self.code+" "+date+" " * 50)

            if traitement == "diff":
                articles = self.processDiff(commit)
            else:
                articles = self.processVersion(commit,traitement,shrink)

            if traitement == "check":
                for sa in seen_articles:
                    if sa in articles: del articles[sa]
                seen_articles += articles.keys()

            for article in articles.values():
                csvwriter.writerow(article.getValues(traitement))

            if datelimit != None:
                if datelimit == "last": break
                if traitement != "check" and date < datelimit: break
                if traitement == "check" and date > datelimit: break

        if traitement == "diff" and shrink == 0:
            commit = commit.parents[0]
            articles = self.processVersion(commit,"stats",0)
            for article in articles.values():
                article.type_modification = "Préexistence"
                csvwriter.writerow(article.getValues(traitement))
