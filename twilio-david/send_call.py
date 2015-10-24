from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "" 
AUTH_TOKEN = "" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
call = client.calls.create(
    to="", 
    from_="",  
    application_sid="", 
    method="GET",  
    fallback_method="GET",  
    status_callback_method="GET",    
    record="false"
) 
 
print call.sid