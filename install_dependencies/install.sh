#!/usr/bin/bash
sudo apt install python3-venv
python3 -m venv env
source env/bin/activate
pip install -r install_dependencies/requirements.txt
export PYTHONPATH=$PWD:$PYTHONPATH
