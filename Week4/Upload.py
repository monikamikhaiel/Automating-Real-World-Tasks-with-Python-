#!/usr/bin/env python3
import requests
from glob import glob
url="http://35.223.103.171/upload/"
for file in glob("/home/student-03-12c3477e10e7/supplier-data/images/*.jpeg"):
  print(file)
  with open(file,"rb") as im :
    r=requests.post(url,files={'file':im})

