#!/usr/bin/env python3
from PIL import Image
import os
from glob import glob
os.chdir("/home/student-03-12c3477e10e7/supplier-data/images/")
#OldImages=os.listdir() # a list of all images names
for i in glob("*.tiff"):
  im=Image.open(i).convert("RGB")
  im.resize((600,400)).save(i[:len(i)-1-4]+".jpeg")


  
