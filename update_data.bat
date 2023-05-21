chcp 65001

set codes=code_civil code_de_commerce code_de_justice_administrative code_de_l'action_sociale_et_des_familles code_de_l'aviation_civile code_de_l'éducation code_de_l'entrée_et_du_séjour_des_étrangers_et_du_droit_d'asile code_de_l'environnement code_de_l'urbanisme code_de_l'organisation_judiciaire code_de_l'énergie code_de_la_consommation code_de_la_construction_et_de_l'habitation code_de_la_propriété_intellectuelle code_de_la_recherche code_de_la_route code_de_la_santé_publique code_de_la_sécurité_intérieure code_de_la_sécurité_sociale code_de_procédure_civile code_de_procédure_pénale code_des_assurances code_des_juridictions_financières code_des_postes_et_des_communications_électroniques code_des_transports code_du_cinéma_et_de_l'image_animée code_du_patrimoine code_du_sport code_du_tourisme code_du_travail code_forestier_(nouveau) code_général_de_la_propriété_des_personnes_publiques code_général_des_collectivités_territoriales code_pénal code_électoral

python archeolex_excavation/archeolex_excavation.py diff %codes% -t -s3 -f data/lp_diffstats_ts3.csv -i data/lp_diff_t.csv
python archeolex_excavation/archeolex_excavation.py stats %codes% -t -s1 -d last -f data/lp_stats_lts1.csv

set dates=1000-01-01 1959-06-01 1965-06-01 1969-06-01 1974-06-01 1981-06-01 1988-06-01 1995-06-01 2002-06-01 2007-06-01 2012-06-01 2017-06-01 2022-06-01
python archeolex_excavation/archeolex_excavation.py diff %codes% -t -s5 -f data/lp_diffstats_jts5.csv -i data/lp_diff_jt.csv -j -d %dates%

tar -cvzf lp_data.tar.gz data/*
