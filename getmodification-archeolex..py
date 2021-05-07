import os
import re
import git
import sys
import difflib
import time 
import dateparser
import csv
from git.compat import defenc

def createRepo(*codes_list):
    """Créer ou mettre à jour un dossier contenant les codes requises

    on clone les codes requis sur git et les place dqns les dossier 
    correspondant de archeo_lex,Si un code existe déjà,exécute git pull

    Arg:
        *codes_list: Une liste contient tous les noms des codes dont 
        nous avons besoin

    returns:

    Raises：
        IOError:une erreur se produit lorsque on entre les mauvais noms 
    """

    for code in codes_list:
        path = 'archeo_lex/'+code
        if(os.path.exists(path)):
            repo = git.Repo(path)
            repo.git.pull()
            #print("archeo_lex/"+code+" a déjà exist,et on le pull")
        else:
            try:
                repo = git.Repo.clone_from(url ='https://archeo-lex.fr/codes/'+code,to_path=path)
            except IOError:
                print("On ne trouve pas"+ code)
            #else:
                #print("On crée archeo_lex/"+code) 
                  
def write_csv(type_code, row):
    with open(type_code+'.csv', 'a+', newline='',encoding='utf-8') as wf:
        csv_write = csv.writer(wf)
        csv_write.writerow(row)

