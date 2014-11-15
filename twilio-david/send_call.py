from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC7889a1889c1833bd7181e45e60372776" 
AUTH_TOKEN = "1ad0315f3cc7a154aaaef048f1304f71" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
call = client.calls.create(
    to="+13473282978", 
    from_="+13477323709",  
    application_sid="AC7889a1889c1833bd7181e45e60372776", 
    method="GET",  
    fallback_method="GET",  
    status_callback_method="GET",    
    record="false"
) 
 
print call.sid