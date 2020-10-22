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
  lines=[]
  for Dict in paragraph:
    lines.append("name: "+Dict["name"]+"<br/>"+"weight: "+str(Dict["weight"])+" lbs"+"<br/>")
  report_data=Paragraph("<br/>".join(lines))
  report.build([report_title,empty_line,report_data])

