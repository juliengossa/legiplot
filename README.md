Legiplot
================

## Présentation

Legiplot vise à évaluer le rythme des réformes par l’exploitation des
dépôts git des codes.

Trois dépôts présentent les données législatives françaises :

-   [Legifrance](https://github.com/legifrance) (Abandonné) : *“Ce dépôt
    des Codes en vigueur de le République Française permet à tout un
    chacun de consulter, modifier (fork) et proposer leurs changements
    (Pull Request) qui seront examinés systématiquement par les
    instances législatives de la République Française. Ces dernières
    mettront en place dans les plus brefs délais un système de
    validation par les citoyens (peers) afin de pouvoir répondre à
    toutes les demandes.”*
-   [EtaLab](https://github.com/etalab/codes-juridiques-francais) : très
    précis, mais avec une mise à jour lente et des commits non
    chronologiques.
-   [Archéo Lex](https://archeo-lex.fr/) : peu précis (un fichier par
    code), mais régulièrement mis à jour et avec des commits
    chronologiques.

## Application archeolex\_excavation

L’application python 3 `archeolex_excavation` facilite la fouille des
dépôts git Archéo Lex.

    usage: archeolex_excavation.py [-h] [-d YYYY-MM-DD] [-f fichier.csv] [-t] [-v] diff|check code [code ...]

    positional arguments:
      diff|check            Le traitement à effectuer
      code                  La liste des codes à fouiller

    optional arguments:
      -h, --help            show this help message and exit
      -d YYYY-MM-DD, --datelimit YYYY-MM-DD
                            Définit une date maximum pour la fouille
      -f fichier.csv, --file fichier.csv
                            Ecrit les données dans un fichier csv (sortie standard par défaut)
      -t, --fulltext        Détecte les noms entiers des sections
      -v, --verbose         Enregistre tous les fichiers intermédiaires

## Détection d’erreurs

L’application permet de détecter des erreurs de deux types : - `doublon`
: articles apparaissant deux fois dans un code ; - `inversion` : deux
articles consécutifs dont la numérotation n’est pas croissante.

Cette détection d’erreur est imparfaite, et n’exclu ni faux-positifs ni
faux-négatifs. La date correspond à la version la plus ancienne à
laquelle l’erreur a été détectée.

Les erreurs détectées sur un échantillon de codes se trouvent dans le
fichier [errors.csv](errors.csv), au format suivant :

<table>
<thead>
<tr>
<th style="text-align:left;">
code
</th>
<th style="text-align:left;">
version
</th>
<th style="text-align:left;">
date
</th>
<th style="text-align:left;">
partie
</th>
<th style="text-align:right;">
sous\_partie
</th>
<th style="text-align:right;">
livre
</th>
<th style="text-align:right;">
titre
</th>
<th style="text-align:right;">
chapitre
</th>
<th style="text-align:left;">
article
</th>
<th style="text-align:left;">
type
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
code civil
</td>
<td style="text-align:left;">
00f14be
</td>
<td style="text-align:left;">
1803-04-29
</td>
<td style="text-align:left;">
Législative
</td>
<td style="text-align:right;">
NA
</td>
<td style="text-align:right;">
8
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
9
</td>
<td style="text-align:left;">
819
</td>
<td style="text-align:left;">
inversion 842
</td>
</tr>
<tr>
<td style="text-align:left;">
code civil
</td>
<td style="text-align:left;">
d48a9bd
</td>
<td style="text-align:left;">
1803-05-13
</td>
<td style="text-align:left;">
Législative
</td>
<td style="text-align:right;">
NA
</td>
<td style="text-align:right;">
9
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
5
</td>
<td style="text-align:left;">
905
</td>
<td style="text-align:left;">
inversion 1095
</td>
</tr>
<tr>
<td style="text-align:left;">
code civil
</td>
<td style="text-align:left;">
f7a5147
</td>
<td style="text-align:left;">
1804-02-17
</td>
<td style="text-align:left;">
Législative
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
3
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
6
</td>
<td style="text-align:left;">
1316
</td>
<td style="text-align:left;">
inversion 1369
</td>
</tr>
<tr>
<td style="text-align:left;">
code civil
</td>
<td style="text-align:left;">
74471bb
</td>
<td style="text-align:left;">
1804-02-24
</td>
<td style="text-align:left;">
Législative
</td>
<td style="text-align:right;">
2
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
2
</td>
<td style="text-align:right;">
4
</td>
<td style="text-align:left;">
2024
</td>
<td style="text-align:left;">
inversion 2027
</td>
</tr>
<tr>
<td style="text-align:left;">
code civil
</td>
<td style="text-align:left;">
d86cb5f
</td>
<td style="text-align:left;">
1804-03-17
</td>
<td style="text-align:left;">
Législative
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
4
</td>
<td style="text-align:right;">
9
</td>
<td style="text-align:right;">
2
</td>
<td style="text-align:left;">
1492
</td>
<td style="text-align:left;">
inversion 1523
</td>
</tr>
<tr>
<td style="text-align:left;">
code civil
</td>
<td style="text-align:left;">
63bf723
</td>
<td style="text-align:left;">
1804-03-26
</td>
<td style="text-align:left;">
Législative
</td>
<td style="text-align:right;">
2
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
6
</td>
<td style="text-align:right;">
2
</td>
<td style="text-align:left;">
2062
</td>
<td style="text-align:left;">
inversion 2070
</td>
</tr>
</tbody>
</table>

Le nombre d’erreurs détectées est :

<table>
<thead>
<tr>
<th style="text-align:right;">
doublon
</th>
<th style="text-align:right;">
inversion
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:right;">
463
</td>
<td style="text-align:right;">
2179
</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th style="text-align:left;">
code
</th>
<th style="text-align:right;">
doublon
</th>
<th style="text-align:right;">
inversion
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
code civil
</td>
<td style="text-align:right;">
17
</td>
<td style="text-align:right;">
46
</td>
</tr>
<tr>
<td style="text-align:left;">
code de commerce
</td>
<td style="text-align:right;">
23
</td>
<td style="text-align:right;">
61
</td>
</tr>
<tr>
<td style="text-align:left;">
code de justice administrative
</td>
<td style="text-align:right;">
4
</td>
<td style="text-align:right;">
6
</td>
</tr>
<tr>
<td style="text-align:left;">
code de l’action sociale et des familles
</td>
<td style="text-align:right;">
11
</td>
<td style="text-align:right;">
38
</td>
</tr>
<tr>
<td style="text-align:left;">
code de l’aviation civile
</td>
<td style="text-align:right;">
7
</td>
<td style="text-align:right;">
16
</td>
</tr>
<tr>
<td style="text-align:left;">
code de l’éducation
</td>
<td style="text-align:right;">
12
</td>
<td style="text-align:right;">
28
</td>
</tr>
<tr>
<td style="text-align:left;">
code de l’énergie
</td>
<td style="text-align:right;">
3
</td>
<td style="text-align:right;">
44
</td>
</tr>
<tr>
<td style="text-align:left;">
code de l’entrée et du séjour des étrangers et du droit d’asile
</td>
<td style="text-align:right;">
6
</td>
<td style="text-align:right;">
9
</td>
</tr>
<tr>
<td style="text-align:left;">
code de l’environnement
</td>
<td style="text-align:right;">
15
</td>
<td style="text-align:right;">
69
</td>
</tr>
<tr>
<td style="text-align:left;">
code de l’organisation judiciaire
</td>
<td style="text-align:right;">
4
</td>
<td style="text-align:right;">
22
</td>
</tr>
<tr>
<td style="text-align:left;">
code de l’urbanisme
</td>
<td style="text-align:right;">
10
</td>
<td style="text-align:right;">
127
</td>
</tr>
<tr>
<td style="text-align:left;">
code de la consommation
</td>
<td style="text-align:right;">
3
</td>
<td style="text-align:right;">
19
</td>
</tr>
<tr>
<td style="text-align:left;">
code de la construction et de l’habitation
</td>
<td style="text-align:right;">
13
</td>
<td style="text-align:right;">
130
</td>
</tr>
<tr>
<td style="text-align:left;">
code de la défense
</td>
<td style="text-align:right;">
2
</td>
<td style="text-align:right;">
36
</td>
</tr>
<tr>
<td style="text-align:left;">
code de la propriété intellectuelle
</td>
<td style="text-align:right;">
5
</td>
<td style="text-align:right;">
16
</td>
</tr>
<tr>
<td style="text-align:left;">
code de la recherche
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
</tr>
<tr>
<td style="text-align:left;">
code de la route
</td>
<td style="text-align:right;">
4
</td>
<td style="text-align:right;">
5
</td>
</tr>
<tr>
<td style="text-align:left;">
code de la santé publique
</td>
<td style="text-align:right;">
80
</td>
<td style="text-align:right;">
502
</td>
</tr>
<tr>
<td style="text-align:left;">
code de la sécurité intérieure
</td>
<td style="text-align:right;">
8
</td>
<td style="text-align:right;">
13
</td>
</tr>
<tr>
<td style="text-align:left;">
code de la sécurité sociale
</td>
<td style="text-align:right;">
76
</td>
<td style="text-align:right;">
260
</td>
</tr>
<tr>
<td style="text-align:left;">
code de procédure pénale
</td>
<td style="text-align:right;">
18
</td>
<td style="text-align:right;">
48
</td>
</tr>
<tr>
<td style="text-align:left;">
code des assurances
</td>
<td style="text-align:right;">
20
</td>
<td style="text-align:right;">
79
</td>
</tr>
<tr>
<td style="text-align:left;">
code des juridictions financières
</td>
<td style="text-align:right;">
2
</td>
<td style="text-align:right;">
56
</td>
</tr>
<tr>
<td style="text-align:left;">
code des postes et des communications électroniques
</td>
<td style="text-align:right;">
8
</td>
<td style="text-align:right;">
44
</td>
</tr>
<tr>
<td style="text-align:left;">
code des transports
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
16
</td>
</tr>
<tr>
<td style="text-align:left;">
code du cinéma et de l’image animée
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
</tr>
<tr>
<td style="text-align:left;">
code du patrimoine
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
6
</td>
</tr>
<tr>
<td style="text-align:left;">
code du sport
</td>
<td style="text-align:right;">
4
</td>
<td style="text-align:right;">
24
</td>
</tr>
<tr>
<td style="text-align:left;">
code du tourisme
</td>
<td style="text-align:right;">
9
</td>
<td style="text-align:right;">
8
</td>
</tr>
<tr>
<td style="text-align:left;">
code du travail
</td>
<td style="text-align:right;">
51
</td>
<td style="text-align:right;">
346
</td>
</tr>
<tr>
<td style="text-align:left;">
code électoral
</td>
<td style="text-align:right;">
9
</td>
<td style="text-align:right;">
31
</td>
</tr>
<tr>
<td style="text-align:left;">
code général de la propriété des personnes publiques
</td>
<td style="text-align:right;">
2
</td>
<td style="text-align:right;">
4
</td>
</tr>
<tr>
<td style="text-align:left;">
code général des collectivités territoriales
</td>
<td style="text-align:right;">
35
</td>
<td style="text-align:right;">
63
</td>
</tr>
<tr>
<td style="text-align:left;">
code pénal
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
5
</td>
</tr>
</tbody>
</table>
