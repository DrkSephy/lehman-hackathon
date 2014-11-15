from twilio.rest import TwilioRestClient

def sendMessage(className, number):
	"""
	Sends SMS to a list of numbers.

	Parameters
	----------
		numbers: list
			List of destination phone numbers.
			A phone number must be a 10 digits
			
	"""
	account_sid = "ACb862b159ac14143c89a89643a844e7e8"
	auth_token = "2d69fb3b0650f953dd17ca6c2bbf6774" 

	client = TwilioRestClient(account_sid, auth_token)

	
	message = client.messages.create(
	    body="Dear students, our class {cn} is canceled".format(cn=className), 
	    to = '+1'+ str(number),
	    from_="+13477323809")

	print message.sid





