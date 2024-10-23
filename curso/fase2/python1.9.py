#enviando email SMTP 
import os
import pathlib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv # type: ignore

load_dotenv()

# caminho html
CAMINHO_HTML = pathlib.Path(__file__).parent / 'python1.9.html'

#dados do remetente e destinatario
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# Configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

#menssagem de texto
with open(CAMINHO_HTML, 'r') as arquivo:
    texto_arquivo = arquivo.read()
    print(texto_arquivo)
    
# transformação da menssagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Esta é o assunto do email'

corpo_email = MIMEText(texto_arquivo, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(remetente, destinatario, mime_multipart.as_string())
    print('Email enviado com sucesso')