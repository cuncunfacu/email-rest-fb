import os
import smtplib
from email.message import EmailMessage

def send_email(to: str, subject: str, plain_txt_content: str, html_content: str) -> None:
    EMAIL_ADDRESS=os.environ.get('EMAIL_ADDRESS')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to

    msg.set_content(plain_txt_content)

    msg.add_alternative(f"""\
                        {html_content}
                        """,
                        subtype='html')


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)