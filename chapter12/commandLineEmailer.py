import sys
import smtplib
from email.mime.text import MIMEText
import os

if len(sys.argv) < 4:
    print("Usage: python emailer.py <recipient_email> <subject> <body>")
    sys.exit(1)

recipient = sys.argv[1]
subject = sys.argv[2]
body = sys.argv[3]

EMAIL_ADDRESS = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

msg = MIMEText(body)
msg['From'] = EMAIL_ADDRESS
msg['To'] = recipient
msg['Subject'] = subject

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())

print("Email sent successfully!")
