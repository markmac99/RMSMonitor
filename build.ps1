pyinstaller .\checkStatus.py --noconsole --clean --windowed 
copy-item license dist\checkStatus
copy-item rmsmonitor.ini.sample dist\checkStatus
Set-Location dist
compress-archive -path .\checkStatus\ -destinationpath c:\temp\rmsMonitor.zip -update
Set-Location ..

