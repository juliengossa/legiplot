CPESR
================
CPESR
2024-01-16

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
| LOI              | 2018-771      | 2018-09-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037367660> |
| LOI              | 2018-778      | 2018-09-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037381808> |
| LOI              | 2018-938      | 2018-10-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037547946> |
| ORDONNANCE       | 2018-1125     | 2018-12-12          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037800506> |
| LOI              | 2018-1202     | 2018-12-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037847559> |
| LOI              | 2018-1203     | 2018-12-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037847585> |
| LOI              | 2018-1317     | 2018-12-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037882341> |
| LOI              | 2019-222      | 2019-03-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038261631> |
| LOI              | 2019-774      | 2019-07-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038821260> |
| LOI              | 2019-791      | 2019-07-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038829065> |
| LOI              | 2019-828      | 2019-08-06          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038889182> |
| ORDONNANCE       | 2019-861      | 2019-08-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038940323> |
| LOI              | 2019-1461     | 2019-12-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039681877> |
| LOI              | 2019-1479     | 2019-12-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039683923> |
| ORDONNANCE       | 2020-71       | 2020-01-29          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000041506557> |
| LOI              | 2020-105      | 2020-02-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000041553759> |
| DECISION         | 2020-834 QPC  | 2020-04-03          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000041782007> |
| LOI              | 2020-760      | 2020-06-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042025624> |
| LOI              | 2020-766      | 2020-06-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042031970> |
| LOI              | 2020-840      | 2020-07-03          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042079128> |
| ORDONNANCE       | 2020-1256     | 2020-10-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042424239> |
| LOI              | 2020-1525     | 2020-12-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042619877> |
| ORDONNANCE       | 2020-1733     | 2020-12-16          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042754770> |
| LOI              | 2020-1674     | 2020-12-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042738027> |
| LOI              | 2021-502      | 2021-04-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043421566> |
| ORDONNANCE       | 2021-552      | 2021-05-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043477594> |
| ORDONNANCE       | 2021-611      | 2021-05-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043511942> |
| LOI              | 2021-641      | 2021-05-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043524722> |
| LOI              | 2021-695      | 2021-06-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043575111> |
| ORDONNANCE       | 2021-702      | 2021-06-02          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043590607> |
| LOI              | 2021-875      | 2021-07-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043741543> |
| LOI              | 2021-874      | 2021-07-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043741537> |
| DECISION         | 2021-823 DC   | 2021-08-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043964902> |
| LOI              | 2021-1104     | 2021-08-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043956924> |
| LOI              | 2021-1109     | 2021-08-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043964778> |
| LOI              | 2021-1485     | 2021-11-15          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044327272> |
| ORDONNANCE       | 2021-1574     | 2021-11-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044411525> |
| LOI              | 2021-1539     | 2021-11-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044387560> |
| LOI              | 2021-1678     | 2021-12-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044513764> |
| LOI              | 2021-1716     | 2021-12-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044537507> |
| ORDONNANCE       | 2021-1747     | 2021-12-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044547312> |
| LOI              | 2021-1754     | 2021-12-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044553428> |
| LOI              | 2021-1774     | 2021-12-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044559192> |
| LOI              | 2022-52       | 2022-01-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045067923> |
| LOI              | 2022-217      | 2022-02-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045197395> |
| LOI              | 2022-272      | 2022-02-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045268755> |
| LOI              | 2022-296      | 2022-03-02          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045287568> |
| LOI              | 2022-299      | 2022-03-02          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045287658> |
| ORDONNANCE       | 2022-408      | 2022-03-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045398055> |
| ORDONNANCE       | 2022-583      | 2022-04-20          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045614880> |
| ORDONNANCE       | 2022-1521     | 2022-12-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046694513> |
| LOI              | 2022-1574     | 2022-12-16          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046751169> |
| LOI              | 2022-1598     | 2022-12-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046771781> |
| LOI              | 2022-1616     | 2022-12-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046791754> |
| LOI              | 2022-1726     | 2022-12-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046845631> |
| ORDONNANCE       | 2023-15       | 2023-01-18          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047007968> |
| LOI              | 2023-29       | 2023-01-25          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047055162> |
| LOI              | 2023-380      | 2023-05-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047561974> |
| LOI              | 2023-451      | 2023-06-09          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047663185> |
| LOI              | 2023-479      | 2023-06-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047709059> |
| LOI              | 2023-580      | 2023-07-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047805414> |
| LOI              | 2023-610      | 2023-07-18          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047858021> |
| LOI              | 2023-703      | 2023-08-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047914986> |

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
| LOI              | 2010-500      | 2010-05-18          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022227311> |
| LOI              | 2010-597      | 2010-06-03          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022308227> |
| ORDONNANCE       | 2010-638      | 2010-06-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022330885> |
| LOI_ORGANIQUE    | 2010-704      | 2010-06-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022402454> |
| LOI              | 2010-751      | 2010-07-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022436528> |
| LOI              | 2010-769      | 2010-07-09          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022454032> |
| LOI              | 2010-788      | 2010-07-12          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022470434> |
| LOI              | 2010-853      | 2010-07-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022511227> |
| LOI              | 2010-874      | 2010-07-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022521587> |
| LOI              | 2010-1127     | 2010-09-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022862522> |
| ORDONNANCE       | 2010-1307     | 2010-10-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022990793> |
| LOI              | 2010-1330     | 2010-11-09          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023022127> |
| LOI              | 2010-1487     | 2010-12-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023174577> |
| LOI              | 2010-1536     | 2010-12-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023229524> |
| LOI              | 2010-1594     | 2010-12-20          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023261006> |
| LOI              | 2010-1657     | 2010-12-29          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023314376> |
| LOI              | 2011-267      | 2011-03-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023707312> |
| LOI              | 2011-302      | 2011-03-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023751262> |
| LOI              | 2011-334      | 2011-03-29          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023781252> |
| LOI              | 2011-525      | 2011-05-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000024021430> |
| LOI              | 2011-893      | 2011-07-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000024408887> |
| LOI              | 2011-940      | 2011-08-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000024457033> |
| LOI              | 2011-1977     | 2011-12-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000025044460> |
| LOI              | 2012-158      | 2012-02-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000025269948> |
| LOI              | 2012-300      | 2012-03-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000025441587> |
| ORDONNANCE       | 2012-351      | 2012-03-12          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000025498645> |
| LOI              | 2012-347      | 2012-03-12          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000025489865> |
| LOI              | 2012-409      | 2012-03-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000025582235> |
| LOI              | 2012-1404     | 2012-12-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000026785322> |
| DECISION         | 354947        | 2012-12-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000026856692> |
| LOI              | 2013-108      | 2013-01-31          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027012750> |
| LOI              | 2013-403      | 2013-05-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027414225> |
| LOI              | 2013-595      | 2013-07-08          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027677984> |
| LOI              | 2013-660      | 2013-07-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027735009> |
| LOI              | 2013-659      | 2013-07-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027734839> |
| LOI              | 2013-1278     | 2013-12-29          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000028399511> |
| LOI              | 2014-58       | 2014-01-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000028526298> |
| LOI              | 2014-173      | 2014-02-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000028636804> |
| LOI              | 2014-288      | 2014-03-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000028683576> |
| ORDONNANCE       | 2014-693      | 2014-06-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029139960> |
| ORDONNANCE       | 2014-691      | 2014-06-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029139765> |
| ORDONNANCE       | 2014-692      | 2014-06-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029145752> |
| LOI              | 2014-788      | 2014-07-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029223331> |
| DECISION         | 372835        | 2014-07-16          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029279331> |
| ORDONNANCE       | 2014-807      | 2014-07-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029256941> |
| ORDONNANCE       | 2014-806      | 2014-07-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029256904> |
| LOI              | 2014-856      | 2014-07-31          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029313296> |
| LOI              | 2014-873      | 2014-08-04          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029330832> |
| LOI              | 2014-891      | 2014-08-08          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029349482> |
| LOI              | 2014-1170     | 2014-10-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029573022> |
| ORDONNANCE       | 2014-1543     | 2014-12-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029925718> |
| LOI              | 2014-1545     | 2014-12-20          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029926655> |
| ORDONNANCE       | 2015-25       | 2015-01-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030098110> |
| ORDONNANCE       | 2015-24       | 2015-01-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030097831> |
| LOI              | 2015-177      | 2015-02-16          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030248562> |
| LOI              | 2015-366      | 2015-03-31          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030423022> |
| LOI              | 2015-737      | 2015-06-25          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030784348> |
| LOI              | 2015-990      | 2015-08-06          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030978561> |
| LOI              | 2015-991      | 2015-08-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030985460> |
| LOI              | 2015-992      | 2015-08-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000031044385> |
| LOI              | 2015-994      | 2015-08-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000031046061> |
| LOI              | 2015-1541     | 2015-11-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000031535624> |
| LOI              | 2015-1785     | 2015-12-29          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000031732865> |
| LOI              | 2016-41       | 2016-01-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000031912641> |
| LOI              | 2016-138      | 2016-02-11          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032036289> |
| LOI              | 2016-297      | 2016-03-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032205234> |
| LOI              | 2016-444      | 2016-04-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032396046> |
| LOI              | 2016-457      | 2016-04-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032401821> |
| LOI              | 2016-483      | 2016-04-20          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032433852> |
| DECISION         | 390956        | 2016-06-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032673436> |
| LOI              | 2016-925      | 2016-07-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032854341> |
| LOI              | 2016-1088     | 2016-08-08          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032983213> |
| LOI              | 2016-1321     | 2016-10-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033202746> |
| ORDONNANCE       | 2016-1519     | 2016-11-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033367836> |
| ORDONNANCE       | 2016-1562     | 2016-11-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033440998> |
| LOI              | 2016-1691     | 2016-12-09          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033558528> |
| ORDONNANCE       | 2016-1809     | 2016-12-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033670708> |
| LOI              | 2016-1828     | 2016-12-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033680801> |
| LOI              | 2016-1888     | 2016-12-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033717812> |
| ORDONNANCE       | 2017-31       | 2017-01-12          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033860852> |
| ORDONNANCE       | 2017-50       | 2017-01-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033893429> |
| LOI              | 2017-86       | 2017-01-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033934948> |
| LOI              | 2017-256      | 2017-02-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000034103762> |
| LOI              | 2017-257      | 2017-02-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000034103927> |
| LOI              | 2017-261      | 2017-03-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000034111794> |
| DECISION         | 395506        | 2017-03-31          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000034391052> |
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
| LOI              | 2018-771      | 2018-09-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037367660> |
| LOI              | 2018-778      | 2018-09-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037381808> |
| LOI              | 2018-938      | 2018-10-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037547946> |
| ORDONNANCE       | 2018-1125     | 2018-12-12          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037800506> |
| LOI              | 2018-1202     | 2018-12-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037847559> |
| LOI              | 2018-1203     | 2018-12-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037847585> |
| LOI              | 2018-1317     | 2018-12-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037882341> |
| LOI              | 2019-222      | 2019-03-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038261631> |
| LOI              | 2019-774      | 2019-07-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038821260> |
| LOI              | 2019-791      | 2019-07-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038829065> |
| LOI              | 2019-828      | 2019-08-06          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038889182> |
| ORDONNANCE       | 2019-861      | 2019-08-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038940323> |
| LOI              | 2019-1461     | 2019-12-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039681877> |
| LOI              | 2019-1479     | 2019-12-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039683923> |
| ORDONNANCE       | 2020-71       | 2020-01-29          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000041506557> |
| LOI              | 2020-105      | 2020-02-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000041553759> |
| DECISION         | 2020-834 QPC  | 2020-04-03          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000041782007> |
| LOI              | 2020-760      | 2020-06-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042025624> |
| LOI              | 2020-766      | 2020-06-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042031970> |
| LOI              | 2020-840      | 2020-07-03          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042079128> |
| ORDONNANCE       | 2020-1256     | 2020-10-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042424239> |
| LOI              | 2020-1525     | 2020-12-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042619877> |
| ORDONNANCE       | 2020-1733     | 2020-12-16          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042754770> |
| LOI              | 2020-1674     | 2020-12-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042738027> |
| LOI              | 2021-502      | 2021-04-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043421566> |
| ORDONNANCE       | 2021-552      | 2021-05-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043477594> |
| ORDONNANCE       | 2021-611      | 2021-05-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043511942> |
| LOI              | 2021-641      | 2021-05-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043524722> |
| LOI              | 2021-695      | 2021-06-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043575111> |
| ORDONNANCE       | 2021-702      | 2021-06-02          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043590607> |
| LOI              | 2021-875      | 2021-07-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043741543> |
| LOI              | 2021-874      | 2021-07-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043741537> |
| DECISION         | 2021-823 DC   | 2021-08-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043964902> |
| LOI              | 2021-1104     | 2021-08-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043956924> |
| LOI              | 2021-1109     | 2021-08-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043964778> |
| LOI              | 2021-1485     | 2021-11-15          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044327272> |
| ORDONNANCE       | 2021-1574     | 2021-11-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044411525> |
| LOI              | 2021-1539     | 2021-11-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044387560> |
| LOI              | 2021-1678     | 2021-12-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044513764> |
| LOI              | 2021-1716     | 2021-12-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044537507> |
| ORDONNANCE       | 2021-1747     | 2021-12-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044547312> |
| LOI              | 2021-1754     | 2021-12-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044553428> |
| LOI              | 2021-1774     | 2021-12-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044559192> |
| LOI              | 2022-52       | 2022-01-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045067923> |
| LOI              | 2022-217      | 2022-02-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045197395> |
| LOI              | 2022-272      | 2022-02-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045268755> |
| LOI              | 2022-296      | 2022-03-02          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045287568> |
| LOI              | 2022-299      | 2022-03-02          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045287658> |
| ORDONNANCE       | 2022-408      | 2022-03-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045398055> |
| ORDONNANCE       | 2022-583      | 2022-04-20          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045614880> |
| ORDONNANCE       | 2022-1521     | 2022-12-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046694513> |
| LOI              | 2022-1574     | 2022-12-16          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046751169> |
| LOI              | 2022-1598     | 2022-12-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046771781> |
| LOI              | 2022-1616     | 2022-12-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046791754> |
| LOI              | 2022-1726     | 2022-12-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046845631> |
| ORDONNANCE       | 2023-15       | 2023-01-18          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047007968> |
| LOI              | 2023-29       | 2023-01-25          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047055162> |
| LOI              | 2023-380      | 2023-05-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047561974> |
| LOI              | 2023-451      | 2023-06-09          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047663185> |
| LOI              | 2023-479      | 2023-06-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047709059> |
| LOI              | 2023-580      | 2023-07-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047805414> |
| LOI              | 2023-610      | 2023-07-18          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047858021> |
| LOI              | 2023-703      | 2023-08-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047914986> |

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
| LOI              | 2003-339      | 2003-04-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000238536> |
| LOI              | 2003-400      | 2003-04-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000602740> |
| LOI              | 2003-708      | 2003-08-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000240077> |
| ORDONNANCE       | 2003-1212     | 2003-12-18          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000429994> |
| LOI              | 2003-1311     | 2003-12-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000612133> |
| LOI              | 2004-1        | 2004-01-02          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000431282> |
| LOI              | 2004-228      | 2004-03-15          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000417977> |
| LOI              | 2004-391      | 2004-05-04          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000613810> |
| ORDONNANCE       | 2004-545      | 2004-06-11          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000617671> |
| ORDONNANCE       | 2004-637      | 2004-07-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000803875> |
| ORDONNANCE       | 2004-631      | 2004-07-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000803481> |
| LOI              | 2004-806      | 2004-08-09          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000787078> |
| LOI              | 2004-805      | 2004-08-09          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000237105> |
| LOI              | 2004-809      | 2004-08-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000804607> |
| LOI              | 2004-811      | 2004-08-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000804612> |
| LOI              | 2004-810      | 2004-08-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000625158> |
| ORDONNANCE       | 2004-1174     | 2004-11-04          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000237213> |
| LOI              | 2004-1343     | 2004-12-09          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000256180> |
| LOI              | 2004-1484     | 2004-12-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000789373> |
| LOI              | 2005-5        | 2005-01-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000624676> |
| LOI              | 2005-32       | 2005-01-18          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000806166> |
| LOI              | 2005-102      | 2005-02-11          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000809647> |
| LOI              | 2005-157      | 2005-02-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000257340> |
| LOI              | 2005-380      | 2005-04-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000259787> |
| ORDONNANCE       | 2005-406      | 2005-05-02          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000606537> |
| ORDONNANCE       | 2005-461      | 2005-05-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000629800> |
| LOI              | 2005-841      | 2005-07-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000632799> |
| LOI              | 2005-1720     | 2005-12-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000813882> |
| LOI              | 2006-10       | 2006-01-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000456019> |
| ORDONNANCE       | 2006-172      | 2006-02-15          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000264872> |
| LOI              | 2006-340      | 2006-03-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000816849> |
| LOI              | 2006-396      | 2006-03-31          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000268539> |
| LOI              | 2006-450      | 2006-04-18          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000426953> |
| ORDONNANCE       | 2006-460      | 2006-04-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000456141> |
| ORDONNANCE       | 2006-596      | 2006-05-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000792831> |
| LOI              | 2006-586      | 2006-05-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000607509> |
| LOI              | 2006-636      | 2006-06-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000608993> |
| LOI              | 2007-148      | 2007-02-02          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000465739> |
| LOI              | 2007-209      | 2007-02-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000644388> |
| LOI              | 2007-297      | 2007-03-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000615568> |
| LOI              | 2007-293      | 2007-03-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000823100> |
| ORDONNANCE       | 2007-329      | 2007-03-12          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000465978> |
| LOI              | 2007-1199     | 2007-08-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000824315> |
| LOI              | 2007-1786     | 2007-12-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000017726554> |
| ORDONNANCE       | 2007-1801     | 2007-12-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000017733142> |
| LOI              | 2007-1822     | 2007-12-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000017853368> |
| LOI              | 2007-1824     | 2007-12-25          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000017839505> |
| LOI              | 2008-112      | 2008-02-08          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000018088910> |
| LOI              | 2008-126      | 2008-02-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000018117826> |
| ORDONNANCE       | 2008-507      | 2008-05-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000018885189> |
| ORDONNANCE       | 2008-728      | 2008-07-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000019243177> |
| ORDONNANCE       | 2008-727      | 2008-07-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000019243132> |
| LOI              | 2008-776      | 2008-08-04          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000019283050> |
| ORDONNANCE       | 2008-1304     | 2008-12-11          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000019907126> |
| LOI              | 2008-1425     | 2008-12-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000019995721> |
| LOI              | 2008-1443     | 2008-12-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000020014790> |
| ORDONNANCE       | 2009-79       | 2009-01-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000020137892> |
| LOI              | 2009-526      | 2009-05-12          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000020604162> |
| ORDONNANCE       | 2009-537      | 2009-05-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000020612883> |
| ORDONNANCE       | 2009-664      | 2009-06-11          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000020728509> |
| LOI              | 2009-669      | 2009-06-12          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000020735432> |
| LOI              | 2009-833      | 2009-07-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000020828203> |
| LOI              | 2009-879      | 2009-07-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000020879475> |
| LOI              | 2009-972      | 2009-08-03          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000020954520> |
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
| LOI              | 2010-500      | 2010-05-18          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022227311> |
| LOI              | 2010-597      | 2010-06-03          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022308227> |
| ORDONNANCE       | 2010-638      | 2010-06-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022330885> |
| LOI_ORGANIQUE    | 2010-704      | 2010-06-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022402454> |
| LOI              | 2010-751      | 2010-07-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022436528> |
| LOI              | 2010-769      | 2010-07-09          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022454032> |
| LOI              | 2010-788      | 2010-07-12          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022470434> |
| LOI              | 2010-853      | 2010-07-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022511227> |
| LOI              | 2010-874      | 2010-07-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022521587> |
| LOI              | 2010-1127     | 2010-09-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022862522> |
| ORDONNANCE       | 2010-1307     | 2010-10-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000022990793> |
| LOI              | 2010-1330     | 2010-11-09          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023022127> |
| LOI              | 2010-1487     | 2010-12-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023174577> |
| LOI              | 2010-1536     | 2010-12-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023229524> |
| LOI              | 2010-1594     | 2010-12-20          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023261006> |
| LOI              | 2010-1657     | 2010-12-29          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023314376> |
| LOI              | 2011-267      | 2011-03-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023707312> |
| LOI              | 2011-302      | 2011-03-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023751262> |
| LOI              | 2011-334      | 2011-03-29          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000023781252> |
| LOI              | 2011-525      | 2011-05-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000024021430> |
| LOI              | 2011-893      | 2011-07-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000024408887> |
| LOI              | 2011-940      | 2011-08-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000024457033> |
| LOI              | 2011-1977     | 2011-12-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000025044460> |
| LOI              | 2012-158      | 2012-02-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000025269948> |
| LOI              | 2012-300      | 2012-03-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000025441587> |
| ORDONNANCE       | 2012-351      | 2012-03-12          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000025498645> |
| LOI              | 2012-347      | 2012-03-12          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000025489865> |
| LOI              | 2012-409      | 2012-03-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000025582235> |
| LOI              | 2012-1404     | 2012-12-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000026785322> |
| DECISION         | 354947        | 2012-12-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000026856692> |
| LOI              | 2013-108      | 2013-01-31          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027012750> |
| LOI              | 2013-403      | 2013-05-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027414225> |
| LOI              | 2013-595      | 2013-07-08          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027677984> |
| LOI              | 2013-660      | 2013-07-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027735009> |
| LOI              | 2013-659      | 2013-07-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027734839> |
| LOI              | 2013-1278     | 2013-12-29          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000028399511> |
| LOI              | 2014-58       | 2014-01-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000028526298> |
| LOI              | 2014-173      | 2014-02-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000028636804> |
| LOI              | 2014-288      | 2014-03-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000028683576> |
| ORDONNANCE       | 2014-693      | 2014-06-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029139960> |
| ORDONNANCE       | 2014-691      | 2014-06-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029139765> |
| ORDONNANCE       | 2014-692      | 2014-06-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029145752> |
| LOI              | 2014-788      | 2014-07-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029223331> |
| DECISION         | 372835        | 2014-07-16          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029279331> |
| ORDONNANCE       | 2014-807      | 2014-07-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029256941> |
| ORDONNANCE       | 2014-806      | 2014-07-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029256904> |
| LOI              | 2014-856      | 2014-07-31          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029313296> |
| LOI              | 2014-873      | 2014-08-04          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029330832> |
| LOI              | 2014-891      | 2014-08-08          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029349482> |
| LOI              | 2014-1170     | 2014-10-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029573022> |
| ORDONNANCE       | 2014-1543     | 2014-12-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029925718> |
| LOI              | 2014-1545     | 2014-12-20          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000029926655> |
| ORDONNANCE       | 2015-25       | 2015-01-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030098110> |
| ORDONNANCE       | 2015-24       | 2015-01-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030097831> |
| LOI              | 2015-177      | 2015-02-16          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030248562> |
| LOI              | 2015-366      | 2015-03-31          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030423022> |
| LOI              | 2015-737      | 2015-06-25          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030784348> |
| LOI              | 2015-990      | 2015-08-06          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030978561> |
| LOI              | 2015-991      | 2015-08-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000030985460> |
| LOI              | 2015-992      | 2015-08-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000031044385> |
| LOI              | 2015-994      | 2015-08-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000031046061> |
| LOI              | 2015-1541     | 2015-11-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000031535624> |
| LOI              | 2015-1785     | 2015-12-29          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000031732865> |
| LOI              | 2016-41       | 2016-01-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000031912641> |
| LOI              | 2016-138      | 2016-02-11          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032036289> |
| LOI              | 2016-297      | 2016-03-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032205234> |
| LOI              | 2016-444      | 2016-04-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032396046> |
| LOI              | 2016-457      | 2016-04-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032401821> |
| LOI              | 2016-483      | 2016-04-20          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032433852> |
| DECISION         | 390956        | 2016-06-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032673436> |
| LOI              | 2016-925      | 2016-07-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032854341> |
| LOI              | 2016-1088     | 2016-08-08          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032983213> |
| LOI              | 2016-1321     | 2016-10-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033202746> |
| ORDONNANCE       | 2016-1519     | 2016-11-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033367836> |
| ORDONNANCE       | 2016-1562     | 2016-11-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033440998> |
| LOI              | 2016-1691     | 2016-12-09          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033558528> |
| ORDONNANCE       | 2016-1809     | 2016-12-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033670708> |
| LOI              | 2016-1828     | 2016-12-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033680801> |
| LOI              | 2016-1888     | 2016-12-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033717812> |
| ORDONNANCE       | 2017-31       | 2017-01-12          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033860852> |
| ORDONNANCE       | 2017-50       | 2017-01-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033893429> |
| LOI              | 2017-86       | 2017-01-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000033934948> |
| LOI              | 2017-256      | 2017-02-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000034103762> |
| LOI              | 2017-257      | 2017-02-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000034103927> |
| LOI              | 2017-261      | 2017-03-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000034111794> |
| DECISION         | 395506        | 2017-03-31          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000034391052> |
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
| LOI              | 2018-771      | 2018-09-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037367660> |
| LOI              | 2018-778      | 2018-09-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037381808> |
| LOI              | 2018-938      | 2018-10-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037547946> |
| ORDONNANCE       | 2018-1125     | 2018-12-12          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037800506> |
| LOI              | 2018-1202     | 2018-12-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037847559> |
| LOI              | 2018-1203     | 2018-12-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037847585> |
| LOI              | 2018-1317     | 2018-12-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037882341> |
| LOI              | 2019-222      | 2019-03-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038261631> |
| LOI              | 2019-774      | 2019-07-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038821260> |
| LOI              | 2019-791      | 2019-07-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038829065> |
| LOI              | 2019-828      | 2019-08-06          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038889182> |
| ORDONNANCE       | 2019-861      | 2019-08-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038940323> |
| LOI              | 2019-1461     | 2019-12-27          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039681877> |
| LOI              | 2019-1479     | 2019-12-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039683923> |
| ORDONNANCE       | 2020-71       | 2020-01-29          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000041506557> |
| LOI              | 2020-105      | 2020-02-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000041553759> |
| DECISION         | 2020-834 QPC  | 2020-04-03          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000041782007> |
| LOI              | 2020-760      | 2020-06-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042025624> |
| LOI              | 2020-766      | 2020-06-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042031970> |
| LOI              | 2020-840      | 2020-07-03          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042079128> |
| ORDONNANCE       | 2020-1256     | 2020-10-14          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042424239> |
| LOI              | 2020-1525     | 2020-12-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042619877> |
| ORDONNANCE       | 2020-1733     | 2020-12-16          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042754770> |
| LOI              | 2020-1674     | 2020-12-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000042738027> |
| LOI              | 2021-502      | 2021-04-26          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043421566> |
| ORDONNANCE       | 2021-552      | 2021-05-05          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043477594> |
| ORDONNANCE       | 2021-611      | 2021-05-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043511942> |
| LOI              | 2021-641      | 2021-05-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043524722> |
| LOI              | 2021-695      | 2021-06-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043575111> |
| ORDONNANCE       | 2021-702      | 2021-06-02          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043590607> |
| LOI              | 2021-875      | 2021-07-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043741543> |
| LOI              | 2021-874      | 2021-07-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043741537> |
| DECISION         | 2021-823 DC   | 2021-08-13          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043964902> |
| LOI              | 2021-1104     | 2021-08-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043956924> |
| LOI              | 2021-1109     | 2021-08-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000043964778> |
| LOI              | 2021-1485     | 2021-11-15          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044327272> |
| ORDONNANCE       | 2021-1574     | 2021-11-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044411525> |
| LOI              | 2021-1539     | 2021-11-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044387560> |
| LOI              | 2021-1678     | 2021-12-17          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044513764> |
| LOI              | 2021-1716     | 2021-12-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044537507> |
| ORDONNANCE       | 2021-1747     | 2021-12-22          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044547312> |
| LOI              | 2021-1754     | 2021-12-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044553428> |
| LOI              | 2021-1774     | 2021-12-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000044559192> |
| LOI              | 2022-52       | 2022-01-24          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045067923> |
| LOI              | 2022-217      | 2022-02-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045197395> |
| LOI              | 2022-272      | 2022-02-28          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045268755> |
| LOI              | 2022-296      | 2022-03-02          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045287568> |
| LOI              | 2022-299      | 2022-03-02          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045287658> |
| ORDONNANCE       | 2022-408      | 2022-03-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045398055> |
| ORDONNANCE       | 2022-583      | 2022-04-20          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000045614880> |
| ORDONNANCE       | 2022-1521     | 2022-12-07          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046694513> |
| LOI              | 2022-1574     | 2022-12-16          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046751169> |
| LOI              | 2022-1598     | 2022-12-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046771781> |
| LOI              | 2022-1616     | 2022-12-23          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046791754> |
| LOI              | 2022-1726     | 2022-12-30          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046845631> |
| ORDONNANCE       | 2023-15       | 2023-01-18          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047007968> |
| LOI              | 2023-29       | 2023-01-25          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047055162> |
| LOI              | 2023-380      | 2023-05-19          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047561974> |
| LOI              | 2023-451      | 2023-06-09          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047663185> |
| LOI              | 2023-479      | 2023-06-21          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047709059> |
| LOI              | 2023-580      | 2023-07-10          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047805414> |
| LOI              | 2023-610      | 2023-07-18          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047858021> |
| LOI              | 2023-703      | 2023-08-01          | <https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047914986> |

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
