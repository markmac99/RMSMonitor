# Copyright Mark McIntyre, 2024-
#

import requests
import os
import sys
import configparser as cfg 


def getURL(camid):
    baseurl = f'https://globalmeteornetwork.org/weblog/{camid[0:2]}/{camid}/latest/index.html'
    r = requests.get(baseurl)
    if r.status_code != 200:
        print(f'error: {r.status_code}')
        return False
    text = r.text
    rb=text.find('Recording begin: ')
    if rb < 50:
        print('data unavailable')
        return False
    rb = rb + len('Recording begin: ')
    lastdt = text[rb:rb+19]
    print(f'{camid} last updated at {lastdt}')
    return lastdt


if __name__ == '__main__':
    if len(sys.argv) > 1:
        camid = sys.argv[1]
    else:
        camid = 'UK0006'
    getURL(camid)
