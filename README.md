# RMSMonitor
Simple desktop app to check the status of one or more RMS meteor cameras

## Installation
### Windows
* Download the zip file from [here](https://github.com/markmac99/RMSMonitor/releases) and unpack it into a folder of your choosing. 
* Edit the sample ini file to contain a comma-separated list of the stations you want to monitor, then save it as "rmsconfig.ini" with quotemarks around the name (he quotemarks are essential to prevent windows secretly renaming the file with a .txt or .sample extension).
* Create a desktop shortcut pointing to checkStatus.exe.

### Linux and MacOS
You will need Python 3.7 or later installed. Python 2.x is not supported. 

* Create a folder RMSMonitor in your home directory. 
* Download the tgz file from [here](https://github.com/markmac99/RMSMonitor/releases) and unpack it into this folder. 
* Rename the sample config file to rmsmonitor.ini, and edit it to contain a comma-separated list of the stations you want to monitor.
* Open a terminal window and run the install script:
``` bash
$HOME/RMSMonitor/install.sh
```
* This should create a desktop icon from which you can run the tool. 
