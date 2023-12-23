# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:59:31 2023

@author: leon
"""
#import argparse
import json
import os.path
import sys

filename="\\jupyter\\tcmc.json"
newfolder="c:\\church"
fileoutname=os.path.join(newfolder,os.path.basename(filename))
lenth=3

#------ if remark follow block, cancel cmd input
lenth=len(sys.argv)
  
if lenth==1:
    print("Usage: obs-scene scenecolletionfile destfolder if no dest ,display only")
    exit(0)
if lenth>1:
    filename=sys.argv[1]
    print("from: ",filename)
if lenth>2:
    newfolder=sys.argv[2]
    print("dest folder: ", newfolder)
    fileoutname=os.path.join(newfolder,os.path.basename(filename))
    if(lenth>3):
        fileoutname=sys.argv[3]
    print("save at: ",fileoutname)
#--------

    
with open(filename, encoding='utf-8') as complex_data:
    data = complex_data.read()
    z = json.loads(data)

sr=z['sources']

for x in sr:
  if 'settings' in x:
    if 'local_file' in (x['settings']):
        name=x['settings']['local_file']
        file_name=os.path.basename(name)
        file_folder=os.path.dirname(name)
        print(file_folder,file_name)
        namea=os.path.join(newfolder, file_name)
        x['settings']['local_file']=namea

if lenth>2:
    with open(fileoutname, "w") as write_file:
        json.dump(z, write_file)

