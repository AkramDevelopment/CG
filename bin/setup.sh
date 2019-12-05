#!/bin/bash

# create and use environment
virtualenv .venv 
source .venv/bin/activate

pip3 install flask sqlalchemy
