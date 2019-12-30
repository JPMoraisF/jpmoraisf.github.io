import smtplib
import mimetypes
import email
import email.mime.application
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send_email():
        TO=data['user']                                                         # EMAIL DE DESTINO DA MENSAGEM
        GMAIL_USER=''								# EMAIL DE QUEM VAI ENVIAR
        GMAIL_PASS=data['password']						#SENHA DO EMAIL QUE VAI ENVIAR
        SUBJECT='assunto do email'
        TEXT='texto do email'
        msg= MIMEMultipart()
        msg['Subject']= SUBJECT
        msg['To']=TO
        msg.preamble= TEXT
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        #s.ehlo()
        s.login(GMAIL_USER, GMAIL_PASS)		
        s.sendmail(GMAIL_USER,TO,msg.as_string())
        s.quit()
        print('Enviado')


import json
with open('assets/python/config.json') as file:
        data = json.load(file)

send_email()
