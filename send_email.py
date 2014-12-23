"""
Email function for Krishan's poetry project
"""
import smtplib
import urllib2
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# myemail = 'dshaff001@gmail.com'
# toemail = 'victoriasedmonds@gmail.com'

def internet_on():
    try:
        response=urllib2.urlopen('http://www.google.com',timeout=1)
        return True
    except urllib2.URLError: pass
    return False

def send_email(to_email,from_email,poem):

	if internet_on():
		msg = MIMEMultipart()
		msg['Subject'] = 'A poem from Krishan'
		msg['From'] = from_email
		msg['To'] = to_email
		body = poem
		msg.attach(MIMEText(body, 'plain'))
		text = msg.as_string()

		username = 'poetrytest1'
		password = 'poetrytest'

		try:
			server = smtplib.SMTP('smtp.gmail.com',587)
			server.set_debuglevel(True)
			server.ehlo()
			#if server.has_extn('STARTTLS'):
			server.starttls()
			server.ehlo()

			server.login(username,password)
			server.sendmail(from_email,to_email,text) #from_address, to_address
			server.close()
			return "Success! Email sent."
		except:
			server.close()
			return "Error occured, email not sent."

	elif not internet_on():
		return "Internet not connected! Check connection."






