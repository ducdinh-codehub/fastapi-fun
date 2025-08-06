import smtplib, ssl

import config
from database import Database
from .models import EmailManager, SendingEmailRequest
from sqlmodel import Session
from email.mime.text import MIMEText

engine = Database().engine

subject = "Hi there (NO REPLY)"

smtp_server = config.Settings().smtp_host
port = config.Settings().smtp_port
sender_email = config.Settings().smtp_user
password = config.Settings().smtp_password

def sendEmail(data: SendingEmailRequest):
    message = f"""\
                    Dear Mr/Ms {data.client_name},

                    Welcome to our system, thank you for support and using our service.

                    This message is auto sent from Smart Agricultural BE System, please do not reply this mail.
                    
                    Best Regards."""
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    receipient = [sender_email, data.email_receiver]
    msg['To'] = ', '.join(receipient) 

    with smtplib.SMTP_SSL(smtp_server, port) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, receipient, msg.as_string())
            mail_sending_status = True
            mail_sending_error = None
        except Exception as e:
            print('e', e)
            mail_sending_status = False
            mail_sending_error = e

    # Adding email content into email manager table.
    email = EmailManager(content = message, created_at = data.created_at, updated_at = data.updated_at, owner = sender_email, sending_status = mail_sending_status, receiver_email=data.email_receiver, receiver_name=data.client_name, error_sending=mail_sending_error)
    session = Session(engine)
    session.add(email)
    session.commit()

    return {"message": "Send Email Success"}