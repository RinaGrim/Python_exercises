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
    msg["From"] = 'grimrina@yandex.ru'
    msg["To"] = 'kosh.sob@rambler.ru'
    msg["Subject"] = 'Тестовая тема'
    msg["Date"] = formatdate(localtime=True)

    body = "hello"
    msg.attach(MIMEText(body))

    attachment = MIMEBase('application', 'octet-stream')
    for screen in listScreen:
        with open(f".\\screens\\{screen}", 'rb') as scrn:
            image = scrn.read()
        attachment.set_payload(image)
        encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment', filename=f"{screen}")
        msg.attach(attachment)

    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.ehlo()
    server.login(input('your e-mail: '), input('password: '))
    text = msg.as_string()
    server.sendmail('grimrina@yandex.ru', ['kosh.sob@rambler.ru'], text)
    server.quit()