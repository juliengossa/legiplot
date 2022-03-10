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

from ae_article import AEArticle
from ae_version import AEVersion

class AELog:
    def __init__(self, code, csvwriter, csvwriter2, verbose, print_progression):
        self.code = code
        self.csvwriter = csvwriter
        self.csvwriter2 = csvwriter2
        self.verbose = verbose
        self.print_progression = print_progression

    def create_repo(self):
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

        self.repo = repo


    def process_code(self,traitement,datelimit,shrink,PLTC_method,jump):
        """Obtenir tous les versions d'un code et pour chaque version un getDiff()
        """
        self.create_repo()

        # obtenir tous les version
        commit_log = self.repo.git.log('--pretty={"%h"}')
        log_list = commit_log.split("\n")

        # gestion du last
        if datelimit[0] == "last":
            log_list = [log_list[0]]

        log_list.reverse() #ordre chronologique

        articles = {}

        AEVersion.reset()

        for ilog,log in enumerate(log_list):
            commit_number = "".join(re.findall(r"{\"(.+?)\"}",log))
            commit = self.repo.commit(commit_number)

            ae_version = AEVersion(self.code,self.repo,commit,self.verbose,PLTC_method)

            # sys.stderr.write(" - "+ae_version.get_date()+" / "+datelimit[0]+"\n")

            # saut de versions
            if datelimit == []: break
            if ae_version.get_date() < datelimit[0] and ilog != len(log_list)-1: continue
            else:
                if jump:
                    datelimit = datelimit[1:]


            if self.print_progression:
                sys.stderr.write("\r"+self.code+" "+ae_version.get_date()+" " * 50)

            ae_version.process(traitement)

            if self.csvwriter2 is not None:
                articles = ae_version.get_shrink(traitement,0)
                for article in articles:
                    self.csvwriter2.writerow(article.get_values(traitement,0))

            articles = ae_version.get_shrink(traitement,shrink)
            for article in articles:
                self.csvwriter.writerow(article.get_values(traitement,shrink))


        # if traitement == "diff" and shrink == 0:
        #     commit = commit.parents[0]
        #     ae_version = AEVersion(commit)
        #     articles = ae_version.process_version(commit,"stats",0)
        #     for article in articles.values():
        #         article.type_modification = "Préexistence"
        #         csvwriter.writerow(article.get_values(traitement))
