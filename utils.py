
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_message(title,text,email='skywalker0803r@gmail.com',password="wlqdsvznivzgdygs"):
  content = MIMEMultipart()
  content["subject"] = title
  content["from"] = email
  content["to"] = email
  content.attach(MIMEText(text))
  with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email,password)
    smtp.send_message(content)

if __name__ == '__main__':
  send_message('你好','測試寄信')
     