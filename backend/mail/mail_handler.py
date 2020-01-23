#Create Email Verification Functions
#Create Mass Email System

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

port = 587
server = 'smtp.gmail.com'
#Move these to config file in the future
smtp_user = "user_name"
smtp_password = "password"

def send_mail(mail_to,subject,message):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = mail_to
    msg.attach(MIMEText(message))
    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()
    s.login(smtp_user, smtp_password)
    s.sendmail(smtp_user, mail_to, msg.as_string())
    print(msg)
    s.quit()



def verify_account(account_id,first_name,last_name):
    #WIP Account Verification System
    pass

send_mail("neko_shinigami@yahoo.com","Cyber Gladiators Mail System","Hello! This is a test for the Cyber Gladiators Mail System!")
    
