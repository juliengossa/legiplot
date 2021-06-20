#!/bin/bash

#python3 archeolex_excavation.py diff `cat $1` -t -f lp_diff_t.csv
python3 archeolex_excavation.py stats `cat $1` -t -s3 -f lp_stats_ts3.csv
python3 archeolex_excavation.py stats `cat $1` -t -s1 -d last -f lp_stats_lts1.csv
