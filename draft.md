Draft
================

    ## `summarise()` has grouped output by 'partie', 'sous_partie', 'article'. You can
    ## override using the `.groups` argument.

<table>
<thead>
<tr>
<th style="text-align:left;">
partie
</th>
<th style="text-align:left;">
sous\_partie
</th>
<th style="text-align:left;">
article
</th>
<th style="text-align:left;">
type
</th>
<th style="text-align:right;">
nb
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:left;">
NA
</td>
<td style="text-align:left;">
D371-3
</td>
<td style="text-align:left;">
Modification
</td>
<td style="text-align:right;">
25
</td>
</tr>
<tr>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:left;">
NA
</td>
<td style="text-align:left;">
D373-2
</td>
<td style="text-align:left;">
Modification
</td>
<td style="text-align:right;">
21
</td>
</tr>
<tr>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:left;">
NA
</td>
<td style="text-align:left;">
D374-3
</td>
<td style="text-align:left;">
Modification
</td>
<td style="text-align:right;">
20
</td>
</tr>
<tr>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:left;">
NA
</td>
<td style="text-align:left;">
D718-5
</td>
<td style="text-align:left;">
Modification
</td>
<td style="text-align:right;">
15
</td>
</tr>
<tr>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:left;">
NA
</td>
<td style="text-align:left;">
D683-2
</td>
<td style="text-align:left;">
Modification
</td>
<td style="text-align:right;">
14
</td>
</tr>
<tr>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:left;">
NA
</td>
<td style="text-align:left;">
D684-2
</td>
<td style="text-align:left;">
Modification
</td>
<td style="text-align:right;">
14
</td>
</tr>
</tbody>
</table>

    ## `summarise()` has grouped output by 'partie'. You can override using the
    ## `.groups` argument.

<table>
<thead>
<tr>
<th style="text-align:left;">
partie
</th>
<th style="text-align:left;">
type
</th>
<th style="text-align:right;">
nb
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
Législative
</td>
<td style="text-align:left;">
Ajout
</td>
<td style="text-align:right;">
47
</td>
</tr>
<tr>
<td style="text-align:left;">
Législative
</td>
<td style="text-align:left;">
Modification
</td>
<td style="text-align:right;">
269
</td>
</tr>
<tr>
<td style="text-align:left;">
Législative
</td>
<td style="text-align:left;">
Suppression
</td>
<td style="text-align:right;">
21
</td>
</tr>
<tr>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:left;">
Ajout
</td>
<td style="text-align:right;">
441
</td>
</tr>
<tr>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:left;">
Modification
</td>
<td style="text-align:right;">
927
</td>
</tr>
<tr>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:left;">
Suppression
</td>
<td style="text-align:right;">
228
</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th style="text-align:left;">
type
</th>
<th style="text-align:right;">
nb
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
Ajout
</td>
<td style="text-align:right;">
488
</td>
</tr>
<tr>
<td style="text-align:left;">
Modification
</td>
<td style="text-align:right;">
1196
</td>
</tr>
<tr>
<td style="text-align:left;">
Suppression
</td>
<td style="text-align:right;">
249
</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th style="text-align:left;">
date
</th>
<th style="text-align:right;">
nb
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
2020-01-01
</td>
<td style="text-align:right;">
392
</td>
</tr>
<tr>
<td style="text-align:left;">
2019-09-02
</td>
<td style="text-align:right;">
159
</td>
</tr>
<tr>
<td style="text-align:left;">
2020-08-03
</td>
<td style="text-align:right;">
71
</td>
</tr>
<tr>
<td style="text-align:left;">
2020-06-28
</td>
<td style="text-align:right;">
68
</td>
</tr>
<tr>
<td style="text-align:left;">
2020-12-27
</td>
<td style="text-align:right;">
66
</td>
</tr>
<tr>
<td style="text-align:left;">
2018-01-01
</td>
<td style="text-align:right;">
50
</td>
</tr>
</tbody>
</table>

    ## `summarise()` has grouped output by 'date', 'partie'. You can override using
    ## the `.groups` argument.
    ## `summarise()` has grouped output by 'date'. You can override using the
    ## `.groups` argument.
    ## Joining, by = c("date", "partie")

