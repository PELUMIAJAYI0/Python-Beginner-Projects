from email.message import EmailMessage
import ssl
import smtplib

#the sender details: the email address and password to the email address
email_sender = "ajayioluwapelumi920@gmail.com"
email_password = "xvlo lbpd peft ngmt"

#the receiver email address
email_receiver = "oluwapelumi.ajayi@student.aul.edu.ng"

#subject of the email
subject = "An Order From Pelumi"

#main body of the email, what the sender would send to the receiver
body ="""Dont forget to read and prepare for the upcoming exams"""

#created an instance of the image
email = EmailMessage()
email["From"] = email_sender
email["To"] = email_receiver
email["Subject"] = subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, email.as_string())

