#!/usr/bin/env python3
import requests
#import os
from glob import glob
list=[]
dict={}
for file in glob("*.txt"):
  f=open(file)
  dict["title"]=file.readline()
  dict["name"]=file.readline()
  dict["date"]=file.readline()
  dict["feedback"]=file.read()
  f.close()
  list.append(dict)
  dict={}
response=requests.post(,data=list)
print(response.status_code)
