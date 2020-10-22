#!/usr/bin/env python3
import reports
import emails
from datetime import date
import run 
if __name__="__main__":
  paragraph=run.RetList()
  ##report generation
  today=date.today()
  d1 = today.strftime("%m %d,%Y")
  title="Processed Update on {}".fromat(d1)
  path="/tmp/processed.pdf"
  reports.generate_report(path, title,paragraph)
    ## email generation 
  sender="automation@example.com"
  recepient="@example.com"
  attach_path=path
  subject="Upload Completed - Online Fruit Store"
  body="All fruits are uploaded to our website successfully. A detailed list is attached to this email." 
  message=emails.generate_email(sender,recepient,subject,body,attach_path)
  emails.send_email(message)
