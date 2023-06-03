from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'EMAIL_ENVIO'
email_password = password

email_receiver = 'EMAIL_RECEPTOR'

subject = 'Email de prueba SMTP'
body = 'Prueba de envio de mail usando Python. Grupo NSA. Redes2023'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
