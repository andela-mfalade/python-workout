import os
from twilio.rest import TwilioRestClient


# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_num = os.environ['TWILIO_PHONE_NUMBER']
client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(
    body="Hey Mayor, Go and eat! ;)",
    to="+2348137219945",
    from_=""
)
print message.sid
