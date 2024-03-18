import os
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # username = "rkyforstudy@gmail.com"
    username = os.getenv("Username")
    password = os.getenv("Password")

    receiver = os.getenv("Receiver")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)





