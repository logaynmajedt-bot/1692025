import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Hello from Python")
msg["subject"] = "Reminder"
msg["From"] = "logaynmajedt@gmail.com"
msg["To"] = "logayntafesh@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("logaynmajedt@gmail.com", "App_password")
    server.send_message(msg)
