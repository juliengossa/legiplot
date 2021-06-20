#!/bin/bash

cd archeolex_excavation
python3 archeolex_excavation.py diff `cat $1` -t -f ../data/lp_diff_t.csv
python3 archeolex_excavation.py stats `cat $1` -t -s3 -f ../data/lp_stats_ts3.csv
python3 archeolex_excavation.py stats `cat $1` -t -s1 -d last -f ../data/lp_stats_lts1.csv

cd ..
tar -cvzf lp_data.tar.gz data/*
