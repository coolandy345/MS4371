import glob
import os
import json

def scan_temp_profile():
    list=glob.glob("user/profiles/temperature profile/*.json")
    liste=[]
    for item in list:
        liste.append(os.path.splitext(os.path.basename(item))[0])
    return liste

def scan_test_profile():
    list=glob.glob("user/profiles/test profile/*.json")
    liste=[]
    for item in list:
        liste.append(os.path.splitext(os.path.basename(item))[0])
    return liste

