import os
from twilio.rest import Client

#hide
# Account SID from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
# Auth Token from twilio.com/console
auth_token  = os.environ['TWILIO_AUTH_TOKEN']
recepient_number = os.environ

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15483337345", 
    from_="+12267814024",
    body="게임 시작합니다. 상금은 총456억.")

print(message.sid)