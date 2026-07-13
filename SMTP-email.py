'''
SMTP module
email.message

plnz buxg exed dsww
'''

import smtplib
import ssl
from email.message import EmailMessage
sender_email = "lavanyayalamanchi2005@gmail.com"
password = "plnzbuxgexeddsww"

reciever_email = "lavanyayalamanchi689@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = reciever_email
message["Subject"] = "Welcome Mail"
message.set_content("Hi Lavanya\n ""Welcome come to the Codegnan")

context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com",port=587)as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email,password)
    smtp.send_message(message)
    smtp.quit()
    
    
