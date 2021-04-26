import os
import re
import git
import sys
import difflib
import time 
from git.compat import defenc

def createRepo(*codes_list):
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


def getDiff(type_code,number_commit):
    path='archeo_lex/'+type_code
    repo = git.Repo(path)
    os.chdir(path)
    commit = repo.commit(number_commit)
    #la version
    sha=commit.hexsha
    short_sha=repo.git.rev_parse(sha, short=7)
    version = short_sha
    #la date de commit
    date = time.strftime("%Y-%m-%d", time.gmtime(commit.committed_date))
    diff = commit.parents[0].diff(commit, create_patch=True).pop()
    a=diff.a_blob.data_stream.read().decode('utf-8').splitlines()
    b=diff.b_blob.data_stream.read().decode('utf-8').splitlines()
    differ=difflib.Differ()
    lines = list(differ.compare(a,b))
    current_section=None
    print("code date version partie livre titre chapitre article type")
    for num,txt in enumerate(lines):
       if txt.find("Article")!=-1 and txt.find("#")!=-1:
            current_section = txt.replace("#","").replace(" ","").strip("+").strip("-")
            partie ="Législative" if current_section[7]=='L' else "Réglementaire"
            livre = current_section[8]
            titre = current_section[9]
            chapitre = current_section[10]
            currentArticleLines = lines[num+1:]
            nombre_supprimer = 0
            nombre_ajouter = 0
            for modification in currentArticleLines:
                if modification.find("Article")!=-1 and modification.find("#")!=-1 and nombre_ajouter == 0 and nombre_supprimer == 0:
                    break
                if modification.find("Article")!=-1 and modification.find("#")!=-1 and nombre_ajouter !=0 and nombre_supprimer ==0:
                    print(type_code,date,version,partie,livre,titre,chapitre,current_section,"Ajout")
                    break
                if modification.find("Article")!=-1 and modification.find("#")!=-1 and nombre_ajouter ==0 and nombre_supprimer !=0:
                    print(type_code,date,version,partie,livre,titre,chapitre,current_section,"Suppression")
                    break
                if modification.find("Article")!=-1 and modification.find("#")!=-1 and nombre_ajouter !=0 and nombre_supprimer !=0:
                    print(type_code,date,version,partie,livre,titre,chapitre,current_section,"Modification")
                    break
                if modification.startswith('+'):
                    nombre_ajouter=nombre_ajouter+1                   
                if modification.startswith('-'):
                    nombre_supprimer=nombre_supprimer+1

#main
createRepo('code_civil','code_de_la_propriété_intellectuelle','code_de_l\'éducation')
#getDiff("code_de_l\'éducation","f55675eb9e77976b2f4dea8b24a960f8c03079ba")
getDiff("code_de_la_propriété_intellectuelle","5132e20ff201b8f4cbcfb63bee5857847a77f193")




