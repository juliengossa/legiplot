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
    diff = commit.diff(commit.parents[0], create_patch=True).pop()
    #a=diff.a_blob
    a=diff.a_blob.data_stream.read().decode('utf-8').splitlines()
    b=diff.b_blob.data_stream.read().decode('utf-8').splitlines()
    d = difflib.Differ()
    lines = list(d.compare(a,b))
    for num,line in enumerate(lines):
        if num<32518 and num>32450:
            print(num,":",line)
    for num,line in enumerate(lines):
        if line.startswith('- '):
            print(num,":",line)
        elif line.startswith('+ '):
            print(num,":",line)
    
    
"""
version 
git diff 69b00191794e276da0d8cdd12aa9d48cbd569c1b 1289adb8cf1af5b3a0bd9a1ed722dd49b411bc72
"""

    
#main
#createRepo('code_civil','code_de_la_propriété_intellectuelle','code_de_l\'éducation')
getDiff("code_de_l\'éducation","69b00191794e276da0d8cdd12aa9d48cbd569c1b")



