CPESR
================
CPESR
2024-01-15

## Données

    ##  [1] "article_id"          "article_num"         "article_date_debut" 
    ##  [4] "article_etat"        "lien_id"             "lien_typelien"      
    ##  [7] "lien_sens"           "lien_datesignatexte" "lien_naturetexte"   
    ## [10] "lien_numtexte"       "lien_num"            "lien_texte"         
    ## [13] "lien_url"            "partie"

## Explorations

### Doublons

    ##  [1] article_id          article_num         article_date_debut 
    ##  [4] article_etat        lien_id             lien_typelien      
    ##  [7] lien_sens           lien_datesignatexte lien_naturetexte   
    ## [10] lien_numtexte       lien_num            lien_texte         
    ## [13] lien_url            partie              nb                 
    ## <0 lignes> (ou 'row.names' de longueur nulle)

### Type lien

<details>
<summary>
Voir les données
</summary>

| lien_typelien |    nb |
|:--------------|------:|
| CONCORDANCE   | 10690 |
| CONCORDE      |  5006 |
| CODIFICATION  |  9281 |
| CITATION      | 90684 |
| MODIFICATION  |   752 |
| MODIFIE       |  5282 |

</details>

### Type état

<details>
<summary>
Voir les données
</summary>

| article_etat    |    nb |
|:----------------|------:|
| MODIFIE         | 82097 |
| VIGUEUR         | 33428 |
| TRANSFERE       |  1051 |
| ABROGE          |  8046 |
| MODIFIE_MORT_NE |  1021 |
| VIGUEUR_DIFF    |   953 |

</details>

### Nombre de versions

<details>
<summary>
Voir les données
</summary>

| versions |   nb |
|---------:|-----:|
|        1 | 3347 |
|        2 | 1481 |
|        3 |  724 |
|        4 |  294 |
|        5 |  140 |
|        6 |   66 |

</details>

## M. Macron

<details>
<summary>
Nb versions
</summary>

| partie        | nb_versions |
|:--------------|------------:|
| Législative   |          77 |
| Réglementaire |         257 |

</details>
<details>
<summary>
Articles les plus modifiés
</summary>

    ## Joining with `by = join_by(article_num)`

| article_num | partie        | nb_versions | url                                                                    |
|:------------|:--------------|------------:|:-----------------------------------------------------------------------|
| L721-2      | Législative   |           7 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045293824> |
| L312-9      | Législative   |           6 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047666746> |
| L312-15     | Législative   |           6 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045292525> |
| L371-1      | Législative   |           5 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043484834> |
| L771-1      | Législative   |           5 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043485415> |
| L773-1      | Législative   |           5 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042814878> |
| L774-1      | Législative   |           5 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042814828> |
| L131-5      | Législative   |           4 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043982594> |
| L261-1      | Législative   |           4 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039163423> |
| L442-2      | Législative   |           4 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045292494> |
| D371-3      | Réglementaire |          27 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045039726> |
| D373-2      | Réglementaire |          22 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044381557> |
| D374-3      | Réglementaire |          22 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044381714> |
| D718-5      | Réglementaire |          22 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047266607> |
| D711-6-1    | Réglementaire |          16 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048388742> |
| D612-32-2   | Réglementaire |          14 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047094723> |
| D681-2      | Réglementaire |          14 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045043588> |
| D683-2      | Réglementaire |          14 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043195661> |
| D684-2      | Réglementaire |          14 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043195604> |
| D612-34     | Réglementaire |          11 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047967224> |

</details>
<details>
<summary>
Nb textes de modification par nature
</summary>

| lien_naturetexte |  nb |
|:-----------------|----:|
| LOI              |  55 |
| ORDONNANCE       |  16 |
| DECISION         |   2 |
| DECRET           | 332 |

</details>
<details>
<summary>
Top textes modifiants
</summary>

| lien_naturetexte | lien_numtexte | lien_datesignatexte | nb_modifications | lien_url                                                      |
|:-----------------|:--------------|:--------------------|-----------------:|:--------------------------------------------------------------|
| DECRET           | 2019-1558     | 2019-12-30          |              201 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039700476> |
| LOI              | 2019-791      | 2019-07-26          |              151 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038829065> |
| DECRET           | 2019-1554     | 2019-12-30          |              110 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039700158> |
| DECRET           | 2018-614      | 2018-07-16          |               63 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037202561> |
| DECRET           | 2021-1907     | 2021-12-30          |               55 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044638867> |
| LOI              | 2020-1674     | 2020-12-24          |               49 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042738027> |
| DECRET           | 2023-856      | 2023-09-05          |               49 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048046061> |
| DECRET           | 2020-785      | 2020-06-26          |               47 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042044408> |
| DECRET           | 2021-1910     | 2021-12-30          |               44 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044740106> |
| ORDONNANCE       | 2021-1747     | 2021-12-22          |               40 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044547312> |

