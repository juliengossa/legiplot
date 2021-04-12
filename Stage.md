# Stage 

## Description du stage

- Sujet du stage : Quantification des évolutions législatives
- Lieu où aura lieu le stage : Université de Strasbourg
- Service accueillant le stagiaire : Centre d'Etudes Internationales de la Propriété Intellectuelle (CEIPI)
- Durée du stage (en jours) : 10 semaines / 50 jours ouvrés

## Contenu pédagogique

Les codes juridiques français contiennent les lois et règlements, qui évoluent constament. 
Divers projets visent à stocker ces codes sur des dépôts git. Ces dépôts permettent de quantifier et qualifier ces modifications.

Une exemple préliminaire est disponible ici : https://github.com/juliengossa/legiplot

### Missions et tâches confiées au stagiaire *

Le stagiaire aura pour mission de concevoir une application prenant en entrée un dépôt GIT [Archeo-Lex](https://archeo-lex.fr/)
et retournant en sortie un jeu de données quantitiatives décrivant les évolutions du code juridique déposé. 

L'application devra être capable d'identifier les sections de code (Article de loi)
dans lesquelles interviennent les modifications de chaque version, et d'identifier la nature des modifications
(ajouts/suppressions d'article). Ceci implique de travailler sur des diff GIT pour localiser les modification dans la structure 
markdown du fichier. 

### Compétences à acquérir

GIT, diff, markdown, R, analyse de texte, versionning. 

### Objectifs du stage *

- Concevoir une application d'analyse des diffs d'un GIT [Archéo-Lex](https://archeo-lex.fr/).
- Procéder à des analyses quantitatives préliminaires.

## Détails concrets 

Ces modifications sont localisées dans les codes, selon :
- La partie législative/règlementaire ;
- La sous-partie (optionnelle) ;
- Le livre ;
- Le titre ;
- Le chapitre ;
- Le chapitre ;
- Le sous-chapitre ;
- Le paragraphe ;
- Le sous-paragraphe ;
- L'article.

Ces localisations sont identifiées par des titres en markdown, et des numérotations plein texte :
```
# Partie législative
## Première partie : Dispositions générales et communes
### Livre Ier : Principes généraux de l'éducation
#### Titre Ier : Le droit à l'éducation
##### Chapitre Ier : Dispositions générales.
###### Article L111-1
```

Mais attention, les niveaux peuvent varier selon les parties et les codes.
```
#### Chapitre IX : Dispositions communes
##### Section 1 : Dispositions applicables aux conseils
###### Sous-section 1 : Conditions d'exercice du droit de suffrage, composition des collèges électoraux et modalités d'assimilation et d'équivalence de niveau pour la représentation des personnels et des étudiants aux conseils
####### Paragraphe 1 : Composition des collèges électoraux
######## Article D719-1
######## Sous-paragraphe 1 : Composition des collèges électoraux pour l'élection des membres des conseils d'unités de formation et de recherche et des membres des conseils des instituts et écoles internes
######### Article D719-4
```

Les niveaux sont aussi [encodés directement dans le nom de l'article](http://www1.univ-ag.fr/buag/cours/LS1droit-web/co/03_%20Differents%20types%20docs%20Codes.html). 
Par exemple :
```
#### Chapitre III : Les compétences des départements
##### Section 1 : Collèges.
###### Article R213-1
###### Article R213-2
##### Section 2 : Transports scolaires
###### Sous-section 1 : Dispositions générales
####### Paragraphe 1 : L'organisation des transports scolaires.
######## Article R213-3
```

`R213-2` est le 2eme article de la partie règlementaire (R), partie 2, livre 1, titre 3.

Certaines modifications sont purement de structure. Par exemple, [ici](https://archeo-lex.fr/codes/code_de_l%27environnement/2021-04-01/commit) l'ajout d'une sous-section :
```
-###### Article R541-42
+###### Sous-section 1 : Traçabilité des déchets, terres excavées et sédiments
+####### Article R541-42
```


Les modification des articles sont de trois types :

- Ajout ;
- Suppression ;
- Modification.

La granularité des modifications peut être :

- Le mot ;
- La ligne ;
- L'article, ou toute autre localisation.

Pour ce travail, la granularité choisie est l'article.

### Application

L'application doit prendre en entrée un dépôt git Archeo-Lex et doit produire en sortie un fichier au format suivant :

`Code;Version;Date;Partie;Nature;Sous-partie;Livre;Titre;Article;Type`

Par exemple, pour [ce commit](https://archeo-lex.fr/codes/code_de_l%27%C3%A9ducation/2021-04-03/commit) :

```
Code;Version;Date;Partie;Nature;Sous-partie;Livre;Titre;Article;Type
Code de l'éducation;85ba87f;2020-04-03;Règlementaire;R;NA;6;1;2;D612-34;Modification
```

NB : la Sous-partie peut être à `NA` lorsqu'elle n'existe pas (fréquent dans la partie réglementaire).

Il s'agit donc, pour chaque modification, d'identifier sa nature, le numéro d'article concerné (s'il ne s'agit pas d'une modification de structure), et l'éventuelle sous-partie.

### Algorithme général pour un code et un commit

- Récupérer le `diff` du commit
- Récupérer le `texte` du code à la version du commit
- Pour chaque ligne du `diff`
  - Identifier la nature de la modification
  - Identifier l'article de la modification et l'éventuelle sous-partie
  - Décider d'ajouter ou non à la sortie




