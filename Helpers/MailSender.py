import smtplib, ssl
import certifi
import os

class MailSender:
    
    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        
        self.receiverEmail = os.getenv('To')
        self.sender_mail = os.getenv('From')
        self.password = os.getenv('FromPassword')

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        
        for email in emails:
            print(self.sender_mail, email, f"Subject: {subject}\n{content}")
            result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()