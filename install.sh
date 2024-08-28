#!/bin/bash
sudo apt install python3-virtualenv
virtualenv ~/venvs/vRMSMonitor
source ~/venvs/vRMSMonitor/bin/activate
pip3 install -r RMSMonitor/requirements.txt
cp RMSMonitor/RMSMonitor.desktop $HOME/Desktop
