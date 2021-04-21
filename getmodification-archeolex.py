import os
import re
import git
import sys
import difflib 
from git.compat import defenc

def createRepo(*codes_list):
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
    #sys.stdout = open("a.txt","w")
    path='archeo_lex/'+type_code
    repo = git.Repo(path)
    os.chdir(path)
    commit = repo.commit(number_commit)
    #Obtenit le diff selon le commit(le diff de le commit que l'on a entré et le commit précédent)
    #lines=list(difflib.unified_diff(a,b))
    #result = re.findall("/d",str(difflib.unified_diff(a,b)))
    diff2 = commit.parents[0].diff(commit, create_patch=True)
    print(diff2)
    for n in diff2:
        msg = n.diff.decode(defenc)
        modifications = re.findall(".*@@(.*)@@.*",str(msg))
    diff = commit.parents[0].diff(commit, create_patch=True).pop()
    a=diff.a_blob.data_stream.read().decode('utf-8').splitlines()
    b=diff.b_blob.data_stream.read().decode('utf-8').splitlines()
    diff3=difflib.unified_diff(a,b)
    lines = list(diff3)

    nature = "1"
    for num,line in enumerate(lines):
        if line.startswith('@@'+modifications[1]):
            print(modifications[0])
            del lines[0:num+1]
            for num,line in enumerate(lines):
                if line.startswith('+'):
                    if nature == 'supprimer': 
                        nature = 'modifier'
                    else:
                        nature == "ajouter"
                if line.startswith('-'):
                    if nature == 'ajouter': 
                        nature = 'modifier'
                    else:
                        nature = "supprimer"
                if line.startswith('@@'+modifications[2]):
                    print(nature)
                    break
    
          

    #print(len(modifications))
    #print('@@ '+modifications[0])
    
    '''
    diff = commit.parents[0].diff(commit, create_patch=True).pop()
    a=diff.a_blob.data_stream.read().decode('utf-8').splitlines()
    b=diff.b_blob.data_stream.read().decode('utf-8').splitlines()

    diff3=difflib.unified_diff(a,b)
    lines = list(diff3)
    for num,line in enumerate(lines):
        if line.startswith('@@ '+modifications[0]):
            print(num,":",line)
  
    '''
   
    '''
    d = difflib.Differ()
    lines = list(d.compare(a,b))
    for num,line in enumerate(lines):
        if num<32549 and num>32491:
            print(num,":",line)
    
    for num,line in enumerate(lines):
        print(num,":",line)
        if line.startswith('@'):
            print(num,":",line)
        elif line.startswith('+'):
            print(num,":",line)
        elif line.startswith('-'):
            print(num,":",line)
     '''   
     
    

    

def getModiffication(type_code,number_commit):
    path='archeo_lex/'+type_code
    repo = git.Repo(path)
    os.chdir(path)
    commit = repo.commit(number_commit)
    diff2 = commit.parents[0].diff(commit, create_patch=True)
    print(commit.parents[0].hexsha)
    for k in diff2:
        msg = k.diff.decode(defenc)
        print(msg) #on peut print tous les information de diff       
        #On obtient l'informations nécessaire pour csv 
        print("Code Version Date modifier_location Partie Nature Sous-partie Livre Titre Article Type")

        results = re.findall(".*@@(.*)@@.*",str(msg))  # @@****@@ est le début d'une modification(le début de chunck)
        for match in results:
            print(type_code,end=" ") 
            print(commit.hexsha,end=" ")
            print(commit.committed_date,end=" ")
            print(match)


"""
version 
git diff 69b00191794e276da0d8cdd12aa9d48cbd569c1b 1289adb8cf1af5b3a0bd9a1ed722dd49b411bc72
git diff 1289adb8cf1af5b3a0bd9a1ed722dd49b411bc72 6b00e22e9e41a401f2abc093fa73d5bb8f7a4edf
"""

    
#main
#createRepo('code_civil','code_de_la_propriété_intellectuelle','code_de_l\'éducation')
getDiff("code_de_l\'éducation","1289adb8cf1af5b3a0bd9a1ed722dd49b411bc72")
#getModiffication("code_de_l\'éducation","1289adb8cf1af5b3a0bd9a1ed722dd49b411bc72")