def romanToInt(s):
    """Convertir des chiffres romains ou spéciaux en chiffres arabes

        Utiliser pour la conversion du numéro de série du chapitre/livre/titre

        Arg: 
            s:string de chiffre romain

        return: 
           str(sum):string de chiffre arabe
    """

    if s=="Ier" or s=="unique":
        sum = 1
    elif s=="Préliminaire" or s=="préliminaire":
        sum = 0
    else:    
        sum=0
        convert={'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1} 
        for i in range(len(s)-1):
            if convert[s[i]] < convert[s[i+1]]:
                sum -= convert[s[i]]
            else:
                sum += convert[s[i]]
        sum += convert[s[-1]]    
    return str(sum) 

def frToInt(n):
    """Convertir des chiffres français en chiffres arabes

        Utiliser pour la conversion du numéro de série de la sous_partie

        Arg: 
            n:String de numéros français

        return: 
           str(dict[n]):String de chiffre arabe
    """
    dict={"Première":"1","Deuxième":"2","Troisième":"3","Quatrième":"4","Cinquième":"5","Sixième":"6","Septième":"7","Huitième":"8","Neuvième":"9","Dixième":"10"}
    return(str(dict[n]))

def enterPath(type_code):
    """Entrer dans le dossier contenant le code requis
       
       Arg:
           type_code:String de code que l'on veut
        
       return:
           Path:String du chemin du code requis

    """
    dir_path=os.path.abspath(os.path.dirname(__file__))
    path=dir_path+'/archeo_lex/'+type_code
    os.chdir(path)
    return path  

def getVersion(repo,commit):
    sha=commit.hexsha
    short_sha=repo.git.rev_parse(sha, short=7)
    version = short_sha
    return version

def getDate(repo,commit):
    date_fr=" ".join(re.findall('(?<=au).*$',commit.message))
    date=dateparser.parse(date_fr).date().strftime("%Y-%m-%d")
    return date

def getDifflines(commit):
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

def getType(line):
    type = "Na"
    if line.find("Article")!= -1 and line.find('#')!=-1:
            #get type
            if line.startswith('-'):             # -######Article est Supression
                type = "Suppression"
            elif line.startswith('+'):           # +######Article est Ajout
                type = "Ajout"
            else:
                type = "modification" 
    return type

def getNumberChanged(type):
    if type =="Suppression":
        number_changed=1
    elif type =="Ajout":
        number_changed=1
    else:
        number_changed=0
    return number_changed

def getPartieCourent(Article_courent):
    if Article_courent[0] == 'L':
        partie_courent="Législative" 
    elif Article_courent[0]=='R' or Article_courent[0] == 'D':
        partie_courent = "Réglementaire"
    else:
        partie_courent="Na"
    return partie_courent

def getSousPartieCourent(previous_partie,line):
    """Obtient le numéro de série sous_partie courente

        Sous partie s'écrit généralement comme   ## Première partie : XXXXX. 
        Nous extrayons Première et la convertissons en chiffres romains. 
        Si nous passons à la Partie suivante (ex: # Partie réglementaire), la sous_partie courante est Na
       
       Arg:
           previous_partie:String de sous partie précedente
           line:String on doit le traiter
        
       return:
           sous_partie_courent:String de partie courente

        Raise:
            KeyError:Il peut y avoir plus de 10 Sous Partie, ou écriture irrégulière
                       Et les errors vont être écrit dans errorMessage.csv
    """
    sous_partie_courent= previous_partie

    if line.find("partie : ") != -1 and line.startswith("  ##") and not line.startswith("  ###"):   
        try:
            sous_partie_courent =frToInt("".join(re.findall(r"## (.+?) partie",line)))
        except KeyError:
            faultMessage = "There is a spelling error in this line: "+line
            print(faultMessage)
            write_csv("errorMessage",faultMessage)      
    if line.startswith("  # Partie"):           
        sous_partie_courent = "Na"
    return sous_partie_courent

def getCourent(structure_name,previous,line):
    """Obtient le numéro de série(Livre/Titre/Chapitre)

        La sturcture normale s'écrit généralement comme   ##### Chapitre Ier :  
        Nous extrayons Ier et la convertissons en chiffres romains. 
       
       Arg:
           structure_name:"Livre" ou "Titre" ou "Chapitre"
           previous_partie:La structure précédente
           line:String on doit le traiter
        
       return:
           courent:Structure courente

        Raise:
            KeyError:Il peut y avoir écriture irrégulière
            Et les errors vont être écrit dans errorMessage.csv
    """
    courent = previous
    #Exemple:Chapitre  Ier quinquies : Autorisations,Supprimer les espaces supplémentaires
    line =' '.join(re.split(' +|\n+', line)).strip()
    #on trouve il y a des fautes pour des codes 
    #Exemple:civle(version:2b5d875),normalment la titre est Titre XIV,mais il a écrit Titre : XIV
    if line.find(structure_name+" :")!= -1 and line.startswith("  #")!=-1:
       structure_name=structure_name+" :"
    if line.find("# "+structure_name)!= -1 :
        try:
            courent = romanToInt("".join(re.findall(rf'{structure_name} (.+?)\b',line)))
        except IndexError:
            faultMessage = "There is a spelling error in this line: "+line
            print(faultMessage)
            write_csv("errorMessage",faultMessage)
    return courent

def outputInfo(type_code,version,date,partie_courent,sous_partie_courent,livre_courent,titre_courent,chapitre_courent,article_courent,type):
    """print les infomations et les écrire dans csv

    """
    message =[type_code,version,date,partie_courent,sous_partie_courent,livre_courent,titre_courent,chapitre_courent,article_courent,type]
    write_csv(type_code,message)
    print(message)

def isStructureChange(modification):
    """vérifier si un changes est sur structure ou non

    """
    if modification.find("# Chapitre")!=-1 or modification.find("# Livre") !=-1 or modification.find("# Titre")!=-1 or modification.find("# Section")!=-1 or modification.find("# Sous-")!=-1 or modification.find("# Paragraphe")!=-1 or modification.find("# Dispositions")!=-1 :
        return True
    else:
        return False

def getDiff(type_code,number_commit):
    """Obtenez toutes les modifications d'une version d'un code

        Parcourez les informations de différence, déterminer le livre et titre et chapitre et article de chaque ligne, 
        et lorsqu'il atteint le début de l'article suivant ou la dernière ligne du texte, juger s'il faut sortir les 
        informations des ；modification de l'article actuel en calculant si le nombre de lignes modifiées est égal 
        à zéro. 

        Arg: 
           type_code:String de non du code
           number_commit: Commit(type) de version
    """
    #créer repo et get commit
    repo = git.Repo(enterPath(type_code))
    commit = repo.commit(number_commit)
    #get la version et la date
    date = getDate(repo,commit)
    version = getVersion(repo,commit)
    #get lines in diff
    lines=getDifflines(commit)
    #get la structue des articles modifiées
    livre_courent = "Na"
    titre_courent = "Na"
    chapitre_courent = "Na"
    article_courent = "Na"
    partie_courent = "Na"
    sous_partie_courent = "Na"
    type="Na"
    for num,line in enumerate(lines):
        livre_courent = getCourent("Livre",livre_courent,line)
        titre_courent=getCourent("Titre",titre_courent,line)
        chapitre_courent=getCourent("Chapitre",chapitre_courent,line)
        sous_partie_courent=getSousPartieCourent(sous_partie_courent,line)
        if line.find("Article")!= -1 and line.find('#')!= -1:
            article_courent=line.replace("#","").replace(" ","").replace("Article","").strip("+").strip("-")
            type=getType(line)
            #nombre_modifier=0
            nombre_modifier=getNumberChanged(type)
            #Parcourir tous les lignes d'article courent
            currentArticleLines = lines[num+1:]
            for modification in currentArticleLines:
                #S'il y a pas de modifcation on n'imprime pas les résultats
                if modification.find("Article")!=-1 and modification.find("#")!=-1 and nombre_modifier ==0:
                    break
                #S'il y a des modification on imprime les résultats et l'écrit dans csv
                if modification.find("Article")!=-1 and modification.find("#")!=-1 and nombre_modifier !=0:  
                    partie_courent=getPartieCourent(article_courent)
                    outputInfo(type_code, version, date, partie_courent, sous_partie_courent, livre_courent, titre_courent, chapitre_courent, article_courent, type)
                    break
                #S'il y a des changement sur la dernière version
                if  nombre_modifier !=0 and not modification:
                    partie_courent=getPartieCourent(article_courent)
                    outputInfo(type_code, version, date, partie_courent, sous_partie_courent, livre_courent, titre_courent, chapitre_courent, article_courent, type)
                    break
                #Compter le nombre de lignes modifiées et Ignorer les changements structurels
                if modification.startswith('+') and len(modification) != 2 and isStructureChange(modification) == False:   # len(modification)==2 quand il y a que un "+" dans cette ligne  
                    nombre_modifier = nombre_modifier + 1
                if modification.startswith('-') and len(modification) != 2 and isStructureChange(modification) == False:
                    nombre_modifier = nombre_modifier + 1
                
def processCode(type_code):
    """Obtenir tous les versions d'un et pour chaque version on fonction getDiff()
    """
    csv_head = ['code','version','date','partie','sous_partie','livre','titre','chapitre','article','nature']
    path = enterPath(type_code)
    write_csv(type_code,csv_head) 
    repo = git.Repo(path)
    #obtenir tous les version
    commit_log =repo.git.log('--pretty={"%h"}') 
    log_list = commit_log.split("\n")
    log_list.pop()  #supprimer la première version
    for log in log_list:
        commit_number ="".join(re.findall(r"{\"(.+?)\"}",log))
        getDiff(type_code,commit_number)

#main
createRepo('code_civil','code_de_la_propriété_intellectuelle','code_de_l\'éducation')
processCode("code_de_l\'éducation")
processCode('code_de_la_propriété_intellectuelle')
#processCode('code_civil')



                


 




