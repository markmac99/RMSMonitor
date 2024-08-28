pyinstaller .\checkStatus.py --noconsole --clean --windowed 
copy-item license dist\checkStatus
copy-item rmsmonitor.ini.sample dist\checkStatus
Set-Location dist
compress-archive -path .\checkStatus\ -destinationpath ..\rmsMonitor.zip -update
Set-Location ..
bash -c "tar cvzf rmsMonitor.tgz *.sh checkStatus.py LICENSE README.md *.sample *.desktop requirements.txt"
