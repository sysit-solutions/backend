import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid
from smtplib import SMTP

from fastapi import HTTPException
from freenit.config import getConfig
from freenit.decorators import route

from ..models.email import models
from .router import api


def sendmail(message):
    config = getConfig()
    mail = config.mail
    if None not in [mail.host, mail.username, mail.password]:
        server = SMTP(host=mail.host, port=mail.port)
        if mail.ssl:
            server.ehlo()
            server.starttls()
            server.ehlo()
        server.login(mail.username, mail.password)
        to = "office+feedback@sysit.solutions"
        msg = MIMEText(message.message, "plain", "utf-8")
        msg["Subject"] = message.subject
        msg["To"] = to
        msg["From"] = message.email
        msg["Message-ID"] = make_msgid()
        msg["Date"] = formatdate(localtime=True)
        data = msg.as_string().encode('utf-8')
        print(data)
        server.sendmail(message.email, [to], data)


@route(api, "/email/feedback", models=models, tags=["email"])
class EmailFeedback:
    async def create(message: models.base):
        try:
            sendmail(message)
        except smtplib.SMTPAuthenticationError:
            raise HTTPException(status_code=403, detail="SMTP login failed")
        return message
