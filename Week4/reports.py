#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
#from datetime import date
#today=date.today()
#d1 = today.strftime("%m %d,%Y")
#import run
def generate_report(path, title, paragraph):
  report = SimpleDocTemplate(path)
  styles = getSampleStyleSheet()
  report_title=Paragraph(title,styles["h1"])
  empty_line = Spacer(1,20)
  report_data=[]
  for Dict in paragraph:
    line="name:"+Dict["name"]+"\n"+"weight:"+Dict["weight"]+"lbs"+"\n"
    report_data.append(Paragraph(line, styles["h2"]))
    report_data.append(Spacer(1,20))
  report.build([report_title,empty_line,report_data])

