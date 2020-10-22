#!/usr/bin/env python3
import requests
import os
def RetList():
  list=[]
  dict={}
#os.chdir("/home/student-04-f1e532499100/supplier-data/d")
  files=os.listdir("/home/student-04-f1e532499100/supplier-data/descriptions")
#print(files)
  for file in files:
    f=open("/home/student-04-f1e532499100/supplier-data/descriptions/"+file)
    dict["name"]=f.readline().strip()
    dict["weight"]=int(f.readline().strip().split()[0])
    dict["description"]=f.read().strip()
    f.close()
 # with open("/home/student-04-f1e532499100/supplier-data/images/"+file[:len(file)-1-3]+".jpeg","rb") as im :
    dict["image_name"]=file[:len(file)-1-3]+".jpeg"
    list.append(dict)
    dict={}
  return list
#print(list)
if __name__=="__main__":
  list=RetList()
  for i in range(len(list)):
    response=requests.post("http://34.68.255.223/fruits/",json=list[i])
    print(response.request.body)
    print(response.status_code)
# the images has been uploaded beforre we just need the associated name 
