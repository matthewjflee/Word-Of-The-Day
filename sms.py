import smtplib

"""
Send an SMS text
"""

carriers = {
	'fido':  '@sms.fido.ca',
	'telus': '@mms.telusmobility.com',
	'koodo': '@msg.telus.com',
	'bell':  '@txt.bell.ca'
}

def send(message):
    to_number = 'number{}'.format(carriers['carrier'])
    auth = ('email', 'password')

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    server.sendmail( auth[0], to_number, message)
