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
    def __init__(self,code):
        self.code=code  

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
        csv_head = ['code','version','date','partie','sous_partie','livre','titre','chapitre','article','nature']
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
        lines = list(differ.compare(a,b))
        return lines

    def getPartieCurrent(slef,article_current):
        #code_pénal est spéciale,dans sa partie législative,pas de "L" dans le nom des articles
        #Exemple: Article L111 est remplcé par Article 111
        if article_current[0] == 'L'or article_current[0].isnumeric():
            partie_current="Législative"
        elif article_current[0] == 'A':
            partie_current = "Arrêtés"
        elif article_current[0]=='R' or article_current[0] == 'D':
            partie_current = "Réglementaire"
        else:
            partie_current="NA"
        return partie_current

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

    def outputInfo(self,version,date,partie_current,sous_partie_current,livre_current,titre_current,chapitre_current,article_current,type,file):
        """print les infomations et les écrire dans csv,par défault,le file est codes.csv
           
        """
        if file!=None:
            fileCsv= os.path.dirname(os.path.abspath(__file__))+'/'+file+'.csv'
        else:
            fileCsv= os.path.dirname(os.path.abspath(__file__))+'/codes.csv'
        message =[self.code,version,date,partie_current,sous_partie_current,livre_current,titre_current,chapitre_current,article_current,type]
        self._write_csv(message,fileCsv)
        print(message)

    @staticmethod
    def _getTypeLine(line):
        if line.startswith('-'):             # -######Article est Supression
            type_line = "Suppression"
        elif line.startswith('+'):           # +######Article est Ajout
            type_line = "Ajout"
        else:
            type_line = None
        return type_line

    def isAnnex(self,article_current):
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

        Arg:
            article_current:le nom d'article
            
        return:
            True:C'est un article dans l'annex
            False:ce n'est pas un article dans l'annex
        """
        if article_current.upper().find("ANNEX")!=-1 or len(article_current)==1:
            return True
        elif article_current[0].isnumeric() and self.code != "code_pénal":
            return True
        #c'est pas numéro romain
        elif article_current[0]=="I" or article_current[0].upper=="V" or  article_current[0].upper=="X": 
            return True
        else:
            return False   

    @staticmethod
    def _getLivreLocation(article_current):
        """vérifier le type du nom d'article et return la location du livre

           cas normal:
           Ex:L111,la location du livre est 1
           3 cas spéciaux:
           1.Ex:L10/L10-1,pas de livre courant,on return -1 (code_de_justice_administrative 2019-3-25)
                L1/L2/L3, pas de livre courant,on return -1 (code_du_travail )
           2.Ex:L3121-3,la location du livre est 2 (code_du_travail) (ps:la location 1 est sous_partie)
           3.Ex:111, la location du livre est 0 
           
           Arg:
           article_current:le nom d'article
            
        return:
            True:C'est un article dans l'annex
            False:ce n'est pas un article dans l'annex
        """
        location=1                                                                             #le cas normal:Article R14-10-2
        if  article_current[0].isnumeric():                                                     #Article 111
            location=0  
        elif (len(article_current)<=3) or (len(article_current)<=5 and article_current[3]=="-" and (not article_current[0].isnumeric())):    #Article L10/L10-1
            location=-1                                                                                
        elif len(article_current)>=5:                                                            
            if article_current[4].isnumeric() and article_current[3]!="-":
                location = 2                                                                  #Article L3121-3  Ps(éviter L77-10-25)
        return location
          
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
        #get la structue des articles modifiées
        livre_current = "NA"
        titre_current = "NA"
        chapitre_current = "NA"
        article_current = "NA"
        partie_current = "NA"
        sous_partie_current = "NA"
        type = None
        for num,line in enumerate(lines):
            # Détection du type de la ligne
            type_line =self._getTypeLine(line)
                # Si changement de section ou la dernière ligne de codes
            if (len(line) > 2 and line[2] == '#') or num == lines.count:
                # Si un type de modification a été détecté avant ce changement de section, l'afficher et le réinitialiser
                if type is not None:
                    #On calcule et d'imprimer les résultats si ce n'est pas un changement d'article Annexe
                    if not self.isAnnex(article_current):
                        article_print=article_current #On enregistre le nom d'article avec * pour imprimer 
                        article_current=article_current.replace('*','') #On supprime *
                        partie_current = self.getPartieCurrent(article_current)
                        # On obtenir la location du livre
                        i=self._getLivreLocation(article_current)
                        if i==-1:
                            livre_current="NA"
                            titre_current ="NA"
                            chapitre_current = "NA"
                        else:
                            livre_current = article_current[i]
                            titre_current =article_current[i+1]
                            chapitre_current = article_current[i+2]
                            if chapitre_current == "-":             #Ex:L12-10-14(code_de_conmerce 2021-01-01)la chapitre est 10
                                chapitre_current = article_current[i+3]+article_current[i+4]

                        #Le numéro avat le titre est sous_partie()
                        #L3121-3, sous_partie 3 livre 1 titre 2 chapitre 1
                        try:
                            if article_current[i-1].isnumeric() and i-1>=0:
                                sous_partie_current=article_current[i-1]
                        except IndexError as f:
                            sys.stderr.write("IndexError: "+article_current)
                            

                        self.outputInfo(version, date, partie_current, sous_partie_current, livre_current, titre_current, chapitre_current, article_print, type,file)
                type = None

                # Détection d'une nouvelle sous partie
                # TODO : vérifier que la sous partie est réinitialisée en cas de changement de partie
                sous_partie_current = self.getSousPartieCurrent(sous_partie_current,line)

                # Si la section est un article
                if line.find("Article")!= -1 :
                    article_current=line.replace("#","").replace(" ","").replace("Article","").strip("+").strip("-")
                    type = type_line

            # Si pas de changement de section, on vérifie juste s'il n'y a pas de modifications, dans une ligne non vide
            elif type is None and type_line is not None and len(line[1:].strip()) > 0:
                type = "Modification"
    
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
            
            
