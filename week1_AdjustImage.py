#!/usr/bin/env python3
from PIL import Image
import os
from glob import glob
#OldImages=os.listdir() # a list of all images names
for i in glob("*.tiff"):
  im=Image.open(i).convert("RGB")
  im.resize((128,128)).rotate(90)
  im.save("/opt/icons/"+i[:len(i)-1-4]+"jpeg")
