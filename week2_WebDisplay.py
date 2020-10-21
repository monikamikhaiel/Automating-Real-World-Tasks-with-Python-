#!/usr/bin/env python3
import requests
import os
list=[]
dict={}
files=os.listdir("/data/feedback")
#print(files)
for file in files:
  f=open("/data/feedback/"+file)
  dict["title"]=f.readline().strip()
  dict["name"]=f.readline().strip()
  dict["date"]=f.readline().strip()
  dict["feedback"]=f.read().strip()
  f.close()
  list.append(dict)
  dict={}
#print(list)
for i in range(len(list)):
  response=requests.post("http://34.72.12.7/feedback",json=list[i])
  print(response.request.body)
  print(response.status_code)

