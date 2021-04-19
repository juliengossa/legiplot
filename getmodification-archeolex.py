import os
import re
import git 
from git.compat import defenc

def createDepo(*codes_list):
    for code in codes_list:
        path = 'archeo_lex/'+code
        if(os.path.exists(path)):
            repo = git.Repo(path)
            repo.git.pull()
            print("archeo_lex/"+code+" a déjà exist,et on le pull")
        else:
            try:
                repo = git.Repo.clone_from(url ='https://archeo-lex.fr/codes/'+code,to_path=path)
            except IOError:
                print("On ne trouve pas"+ code)
            else:
                print("On crée archeo_lex/"+code)


def getDiff(type_code,number_commit):
    path='archeo_lex/'+type_code
    repo = Repo.clone_from(url='https://archeo-lex.fr/codes/'+type_code,to_path=path)
    os.chdir(path)
    #Parcourir tous les commits et obtenir le commit(hcommit) dont hexsha est type_code
    commits = list(repo.iter_commits('texte'))
    for i in commits:
        if i.hexsha == number_commit:
            hcommit = i

    #Obtenit le diff selon le commit(le diff de le commit que l'on a entré et le commit précédent)
    diff = hcommit.diff(hcommit.parents[0], create_patch=True)
    print(hcommit.parents[0].hexsha)
    for k in diff:
        msg = k.diff.decode(defenc)
        #print(msg) #on peut print tous les information de diff
        
        #On obtient l'informations nécessaire pour csv 
        print("Code Version Date modifier_location Partie Nature Sous-partie Livre Titre Article Type")

        results = re.findall(".*@@(.*)@@.*",str(msg))  # @@****@@ est le début d'une modification(le début de chunck)
        for match in results:
            print(type_code,end=" ") 
            print(hcommit.hexsha,end=" ")
            print(hcommit.committed_date,end=" ")
            print(match)

'''
quelques versions de commit pour code_civil
2b5d875bf431d8cf21df3c376551d7b7802e7a75
f1975506ff1acf167891aa2287e88f5330f2bab3
7947e5660e5ff34cbc639b84b72b8245446dbcdc
075e5160b5e137c2e71fbfe95ff88be52fa9e50d
'''

#main
#getDiff("code_civil","2b5d875bf431d8cf21df3c376551d7b7802e7a75")
createRepo('code_civil','code_de_la_propriété_intellectuelle')


'''
#Récupérer tous les codes de archeo-lex
def getAllTheRepo():
    codes = ['code_civil','code_de_la_propriété_intellectuelle','code_de_l\'éducation']
    for code in codes:
        repo = Repo.clone_from(url='https://archeo-lex.fr/codes/'+code,to_path='../'+code)
''' 