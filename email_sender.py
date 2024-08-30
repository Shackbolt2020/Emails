import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Name'
email['to'] = 'emailID'
email['subject'] = 'Subject'

email.set_content('Text')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email', '{pass}')
    smtp.send_message(email)
    print('Mail sent :)')
