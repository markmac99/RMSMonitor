#!/bin/bash
sudo apt install python3-virtualenv python3-tk
virtualenv $HOME/venvs/vRMSMonitor
source $HOME/venvs/vRMSMonitor/bin/activate
pip3 install -r $HOME/RMSMonitor/requirements.txt
cp $HOME/RMSMonitor/RMSMonitor.desktop $HOME/Desktop
chmod +x $HOME/Desktop/RMSMonitor.desktop

