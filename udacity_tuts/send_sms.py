from twilio.rest import TwilioRestClient


# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACeeb7428aca8d1a9e8b4a26c5b9890a4c"
auth_token = "5f5d3f71ab3d25d7d5ebc7f53d2adb47"
client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(
    body="Hey Mayor, Go and eat! ;)",
    to="+2348137219945",
    from_="+12516629160"
)
print message.sid
