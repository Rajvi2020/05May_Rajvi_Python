import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = "+17372508034"
to_number = "+919104473913"

try:
    print(f"Sending SMS from {twilio_number} to {to_number}")
    client = Client(account_sid, auth_token)
    
    # Using Twilio approved template
    message = client.messages.create(
        body="Your Twilio code is 123456",
        from_=twilio_number,
        to=to_number
    )
    print("SMS Status:", message.status)
    print("Message SID:", message.sid)
except Exception as e:
    print(f"Twilio Error: {e}")
