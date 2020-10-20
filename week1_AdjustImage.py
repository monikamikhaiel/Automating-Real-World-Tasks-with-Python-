#!/usr/bin/env python3
from PIL import Image
import os
OldImages=os.listdir() # a list of all images names
#NewImages=[ "/opt/icons/"+i for i in OldImages ]
#print(NewImages)
for i in range(len(OldImages)):
  im=Image.open(OldImages[i])
  im.resize((128,128)).rotate(90)
  im.save("/home/student-00-6d8122963d8f/opt/icons/"+OldImages[i])
