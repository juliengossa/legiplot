from datetime import datetime
import os
import re
import git
import difflib
import dateparser
import csv
import sys
from git.compat import defenc
from pathlib import Path

class ArcheoLexLog:
    def __init__(self,code, verbose=False, PLTC_method="code"):
        self.code=code
        self.verbose=verbose
        self.PLTC_method=PLTC_method

    def createRepo(self):
        """Créer ou mettre à jour un dossier contenant les codes requises

        on clone les codes requis sur git et les place dqns les dossier
        correspondant de archeo_lex,Si un code existe déjà,exécute git pull

        Arg:

        returns:

        Raises：
        IOError:une erreur se produit lorsque on entre les mauvais noms
        GitCommandError:une erreur se produit lorsque il y a un merge
        """
        dir_path=sys.path[0]
        path=dir_path+'/archeo_lex/'+self.code
        if(os.path.exists(path)):
            try:
                repo = git.Repo(path)
                repo.git.pull()
                #print("archeo_lex/"+code+" a déjà exist,et on le pull")
            except git.InvalidGitRepositoryError:
                pass
            except git.GitCommandError:
                os.removedirs(path)
                try:
                    repo = git.Repo.clone_from(url ='https://archeo-lex.fr/codes/'+self.code,to_path=path)
                except IOError:
                    sys.stderr.write("On ne trouve pas"+self.code)
        else:
            try:
                repo = git.Repo.clone_from(url ='https://archeo-lex.fr/codes/'+self.code,to_path=path)
            except IOError:
                sys.stderr.write("On ne trouve pas"+self.code)
            #else:
                #print("On crée archeo_lex/"+code)

    @staticmethod
    def _write_csv(row,fileCsv):
        with open(fileCsv, 'a+', newline='',encoding='utf-8') as wf:
            csv_write = csv.writer(wf)
            csv_write.writerow(row)

    @staticmethod
    def create_csv(fileCsv):
        if fileCsv!=None:
            fileCsv= os.path.dirname(os.path.abspath(__file__))+'/'+fileCsv+'.csv'
        else:
            fileCsv= os.path.dirname(os.path.abspath(__file__))+'/codes.csv'
        if os.path.exists(fileCsv):
            os.remove(fileCsv)
        csv_head = ['code','version','date','partie','sous_partie','livre','titre','chapitre','article','type']
        ArcheoLexLog._write_csv(csv_head,fileCsv)

    @staticmethod
    def _frToInt(n):
        """Convertir des chiffres français en chiffres arabes

            Utiliser pour le numéro de série de la sous_partie

            Arg:
                n:String de numéros français

            return:
                str(dict[n]):String de chiffre arabe
        """
        dict={"Première":"1","Deuxième":"2","Troisième":"3","Quatrième":"4","Cinquième":"5","Sixième":"6","Septième":"7","Huitième":"8","Neuvième":"9","Dixième":"10"}
        return(str(dict[n]))

    def enterPath(self):
        """Entrer dans le dossier contenant le code requis

        return:
            Path:String du chemin du code requis

        """
        #dir_path=os.path.abspath(os.path.dirname(sys.argv[0]))
        dir_path=sys.path[0]
        path=dir_path+'/archeo_lex/'+self.code
        os.chdir(path)
        return path

    def getVersion(self,repo,commit):
        sha=commit.hexsha
        short_sha=repo.git.rev_parse(sha, short=7)
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
        diff = commit.parents[0].diff(commit, create_patch=True).pop()
        a=diff.a_blob.data_stream.read().decode('utf-8').splitlines()
        b=diff.b_blob.data_stream.read().decode('utf-8').splitlines()
        differ=difflib.Differ()
        cmp = differ.compare(a,b)
        return list(cmp)

    def getSousPartieCurrent(self,previous_partie,line):
        """Obtient le numéro de série sous_partie courente

            Sous partie s'écrit généralement comme   ## Première partie : XXXXX.
            Nous extrayons Première et la convertissons en chiffres romains.
            Si nous passons à la Partie suivante (ex: # Partie réglementaire), la sous_partie courante est Na

            Arg:
                previous_partie:String de sous partie précedente
                line:String on doit le traiter

            return:
                sous_partie_current:String de partie courente

            Raise:
                KeyError:Il peut y avoir plus de 10 Sous Partie, ou écriture irrégulière

        """
        sous_partie_current= previous_partie
        if line.find("partie : ") != -1 and line.startswith("  ##") and not line.startswith("  ###"):
            try:
                sous_partie_current =self._frToInt("".join(re.findall(r"## (.+?) partie",line)))
            except KeyError:
                faultMessage = "There is a spelling error in this line: "+line
                sys.stderr.write(faultMessage)
                #self._write_csv("errorMessage",faultMessage)
        if line.startswith("  # Partie"):
            sous_partie_current = "NA"
        return sous_partie_current

    @staticmethod
    def _getTypeLine(line):
        if line.startswith('-'):             # -######Article est Supression
            type_line = "Suppression"
        elif line.startswith('+'):           # +######Article est Ajout
            type_line = "Ajout"
        else:
            type_line = None
        return type_line


    class modification:
        def __init__(self, code, date, version, type, section, PLTC_method = "code"):
            self.code = code
            self.date = date
            self.version = version
            self.type = type
            self.nb_modifications = 0
            self.section = section
            self.article = section[-1].replace("Article ","")
            if PLTC_method == "code":
                self.partie = self.getPartie()
                [self.sous_partie,self.livre,self.titre,self.chapitre] = self.getPLTC()
            else:
                [self.partie, self.sous_partie,self.livre,self.titre,self.chapitre] = self.getPLTC_txt()

        def getPartie(self):
            #code_pénal est spéciale,dans sa partie législative,pas de "L" dans le nom des articles
            if self.isAnnex():
                #Exemple: Article L111 est remplcé par Article 111
                return "Annexe"
            elif self.article[0] == 'L' or self.article[0].isnumeric():
                return "Législative"
            elif self.article[0] == 'A':
                return "Arrêtés"
            elif self.article[0]=='R' or self.article[0] == 'D':
                return "Réglementaire"
            else:
                return "NA"

        def getPLTC(self):
            """vérifier le type du nom d'article et extraire les localisations

               cas normal: L111
               Cas spéciaux traités :
               111 : pas de partie
               L10/L10-1 : pas de livre (code_de_justice_administrative 2019-3-25)
               L1/L2/L3 : pas de livre (code_du_travail )
               L3121-3 : sous partie 3, livre 1 (code_du_travail)
               A931-1-1 : (code de la sécurité sociale)

               Cas spéciaux non traités:
               R14-10-2 : livre 1, titre 4, chapitre 10 (code de l'action sociale)
               1874 : livre 3, titre 10 (code civil)
            """

            # Extraire le premier numéro d'article
            # Exemples : Article L621, Article L*612, Article , Article 111, Article L10/L10-,
            artnum = re.sub("[^0-9-]","",self.article).split('-')[0]
            if len(artnum) < 3: return ["NA","NA","NA","NA"]
            if len(artnum) == 4:
                souspartie = artnum[0]
                artnum = artnum[1:]
            else:
                souspartie="NA"

            return [souspartie,artnum[0],artnum[1],artnum[2]]

        def getPLTC_txt(self):
            PLTC = self.section[0:5]
            if len(PLTC) < 5: PLTC.pop()
            while len(PLTC) < 5: PLTC.append("NA")
            return PLTC

        def isAnnex(self):
            """vérifier si un article est dans l'annex ou non

                Quand un article dans l'annex,il y a trois cas:
                1.Il y a le mot Annex dans l'artice
                Exemple: Article Anenex I
                2.Pour les articles pas écrire sa Partie (L ou R ou A) et seulment des numéro
                Exemple: Article 123 /Article 11
                3.Pour les articles ont seulment des numéro Romain (code_de_l'urbanisme)
                Exemple: Article II /Article I

                PS:pour le 2ème cas:
                code_pénal est spéciale,dans sa partie législative,pas de "L" dans le nom des articles
                Exemple: Article L111 est remplcé par Article 111

            return:
                True:C'est un article dans l'annex
                False:ce n'est pas un article dans l'annex
            """
            if self.article.upper().find("ANNEX")!=-1 or len(self.article)==1:
                return True
            elif self.article[0].isnumeric() and self.code != "code_pénal":
                return True
            #c'est pas numéro romain
            elif self.article[0]=="I" or self.article[0].upper=="V" or self.article[0].upper=="X":
                return True
            else:
                return False


    def outputInfo(self,mod,file):
        """print les infomations et les écrire dans csv,par défault,le file est codes.csv

        """
        if file != None:
            fileCsv = os.path.dirname(os.path.abspath(__file__))+'/'+file+'.csv'

        else:
            fileCsv = os.path.dirname(os.path.abspath(__file__))+'/codes.csv'
        message = [self.code, mod.version, mod.date,
            mod.partie,mod.sous_partie,mod.livre,mod.titre,mod.chapitre,
            mod.article,mod.type]
        self._write_csv(message,fileCsv)
        print(message)


    def getDiff(self,number_commit,file):
        """Obtenez toutes les modifications d'une version d'un code

            Parcourez les informations de différence, nous extrayons les informations
            correspondantes du nom de l'article

            Arg:
                number_commit: Commit(type) de version
        """
        #créer repo et get commit
        repo = git.Repo(self.enterPath())
        commit = repo.commit(number_commit)
        #get la version et la date
        date = self.getDate(commit)
        version = self.getVersion(repo,commit)
        #get lines in diff
        lines=self.getDifflines(commit)
        if self.verbose:
            with open(self.code+'-'+date+'.txt', 'w') as verbfile:
                verbfile.write('\n'.join(str(line) for line in lines))

        curmod = None # modification courante
        cursec = [] # section courante

        for num,line in enumerate(lines):
            # Détection du type de la ligne
            type_line = self._getTypeLine(line)

            # Si changement de section, enregistrer la nouvelle section
            if (len(line) > 2 and line[2] == '#'):
                level = line.count("#")
                cursec = cursec[:level-1]+[re.sub(".*# ","",line)]
                #print(line)
                #print(cursec)
                #print("\n")

                # Si changement d'article
                if line.find("Article") != -1:
                    # Si une modification a été détectée, l'imprimer
                    if curmod is not None and curmod.type is not None and curmod.nb_modifications != 0:
                        self.outputInfo(curmod, file)
                        #print(line)
                        #print(cursec)
                        #print("\n")

                    # Réinitialiser la modification courante
                    curmod = self.modification(self.code, date, version, type_line, cursec, self.PLTC_method)

            # Si pas de changement de section, on vérifie juste s'il n'y a pas de modifications,
            # dans une ligne non vide
            elif type_line is not None and len(line[1:].strip()) > 0:
                if curmod.type is None : curmod.type = "Modification"
                curmod.nb_modifications += 1
                #print(line)


    def processCode(self,datelimit,file):
        """Obtenir tous les versions d'un et pour chaque version on fonction getDiff()
        """
        path = self.enterPath()
        repo = git.Repo(path)
        #obtenir tous les version
        commit_log =repo.git.log('--pretty={"%h"}')
        log_list = commit_log.split("\n")
        log_list.pop()  #supprimer la première version
        for log in log_list:
            commit_number ="".join(re.findall(r"{\"(.+?)\"}",log))
            commit=repo.commit(commit_number)
            date=self.getDate(commit)
            if datelimit != None:
                if datetime.strptime(date,'%Y-%m-%d').date()<datelimit: return()
            self.getDiff(commit_number,file)
