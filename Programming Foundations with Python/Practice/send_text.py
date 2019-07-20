from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb172d30d544b5891d0a6633eae8d2c06"
# Your Auth Token from twilio.com/console
auth_token  = "25c5e5c894300c3cbef74a2f9ec340df"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+886919301678", # Replace with your phone number
    from_="+15017250604", # Replace with your Twilio number
    body="My name is Jeffrey")

print(message.sid)
