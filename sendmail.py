import os
import smtplib
import imghdr
from email.message import EmailMessage
import re
import time

counter = 0

EMAIL_ADDRESS = ''
EMAIL_PASSWORD = ''

firstname = ''
lastname = ''
address = ''
town = ''
zip = ''
state = ''

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	with open("colleges.txt") as fp:
		line = fp.readline()
		while(line):
			counter += 1
			linesplit = re.split(r'\t+', line)
			print(linesplit[0] + " : " + linesplit[1])
			msg = EmailMessage()
			msg['Subject'] = 'A Request From A Future Applicant'
			msg['From'] = EMAIL_ADDRESS
			msg.set_content('Hello ' + linesplit[0] + ' Admissions.\n\nI just finished my overseas gap-year program and want to apply to ' + linesplit[0] + ' for the upcoming spring semester. It would mean the world to me you could send me a shirt so I could represent your university.\n\nIf possible, could you please send to \n\n'+ firstname + ' ' + lastname +'\n'+ address + '\n' + town + ',' + state + ' ' + zip + '\n\n Thank you,\n' + firstname)
			msg['To'] = linesplit[1]
			line = fp.readline()		
			smtp.send_message(msg)
			if counter == 50:
				counter = 0
				print("waiting...")
				time.sleep(120)
