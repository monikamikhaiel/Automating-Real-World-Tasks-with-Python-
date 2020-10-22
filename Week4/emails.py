from email.message import EmailMessage
import smtplib
import mimetypes
import os
def generate_errorReport(sender,recepient,subject,body):
## get the attachement type
## prepare the message
  message=EmailMessage()
  message["From"]=sender
  message["To"]=recepient
  message["Subject"]=subject
  message.set_content(body)
  return message
def generate_email(sender,recepient,subject,body,attach_path):
## get the attachement type
  attach_filename=os.path.basename(attach_path)
  types,_=mimetypes.guess_type(attach_path)
  mimetype,subtype=types.split("/",1)
## prepare the message
  message=EmailMessage()
  message["From"]=sender
  message["To"]=recepient
  message["Subject"]=subject
  message.set_content(body)
  with open(attach_path,"rb") as f:
    message.add_attachment(f.read(),
      maintype=mimetype,subtype=subtype,filename=attach_filename)
  return message 
def send_email(message):
  server=smtplib.SMTP("localhost")
  #server.login(,)
  server.send_message(message)
  server.quit()
