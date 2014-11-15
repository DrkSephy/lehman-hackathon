from twilio.rest import TwilioRestClient

def sendMessage(numbers):
	"""
	Sends SMS to a list of numbers.

	Parameters
	----------
		numbers: list
			List of destination phone numbers.
			A phone number must be a string and be in the foramt: +Country_code+Number
			Ex: +13472212222
	"""
	account_sid = "ACb862b159ac14143c89a89643a844e7e8"
	auth_token = "2d69fb3b0650f953dd17ca6c2bbf6774" 

	client = TwilioRestClient(account_sid, auth_token)

	for number in numbers:
		message = client.messages.create(
		    body="A TEXT MESSAGE FROM A LIST OF NUMBERS", 
		    to = number,
		    from_="+13477323809")

	print message.sid





