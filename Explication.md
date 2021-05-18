Explication 
================

# Partie Ier: Générer un fichier csv
## La première étape: classer le code
On doit traiter 39 [codes](codes.txt).Nous pouvons classer ces codes selon leurs noms d'articles.Si ses noms d'article sont liés à Titre Livre et Chapitre,ce code appartient au **type I**,sinon ce code appartient au **type II**.

**31 codes de type I:**  

code_de_commerce code_de_justice_administrative code_de_l'action_sociale_et_des_familles code_de_l'aviation_civile code_de_l'éducation code_de_l'entrée_et_du_séjour_des_étrangers_et_du_droit_d'asile code_de_l'environnement code_de_l'urbanisme code_de_l'organisation_judiciaire code_de_l'énergie code_de_la_consommation code_de_la_construction_et_de_l'habitation code_de_la_défense code_de_la_propriété_intellectuelle code_de_la_recherche code_de_la_route code_de_la_santé_publique code_de_la_sécurité_intérieure code_de_la_sécurité_sociale code_des_assurances code_des_juridictions_financières code_des_transports code_du_cinéma_et_de_l'image_animée code_du_patrimoine code_du_sport code_du_tourisme code_du_travail code_forestier_(nouveau) code_général_de_la_propriété_des_personnes_publiques code_général_des_collectivités_territoriales code_pénal

**8 codes de type II:**  

code_civil code_de_l'artisanat code_de_la_famille_et_de_l'aide_sociale code_de_procédure_civile code_de_procédure_pénale code_des_postes_et_des_communications_électroniques code_disciplinaire_et_pénal_de_la_marine_marchande code_électoral

## La deuxième étape:Traiter les codes de type I
Dans la class [ArcheoLexLog](ArcheoLexLog.py),on a un méthode qui s'appelle **getDiff(self,number_commit,file)**,il imprime tous les articles de la version du number_commit qui sont modiffiés(ou Ajoutés ou Supprimés) 
Dans le cas normale, nous pouvons facilement obtenir le livre, le titre et le chapitre actuels par le nom de l'article.Cependant, les noms de certains articles sont inhabituels. Nous avons des cas particuliers. 
| nom_d'article | se trouve | partie | livre | titre | chapitre| Traitement spécial|
| ------ | ------ | ------ |------ | ------ | ------ |------ | 
| Article R111-12 | tous les codes | Régelmentaire |1 | 1 | 1 | C'est cas normal,pas besoin de traitement spécial|
| Article D\*213| beaucoup de codes |beaucoup de codes| 2 |1| 3| dans getDiff() on supprime \* |
| Article \*R213| code_de_l'urbanisme|beaucoup de codes| 2 |1| 3| dans getDiff() on supprime \* |
| Article ANNEX | beaucoup de codes|  | |  |  | ce type de code est dans Annexe est on imprime pas,isAnnex(self,article_current)return Ture|
| Article IV | code_de_l'urbanisme) |  | |  |  | ce type d'article n'est peut être pas dans Annexe mais on ignore,isAnnex(self,article_current)return Ture|
| Article 111 | beaucoup de codes(pas code_pénal) |  | |  |  | ce type d'article est dans Annexe et on imprime pas,isAnnex(self,article_current)return Ture|
| Article 111 | code_pénal|Législative|1 |1| 1 | ce type d'article ignore "L",isAnnex(self,article_current)return False, _getLivreLocation(article_current) return 0,getPartieCurrent(slef,article_current) return Législative|
| Article L10 | beaucoup de codes|Législative|Na |Na| Na |_getLivreLocation(article_current) return -1|
| Article L3121-3| code_du_travail code_de_la_santé_publique code_de_la_défense code_général_des_collectivités_territoriales|Législatives|1 |2| 1| _getLivreLocation(article_current) return 2|
| Article R\*1211-1| code_du_travail code_de_la_santé_publique code_de_la_défense code_général_des_collectivités_territoriales|Législatives|2 |1| 1| dans getDiff() on supprimer \* et _getLivreLocation(article_current) return 2|

PS:Les deux derniers noms d'articles, on peut obtenir sous_partie
| nom_d'article | sous_partie |Traitement spécial|
| ------ | ------ | ------ |
| Article L3121-3 | 3 | écrire dans getDiff(): "if article_current[i-1].isnumeric() and i-1>=0:sous_partie_current=article_current[i-1]"|
| Article R\*1211-1 |1 | écrire dans getDiff(): "if article_current[i-1].isnumeric() and i-1>=0:sous_partie_current=article_current[i-1]"|

### le command pour imprimer le csv des codes
Par Exemple:   
python archeolex-excavation.py -csv codesType1 -d 2020-12-31 -codes code_de_commerce code_de_justice_administrative code_de_l'action_sociale_et_des_familles code_de_l'aviation_civile code_de_l'éducation code_de_l'entrée_et_du_séjour_des_étrangers_et_du_droit_d'asile code_de_l'environnement code_de_l'urbanisme code_de_l'organisation_judiciaire code_de_l'énergie code_de_la_consommation code_de_la_construction_et_de_l'habitation code_de_la_défense code_de_la_propriété_intellectuelle code_de_la_recherche code_de_la_route code_de_la_santé_publique code_de_la_sécurité_intérieure code_de_la_sécurité_sociale code_des_assurances code_des_juridictions_financières code_des_transports code_du_cinéma_et_de_l'image_animée code_du_patrimoine code_du_sport code_du_tourisme code_du_travail code_forestier_(nouveau) code_général_de_la_propriété_des_personnes_publiques

- **csv** le nom du file
- **d** la date limite
- **codes** quelques codes de type I

### les problèmes:
**Problème fréquent et grave**
Pour quelques versions de quelques codes,le nombre de lignes sorties sont beaucoup plus grands que le fait, quelques articles ne changent pas du tout,mais ils apparaissent plusieur fois dans CSV.Et leur types de modification ne sont pas mêmes.
Par exemple
| nom_d'article et version | site | Article_Modifiés_sur_site| csv |lignes_sortie_dans_csv |
| ------ | ------ | ------ |------ |------ |
| code_de_commerce 2021-02-13 |[modification](https://archeo-lex.fr/codes/code_de_commerce/2021-02-13/modifications) | 39|[code_de_commerce_test.csv](code_de_commerce_test.csv)| 314 |
| code_pénal 2010-06-21 |[modification](https://archeo-lex.fr/codes/code_p%C3%A9nal/2010-06-21/modifications) | 41 |[code_pénal_test.csv](code_pénal_test.csv)| 122 |



## La troisième étape:Traiter les codes de type II

Dans la class ArcheoLexLog2(pas encore push)
