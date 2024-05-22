# RMSMonitor
Simple desktop app to check the status of one or more RMS meteor cameras

## Installation
### Windows
* Download the zip file and unpack it into a folder of your choosing. 
* Rename the sample config file to rmsmonitor.ini, and edit it to contain a comma-separated list of the stations you want to monitor.
* Create a desktop shortcut pointing to checkStatus.exe.

### Linux and MacOS
Note: you will need Python 3.7 or later installed.
* Create a folder RMSMonitor in your home directory. 
* Download the tar file and unpack it into this folder. 
* Rename the sample config file to rmsmonitor.ini, and edit it to contain a comma-separated list of the stations you want to monitor.
* Open a terminal window, and install the Requests library by typing "pip3 install -r RMSMonitor/requirements.txt"
* Copy the .desktop file to the Desktop folder in your home directory. 
* Edit the .desktop file so that the Exec line points to the location of checkStatus.py
* This should create a desktop icon from which you can run the tool. 
