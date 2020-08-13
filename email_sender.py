import socket
import sys
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender():
    def send_email(self, testing: bool, email_address: str, password: str, message: str):
        if testing:
            email_address = "mafalda63@ethereal.email"
            password = "QRqWvMvvugwkkfMtCR"

        EMAIL_TO = [email_address]
        EMAIL_FROM = email_address
        EMAIL_SUBJECT = "Network devices update."
        EMAIL_SPACE = ", "

        providers = {
            "google": {
                "host": "smtp.gmail.com",
                "port": 587
                # "port": 465
            },
            "ethereal": {
                "host": "smtp.ethereal.email",
                "port": 587
            }
        }

        current_provider = "ethereal"

        msg = MIMEMultipart()
        msg["From"] = EMAIL_FROM
        msg["To"] = EMAIL_SPACE.join(EMAIL_TO)
        msg["Subject"] = EMAIL_SUBJECT

        msg.attach(MIMEText(message, 'plain'))

        print(f"Sending e-mail to: {email_address}")

        try:
            pass
            context = ssl.create_default_context()
            with smtplib.SMTP(providers[current_provider]["host"], providers[current_provider]["port"]) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(email_address, password)
                server.sendmail(email_address, EMAIL_TO, msg.as_string())
                print("Email sent successfully")
        except Exception as e:
            print(e)
