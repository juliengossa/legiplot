import os
import re
import git
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
    path='archeo_lex/'+type_code
    repo = git.Repo(path)
    os.chdir(path)
    commit = repo.commit(number_commit)
    #Obtenit le diff selon le commit(le diff de le commit que l'on a entré et le commit précédent)
    diff = commit.diff(commit.parents[0], create_patch=True).pop()
    print(commit.parents[0])
    a=diff.a_blob.data_stream.read().decode('utf-8')
    b=diff.b_blob.data_stream.read().decode('utf-8').splitlines()
    #differ = difflib.Differ()
    #lines = list(differ.compare(b,a))
    print(a)
    """
    for line in lines:
        print(line)
    """
    '''
    for num,txt in enumerate(lines):
        if txt.startswith('  #######'):
            print(num,':',txt)
    '''
    
    
'''
quelques versions de commit pour code_civil
2b5d875bf431d8cf21df3c376551d7b7802e7a75
f1975506ff1acf167891aa2287e88f5330f2bab3
7947e5660e5ff34cbc639b84b72b8245446dbcdc
075e5160b5e137c2e71fbfe95ff88be52fa9e50d
'''

#main
getDiff("code_civil","f1975506ff1acf167891aa2287e88f5330f2bab3")
#createRepo('code_civil','code_de_la_propriété_intellectuelle')


