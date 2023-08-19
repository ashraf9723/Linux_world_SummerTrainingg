from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send a text message
message = client.messages.create(
    to='+1234567890',  # Replace with the recipient's phone number
    from_='+0987654321',  # Replace with your Twilio phone number
    body='Hello, this is a test message from Twilio!')

print("Message SID:", message.sid)
