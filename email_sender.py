import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'BAAF Company'
email['to'] = 'abdoulfaridbassirou7898@gmail.com'
email['subject'] = 'Promotion'

email.set_content('''
      Dear Founder,

      BAAF Company has achieved a remarkable promotion and has grown significantly!

      kind regards
	''')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls() # tls is an encryption mecanism, and allows us to connect securely to the server.
	smtp.login('<your email address>', '<your password>')
	smtp.send_message(email)
