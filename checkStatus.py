#!/bin/env python3
# Copyright Mark McIntyre, 2024-
#

import requests
import datetime
import sys
import os
import configparser
from tkinter import ttk
import tkinter as tk


def readConfigFile(cfgfile):
    cfg = configparser.ConfigParser()
    cfg.read(cfgfile)
    camlist = cfg['settings']['cameras'].split(',')
    return camlist


def getURL(camid):
    baseurl = f'https://globalmeteornetwork.org/weblog/{camid[0:2]}/{camid}/latest/index.html'
    r = requests.get(baseurl)
    if r.status_code != 200:
        if r.status_code == 404:
            print(f'data for {camid} not available')
        else:
            print(f'error: {r.status_code}')
        return None
    text = r.text
    rb=text.find('Recording begin: ')
    if rb < 50:
        print(f'data for {camid} not available')
        return None
    rb = rb + len('Recording begin: ')
    lastdt = text[rb:rb+19]
    try:
        dtval = datetime.datetime.strptime(lastdt, '%Y-%m-%d %H:%M:%S')
    except:
        dtval = None
    #print(f'{camid} last updated at {dtval} UT')
    return dtval


if __name__ == '__main__':
    if len(sys.argv) > 1:
        cfgfile = sys.argv[1]
    else:
        cfgfile = 'rmsmonitor.ini'
    if not os.path.isfile(cfgfile):
        print(f'config file {cfgfile} missing')
        sys.exit(1)
    camids = readConfigFile(cfgfile)
    camstati = []
    for camid in camids:
        camid = camid.strip().upper()
        dtval = getURL(camid)
        camstati.append([camid, dtval])

    root = tk.Tk()
    root.title("Camera Status")
    # workaround for ttk bug on Python 3.7
    style = ttk.Style()
    actualTheme = style.theme_use()
    style.theme_create("dummy", parent=actualTheme)
    style.theme_use("dummy")
    # create window and table
    root.geometry('400x150')
    tree = ttk.Treeview(root, column=("c1", "c2"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Cam ID")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Last Update")
    # set colour tags
    tree.tag_configure('warning',foreground='white', background='yellow')
    tree.tag_configure('alert',foreground='white', background='red')
    tree.tag_configure('normal',foreground='black', background='green')
    # get data
    nowdt = datetime.datetime.now()
    for rw in camstati:
        if rw[1] is None or rw[1] == 'None':
            tags='error'
        else:
            age = nowdt - rw[1]
            #print(age)
            tags='normal'
            if age > datetime.timedelta(days=3):
                tags = 'warning'
            if age > datetime.timedelta(days=7):
                tags = 'alert'
               
        tree.insert('', tk.END, values=rw, tags=(tags))
    # display the matrix
    tree.pack()
    root.mainloop()
