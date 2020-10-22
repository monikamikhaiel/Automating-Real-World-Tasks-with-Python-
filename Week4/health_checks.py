#!/usr/bin/env python3
import psutil
import shutil
import socket
import time
import emails

def cpu_usage():
  if(psutil.cpu_percent() >= 80):
    return "Error - CPU usage is over 80%"
  else :
    return ""
def disk_usage():
  _,_,_,percent=psutil.disk_usage('/')
  if percent < 20:
    return "Error - Available disk space is less than 20%"
  else :
    return ""

def mem_usage():
 # p = psutil.Process()
  available=psutil.virtual_memory()._asdict()["available"]
  if available < (500*10^6):
    return "Error - Available memory is less than 500MB"
  else :
    return ""

def net_conn():
  try:
    host=socket.gethostname()
    return ""
  except :
    return "Error - localhost cannot be resolved to 127.0.0.1"
if __name__=="__main__":
  starttime = time.time()
  #while True:
  err=" ".join([cpu_usage(),disk_usage(),mem_usage(),net_conn()])
  print(cpu_usage())
# time.sleep(60.0 - ((time.time() - starttime) % 60.0))
        ## email generation
  sender="automation@example.com"
  recepient="student-04-c8be53d51229@example.com"
  attach_path=""
  subject=err
  body="Please check your system and resolve the issue as soon as possible."
  message=emails.generate_errorReport(sender,recepient,subject,body)
  emails.send_email(message)