![](draft_files/figure-gfm/code-1.png)<!-- -->

## Jumps

    ## `summarise()` has grouped output by 'code', 'date'. You can override using the
    ## `.groups` argument.
    ## Joining, by = "fin"
    ## Joining, by = "fin"

<table>
<thead>
<tr>
<th style="text-align:left;">
code
</th>
<th style="text-align:left;">
date
</th>
<th style="text-align:left;">
partie
</th>
<th style="text-align:right;">
nb\_articles
</th>
<th style="text-align:right;">
nb\_alineas
</th>
<th style="text-align:right;">
nb\_mots
</th>
<th style="text-align:right;">
nb\_modifications
</th>
<th style="text-align:right;">
nb\_ajouts
</th>
<th style="text-align:right;">
nb\_suppressions
</th>
<th style="text-align:left;">
fin
</th>
<th style="text-align:left;">
président
</th>
<th style="text-align:right;">
nb\_conservations
</th>
<th style="text-align:right;">
check
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
code de l’énergie
</td>
<td style="text-align:left;">
2017-05-11
</td>
<td style="text-align:left;">
Législative
</td>
<td style="text-align:right;">
849
</td>
<td style="text-align:right;">
2974
</td>
<td style="text-align:right;">
119281
</td>
<td style="text-align:right;">
233
</td>
<td style="text-align:right;">
171
</td>
<td style="text-align:right;">
48
</td>
<td style="text-align:left;">
2017
</td>
<td style="text-align:left;">
Hollande
</td>
<td style="text-align:right;">
445
</td>
<td style="text-align:right;">
-1
</td>
</tr>
<tr>
<td style="text-align:left;">
code de l’entrée et du séjour des étrangers et du droit d’asile
</td>
<td style="text-align:left;">
2022-02-23
</td>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:right;">
1230
</td>
<td style="text-align:right;">
17136
</td>
<td style="text-align:right;">
419247
</td>
<td style="text-align:right;">
202
</td>
<td style="text-align:right;">
1027
</td>
<td style="text-align:right;">
592
</td>
<td style="text-align:left;">
2022
</td>
<td style="text-align:left;">
Macron
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
1
</td>
</tr>
<tr>
<td style="text-align:left;">
code de l’organisation judiciaire
</td>
<td style="text-align:left;">
2012-03-19
</td>
<td style="text-align:left;">
Législative
</td>
<td style="text-align:right;">
293
</td>
<td style="text-align:right;">
654
</td>
<td style="text-align:right;">
19770
</td>
<td style="text-align:right;">
45
</td>
<td style="text-align:right;">
24
</td>
<td style="text-align:right;">
110
</td>
<td style="text-align:left;">
2012
</td>
<td style="text-align:left;">
Sarkozy
</td>
<td style="text-align:right;">
224
</td>
<td style="text-align:right;">
1
</td>
</tr>
<tr>
<td style="text-align:left;">
code de l’organisation judiciaire
</td>
<td style="text-align:left;">
2012-03-19
</td>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:right;">
600
</td>
<td style="text-align:right;">
12070
</td>
<td style="text-align:right;">
141761
</td>
<td style="text-align:right;">
70
</td>
<td style="text-align:right;">
528
</td>
<td style="text-align:right;">
451
</td>
<td style="text-align:left;">
2012
</td>
<td style="text-align:left;">
Sarkozy
</td>
<td style="text-align:right;">
2
</td>
<td style="text-align:right;">
2
</td>
</tr>
<tr>
<td style="text-align:left;">
code de l’organisation judiciaire
</td>
<td style="text-align:left;">
2017-05-18
</td>
<td style="text-align:left;">
Législative
</td>
<td style="text-align:right;">
319
</td>
<td style="text-align:right;">
547
</td>
<td style="text-align:right;">
16166
</td>
<td style="text-align:right;">
27
</td>
<td style="text-align:right;">
32
</td>
<td style="text-align:right;">
5
</td>
<td style="text-align:left;">
2017
</td>
<td style="text-align:left;">
Hollande
</td>
<td style="text-align:right;">
260
</td>
<td style="text-align:right;">
-1
</td>
</tr>
<tr>
<td style="text-align:left;">
code de l’organisation judiciaire
</td>
<td style="text-align:left;">
2017-05-18
</td>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:right;">
640
</td>
<td style="text-align:right;">
9498
</td>
<td style="text-align:right;">
91814
</td>
<td style="text-align:right;">
101
</td>
<td style="text-align:right;">
48
</td>
<td style="text-align:right;">
6
</td>
<td style="text-align:left;">
2017
</td>
<td style="text-align:left;">
Hollande
</td>
<td style="text-align:right;">
491
</td>
<td style="text-align:right;">
-2
</td>
</tr>
<tr>
<td style="text-align:left;">
code de la consommation
</td>
<td style="text-align:left;">
2022-03-25
</td>
<td style="text-align:left;">
Législative
</td>
<td style="text-align:right;">
1275
</td>
<td style="text-align:right;">
3898
</td>
<td style="text-align:right;">
135349
</td>
<td style="text-align:right;">
252
</td>
<td style="text-align:right;">
169
</td>
<td style="text-align:right;">
46
</td>
<td style="text-align:left;">
2022
</td>
<td style="text-align:left;">
Macron
</td>
<td style="text-align:right;">
854
</td>
<td style="text-align:right;">
1
</td>
</tr>
<tr>
<td style="text-align:left;">
code de la consommation
</td>
<td style="text-align:left;">
2022-03-25
</td>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:right;">
788
</td>
<td style="text-align:right;">
4510
</td>
<td style="text-align:right;">
109685
</td>
<td style="text-align:right;">
161
</td>
<td style="text-align:right;">
104
</td>
<td style="text-align:right;">
46
</td>
<td style="text-align:left;">
2022
</td>
<td style="text-align:left;">
Macron
</td>
<td style="text-align:right;">
523
</td>
<td style="text-align:right;">
1
</td>
</tr>
<tr>
<td style="text-align:left;">
code de la santé publique
</td>
<td style="text-align:left;">
2007-05-16
</td>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:right;">
6984
</td>
<td style="text-align:right;">
49461
</td>
<td style="text-align:right;">
1544367
</td>
<td style="text-align:right;">
72
</td>
<td style="text-align:right;">
6781
</td>
<td style="text-align:right;">
2483
</td>
<td style="text-align:left;">
2007
</td>
<td style="text-align:left;">
Chirac 2
</td>
<td style="text-align:right;">
131
</td>
<td style="text-align:right;">
1
</td>
</tr>
<tr>
<td style="text-align:left;">
code de la santé publique
</td>
<td style="text-align:left;">
2012-05-15
</td>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:right;">
7911
</td>
<td style="text-align:right;">
44343
</td>
<td style="text-align:right;">
1145078
</td>
<td style="text-align:right;">
2442
</td>
<td style="text-align:right;">
2107
</td>
<td style="text-align:right;">
1179
</td>
<td style="text-align:left;">
2012
</td>
<td style="text-align:left;">
Sarkozy
</td>
<td style="text-align:right;">
3362
</td>
<td style="text-align:right;">
-1
</td>
</tr>
<tr>
<td style="text-align:left;">
code des postes et des communications électroniques
</td>
<td style="text-align:left;">
2002-02-21
</td>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:right;">
560
</td>
<td style="text-align:right;">
2587
</td>
<td style="text-align:right;">
80157
</td>
<td style="text-align:right;">
86
</td>
<td style="text-align:right;">
151
</td>
<td style="text-align:right;">
153
</td>
<td style="text-align:left;">
2002
</td>
<td style="text-align:left;">
Chirac
</td>
<td style="text-align:right;">
323
</td>
<td style="text-align:right;">
1
</td>
</tr>
<tr>
<td style="text-align:left;">
code des postes et des communications électroniques
</td>
<td style="text-align:left;">
2007-05-11
</td>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:right;">
464
</td>
<td style="text-align:right;">
3495
</td>
<td style="text-align:right;">
120505
</td>
<td style="text-align:right;">
133
</td>
<td style="text-align:right;">
219
</td>
<td style="text-align:right;">
314
</td>
<td style="text-align:left;">
2007
</td>
<td style="text-align:left;">
Chirac 2
</td>
<td style="text-align:right;">
112
</td>
<td style="text-align:right;">
-1
</td>
</tr>
<tr>
<td style="text-align:left;">
code du travail
</td>
<td style="text-align:left;">
2012-05-11
</td>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:right;">
6580
</td>
<td style="text-align:right;">
48576
</td>
<td style="text-align:right;">
1409811
</td>
<td style="text-align:right;">
18
</td>
<td style="text-align:right;">
6468
</td>
<td style="text-align:right;">
3362
</td>
<td style="text-align:left;">
2012
</td>
<td style="text-align:left;">
Sarkozy
</td>
<td style="text-align:right;">
94
</td>
<td style="text-align:right;">
5
</td>
</tr>
<tr>
<td style="text-align:left;">
code du travail
</td>
<td style="text-align:left;">
2017-05-12
</td>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:right;">
6885
</td>
<td style="text-align:right;">
48456
</td>
<td style="text-align:right;">
1418459
</td>
<td style="text-align:right;">
1297
</td>
<td style="text-align:right;">
1170
</td>
<td style="text-align:right;">
860
</td>
<td style="text-align:left;">
2017
</td>
<td style="text-align:left;">
Hollande
</td>
<td style="text-align:right;">
4418
</td>
<td style="text-align:right;">
-5
</td>
</tr>
<tr>
<td style="text-align:left;">
code électoral
</td>
<td style="text-align:left;">
1973-07-12
</td>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
2
</td>
<td style="text-align:right;">
82
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:left;">
1973
</td>
<td style="text-align:left;">
Pompidou
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
1
</td>
</tr>
<tr>
<td style="text-align:left;">
code électoral
</td>
<td style="text-align:left;">
1981-03-28
</td>
<td style="text-align:left;">
Réglementaire
</td>
<td style="text-align:right;">
162
</td>
<td style="text-align:right;">
424
</td>
<td style="text-align:right;">
13987
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
162
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:left;">
1981
</td>
<td style="text-align:left;">
Giscard
</td>
<td style="text-align:right;">
0
</td>
<td style="text-align:right;">
-1
</td>
</tr>
</tbody>
</table>

## Code de l’éducation

<img src="draft_files/figure-gfm/education-1.png" width="672" />

![](draft_files/figure-gfm/education.facet-1.png)<!-- -->

## Tous les codes dernier mandat

![](draft_files/figure-gfm/touscodes-1.png)<!-- -->

![](draft_files/figure-gfm/touscodes.ratio-1.png)<!-- -->

    ## `summarise()` has grouped output by 'code', 'président'. You can override using
    ## the `.groups` argument.

    ## Warning: Removed 11 rows containing missing values (geom_point).

![](draft_files/figure-gfm/touscodes.ratio.2-1.png)<!-- -->

    ## Warning: Removed 72 rows containing missing values (position_stack).

![](draft_files/figure-gfm/touscodes.ratio.3-1.png)<!-- -->

## Tous les codes tous les mandats

![](draft_files/figure-gfm/tous.data-1.png)<!-- -->