</details>
<details>
<summary>
Textes modifiants (hors décrets)
</summary>

| lien_naturetexte | lien_numtexte | lien_datesignatexte | lien_url                                                      |
|:-----------------|:--------------|:--------------------|:--------------------------------------------------------------|
| ORDONNANCE       | 2017-1491     | 2017-10-25          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000035879962> |
| ORDONNANCE       | 2017-1718     | 2017-12-20          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000036240557> |
| LOI              | 2017-1837     | 2017-12-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000036339197> |
| LOI              | 2018-166      | 2018-03-08          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000036683777> |
| LOI              | 2018-217      | 2018-03-29          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000036755446> |
| LOI              | 2018-266      | 2018-04-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000036798673> |
| LOI              | 2018-493      | 2018-06-20          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037085952> |
| LOI              | 2018-698      | 2018-08-03          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037284333> |
| LOI              | 2018-703      | 2018-08-03          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037284450> |
| LOI              | 2018-699      | 2018-08-03          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037284338> |

</details>

## Bacheliers

<details>
<summary>
Nb versions
</summary>

| partie        | nb_versions |
|:--------------|------------:|
| Législative   |         169 |
| Réglementaire |         482 |

</details>
<details>
<summary>
Articles les plus modifiés
</summary>

    ## Joining with `by = join_by(article_num)`

| article_num | partie        | nb_versions | url                                                                    |
|:------------|:--------------|------------:|:-----------------------------------------------------------------------|
| L214-13     | Législative   |          10 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037390508> |
| L312-15     | Législative   |          10 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045292525> |
| L335-5      | Législative   |          10 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046774910> |
| L683-1      | Législative   |          10 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043485268> |
| L684-1      | Législative   |          10 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043485227> |
| L681-1      | Législative   |           9 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043485309> |
| L822-1      | Législative   |           9 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046873650> |
| L312-9      | Législative   |           8 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047666746> |
| L721-2      | Législative   |           8 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045293824> |
| L771-1      | Législative   |           8 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043485415> |
| D718-5      | Réglementaire |          45 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047266607> |
| D371-3      | Réglementaire |          38 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045039726> |
| D373-2      | Réglementaire |          31 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044381557> |
| D374-3      | Réglementaire |          31 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044381714> |
| D683-2      | Réglementaire |          19 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043195661> |
| D684-2      | Réglementaire |          19 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043195604> |
| D681-2      | Réglementaire |          18 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045043588> |
| D711-3      | Réglementaire |          18 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048388745> |
| D612-32-2   | Réglementaire |          17 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047094723> |
| D711-6-1    | Réglementaire |          16 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048388742> |

</details>
<details>
<summary>
Nb textes de modification par nature
</summary>

| lien_naturetexte |  nb |
|:-----------------|----:|
| LOI              | 125 |
| ORDONNANCE       |  37 |
| DECRET           | 595 |
| DECISION         |   6 |
| LOI_ORGANIQUE    |   1 |

</details>
<details>
<summary>
Top textes modifiants
</summary>

| lien_naturetexte | lien_numtexte | lien_datesignatexte | nb_modifications | lien_url                                                      |
|:-----------------|:--------------|:--------------------|-----------------:|:--------------------------------------------------------------|
| DECRET           | 2019-1558     | 2019-12-30          |              201 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039700476> |
| DECRET           | 2012-16       | 2012-01-05          |              175 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000025105579> |
| LOI              | 2019-791      | 2019-07-26          |              151 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038829065> |
| DECRET           | 2015-652      | 2015-06-10          |              111 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030715134> |
| DECRET           | 2019-1554     | 2019-12-30          |              110 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039700158> |
| LOI              | 2013-660      | 2013-07-22          |              100 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027735009> |
| DECRET           | 2016-1597     | 2016-11-25          |               79 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033479390> |
| LOI              | 2013-595      | 2013-07-08          |               74 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027677984> |
| DECRET           | 2018-614      | 2018-07-16          |               63 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037202561> |
| ORDONNANCE       | 2010-462      | 2010-05-06          |               62 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022176680> |

</details>
<details>
<summary>
Textes modifiants (hors décrets)
</summary>

| lien_naturetexte | lien_numtexte | lien_datesignatexte | lien_url                                                      |
|:-----------------|:--------------|:--------------------|:--------------------------------------------------------------|
| LOI              | 2009-1312     | 2009-10-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000021208103> |
| LOI              | 2009-1437     | 2009-11-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000021312490> |
| LOI              | 2009-1503     | 2009-12-08          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000021451610> |
| ORDONNANCE       | 2009-1534     | 2009-12-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000021447543> |
| ORDONNANCE       | 2010-49       | 2010-01-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000021683301> |
| LOI              | 2010-121      | 2010-02-08          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000021794951> |
| ORDONNANCE       | 2010-177      | 2010-02-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000021868310> |
| LOI              | 2010-241      | 2010-03-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000021954325> |
| ORDONNANCE       | 2010-331      | 2010-03-25          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022018594> |
| ORDONNANCE       | 2010-462      | 2010-05-06          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022176680> |

