from selenium import webdriver
from os import mkdir, listdir, path
from shutil import rmtree
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
from email.utils import formatdate

def before_all(context):
    if path.exists(".\\screens\\"):
        rmtree(".\\screens\\")
    context.driver = webdriver.Firefox()
    mkdir(".\\screens\\")

def after_all(context):
    listScreen = listdir(".\\screens\\")
    msg = MIMEMultipart()
    msg["From"] = input('your e-mail: ')
    msg["To"] = input('receiver: ')
    msg["Subject"] = 'Тест сайта lib.usue.ru'
    msg["Date"] = formatdate(localtime=True)
    smtp = msg["From"]

    body = f"Тест произведен в {formatdate(localtime=True)}"
    msg.attach(MIMEText(body))

    attachment = MIMEBase('application', 'octet-stream')
    for screen in listScreen:
        with open(f".\\screens\\{screen}", 'rb') as scrn:
            image = scrn.read()
        attachment.set_payload(image)
        encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment', filename=f"{screen}")
        msg.attach(attachment)

    server = smtplib.SMTP(f"smtp.{smtp[smtp.index('@') + 1:]}", 587)
    server.starttls()
    server.ehlo()
    server.login(msg["From"], input('password: '))
    text = msg.as_string()
    server.sendmail(msg["From"], msg["To"], text)
    server.quit()