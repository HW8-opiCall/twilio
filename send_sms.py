import os
from twilio.rest import Client

#hide
# Account SID from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
# Auth Token from twilio.com/console
auth_token  = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+XXXXXXXXXXX", 
    from_="+XXXXXXXXXX",
    body="Overdose alert;\nCoordinates:")

print(message.sid)
