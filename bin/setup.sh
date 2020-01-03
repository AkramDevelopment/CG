#!/bin/bash

# create and use environment
virtualenv .venv 
source .venv/bin/activate

REQS='requirements.txt'

while read dep; do 
    dep=$(echo "$dep" | tr -d '\n')
    pip3 install "$dep"
done < $REQS
