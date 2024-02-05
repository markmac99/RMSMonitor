#!/bin/bash

# script to build the deployment packages

cp LICENSE README.md rmsmonitor.ini.sample dist/checkStatus/
cd dist/checkStatus
zip -r test.zip *
mv test.zip ../..
cd ../..
zip -u test.zip LICENSE README.md *.sample
tar cvf test.tar checkStatus.py LICENSE README.md *.sample *.desktop requirements.txt
