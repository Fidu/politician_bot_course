#! /bin/bash

function venv(){
    virtualenv -p python3.6 venv
    source venv/bin/activate
    pip install -r requirements.txt
}

function run(){
    source venv/bin/activate
    python my_first_bot.py
}

$@
