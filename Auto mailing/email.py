import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'ur mailID'
email['to'] = 'to mail ID'
email['subject'] = 'Heyyyyyyyyyyyyyyy!!!!!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('ur mailID', 'ur password')
  smtp.send_message(email)
  print('Done')
