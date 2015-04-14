
from gmail import GMail, Message
"""https://github.com/paulchakravarti/gmail-sender/blob/master/gmail/gmail.py"""

def get_mailer():
	with open('config.txt', 'r') as configfile:
		lines = [x for x in configfile]
		username = lines[0].rstrip().replace(' ', '')
		password = lines[1].rstrip().replace(' ', '')
	print 'connecting with '+username+' '+password
	gmailer = GMail(username, password)
	gmailer.connect()
	return gmailer


# def get_mail_reader():
# 	with open('config.txt', 'r') as configfile:
# 		lines = [x for x in configfile]
# 		username = lines[0].rstrip().replace(' ', '')
# 		password = lines[1].rstrip().replace(' ', '')
# 	gmailer = GmailReader(username, password)
# 	gmailer.login()
# 	print 'this is hte gmail reader'
# 	print dict(gmailer)

def read_messages():
	print 'hello'


def render_tabling_template():
	print 'rendering tabling template'

if __name__=='__main__':

	SEND_MESSAGE = True

	gmailer = get_mailer()
	if gmailer and SEND_MESSAGE:
		print dir(gmailer)
		subject = "This is the subject"
		to = "kzhang22@berkeley.edu"
		html = "<h1>This is the HTML</h1>"
		msg = Message(subject = subject, to = to, html = html, attachments = None)
		gmailer.send(msg)
	else:
		print gmailer
		print 'No message sent'

	print dir(gmailer)