</details>

## Toujours

<details>
<summary>
Nb versions
</summary>

| partie        | nb_versions |
|:--------------|------------:|
| Législative   |         248 |
| Réglementaire |         554 |

</details>
<details>
<summary>
Articles les plus modifiés
</summary>

    ## Joining with `by = join_by(article_num)`

| article_num | partie        | nb_versions | url                                                                    |
|:------------|:--------------|------------:|:-----------------------------------------------------------------------|
| L214-13     | Législative   |          19 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037390508> |
| L683-1      | Législative   |          14 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043485268> |
| L684-1      | Législative   |          14 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043485227> |
| L312-15     | Législative   |          13 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045292525> |
| L335-5      | Législative   |          13 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046774910> |
| L681-1      | Législative   |          13 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043485309> |
| L973-1      | Législative   |          13 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042814773> |
| L974-1      | Législative   |          13 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042814726> |
| L822-1      | Législative   |          12 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046873650> |
| L261-1      | Législative   |          11 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039163423> |
| D718-5      | Réglementaire |          45 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047266607> |
| D371-3      | Réglementaire |          39 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045039726> |
| D373-2      | Réglementaire |          32 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044381557> |
| D374-3      | Réglementaire |          32 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044381714> |
| D683-2      | Réglementaire |          19 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043195661> |
| D684-2      | Réglementaire |          19 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043195604> |
| D681-2      | Réglementaire |          18 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045043588> |
| D711-3      | Réglementaire |          18 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048388745> |
| D612-32-2   | Réglementaire |          17 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047094723> |
| D711-6-1    | Réglementaire |          16 | <https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048388742> |

</details>
<details>
<summary>
Nb textes de modification par nature
</summary>

| lien_naturetexte |  nb |
|:-----------------|----:|
| LOI              | 177 |
| ORDONNANCE       |  59 |
| DECRET           | 657 |
| DECISION         |   6 |
| LOI_ORGANIQUE    |   1 |

</details>
<details>
<summary>
Top textes modifiants
</summary>

| lien_naturetexte | lien_numtexte | lien_datesignatexte | nb_modifications | lien_url                                                      |
|:-----------------|:--------------|:--------------------|-----------------:|:--------------------------------------------------------------|
| DECRET           | 2019-1558     | 2019-12-30          |              201 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039700476> |
| DECRET           | 2012-16       | 2012-01-05          |              175 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000025105579> |
| LOI              | 2019-791      | 2019-07-26          |              151 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038829065> |
| DECRET           | 2015-652      | 2015-06-10          |              111 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030715134> |
| DECRET           | 2019-1554     | 2019-12-30          |              110 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039700158> |
| LOI              | 2013-660      | 2013-07-22          |              100 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027735009> |
| DECRET           | 2016-1597     | 2016-11-25          |               79 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033479390> |
| LOI              | 2005-380      | 2005-04-23          |               76 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000259787> |
| LOI              | 2013-595      | 2013-07-08          |               74 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027677984> |
| DECRET           | 2018-614      | 2018-07-16          |               63 | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037202561> |

</details>
<details>
<summary>
Textes modifiants (hors décrets)
</summary>

| lien_naturetexte | lien_numtexte | lien_datesignatexte | lien_url                                                      |
|:-----------------|:--------------|:--------------------|:--------------------------------------------------------------|
| LOI              | 2000-597      | 2000-06-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000204851> |
| ORDONNANCE       | 2000-916      | 2000-09-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000219672> |
| LOI              | 2000-1207     | 2000-12-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000387814> |
| ORDONNANCE       | 2001-174      | 2001-02-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000755333> |
| LOI              | 2001-588      | 2001-07-04          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000222631> |
| LOI              | 2001-624      | 2001-07-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000757800> |
| LOI              | 2002-73       | 2002-01-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000408905> |
| LOI              | 2002-92       | 2002-01-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000409466> |
| ORDONNANCE       | 2002-198      | 2002-02-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000593677> |
| LOI              | 2002-276      | 2002-02-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000593100> |

</details>

## Mandats présidentiels

    ## Joining with `by = join_by(date)`

<img src="legifouille_files/figure-gfm/mandats-1.png" width="672" />

    ## 
    ## Attachement du package : 'lubridate'

    ## Les objets suivants sont masqués depuis 'package:base':
    ## 
    ##     date, intersect, setdiff, union

<img src="legifouille_files/figure-gfm/mandats.proj-1.png" width="672" />
