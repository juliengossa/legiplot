#!/bin/bash

python3 archeolex_excavation/archeolex_excavation.py diff `cat $1` -t -s3 -f data/lp_diffstats_ts3.csv -i data/lp_diff_t.csv
python3 archeolex_excavation/archeolex_excavation.py stats `cat $1` -t -s1 -d last -f data/lp_stats_lts1.csv

dates="1000-01-01 1959-06-01 1965-06-01 1969-06-01 1974-06-01 1981-06-01 1988-06-01 1995-06-01 2002-06-01 2007-06-01 2012-06-01 2017-06-01 2022-06-01"
python3 archeolex_excavation/archeolex_excavation.py diff `cat $1` -t -s5 -f data/lp_diffstats_jts5.csv -i data/lp_diff_jt.csv -j -d $dates

tar -cvzf lp_data.tar.gz data/*
