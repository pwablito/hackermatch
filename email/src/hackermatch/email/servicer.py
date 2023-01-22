from hackermatch.grpc.stubs import email_pb2_grpc, email_pb2

import logging
import smtplib
import ssl
import os
from email.message import EmailMessage


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EmailServicer(email_pb2_grpc.EmailServiceServicer):
    def SendMatchAlert(self, request, context):
        body = f"Hash: {request.hash}, email matches: {', '.join(request.emails)}"
        for to_addr in request.emails:
            context = ssl.create_default_context()
            smtp_port = 465
            smtp_server = "smtp.gmail.com"
            sender_email = os.environ.get("HACKERMATCH_SEND_EMAIL")
            sender_name = os.environ.get("HACKERMATCH_SEND_NAME")
            sender_password = os.environ.get("HACKERMATCH_SEND_PASSWORD")
            message = EmailMessage()
            message['From'] = "{} <{}>".format(sender_name, sender_email)
            message['To'] = to_addr
            message['Subject'] = f"HackerMatch Matches for Hash {request.hash}"
            message.set_content(body)
            with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
                try:
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, to_addr, message.as_string())
                except smtplib.SMTPAuthenticationError:
                    return email_pb2.SendMatchAlertResponse(
                        success=False,
                        message="Failed to login"
                    )
        return email_pb2.SendMatchAlertResponse(
            success=True,
        )
