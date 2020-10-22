from email.message import EmailMessage
import smtplib
import mimetypes
import os
def generate_email(sender,recepient,attach_path):
## get the attachement type
  attach_filename=os.path.basename(attach_path)
  types,_=mimetypes.guess_type(attach_path)
  mimetype,subtype=types.split("/",1)
## prepare the message
  message=EmailMessage()
  message["From"]=sender
  message["To"]=recepient
  with open(attach,"rb") as f:
    message.add_attachment(f.read(),
      maintype=mimetype,subtype=subtype,filename=attach_filename)
  return message 
def send_mail(message):
  server=smtplib.SMTP("localhost")
  #server.login(,)
  server.send_message(message)
  server.quit()
