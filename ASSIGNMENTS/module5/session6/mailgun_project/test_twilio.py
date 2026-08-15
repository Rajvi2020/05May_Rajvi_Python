import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_PHONE_NUMBER')

try:
    print(f"Testing with SID: {account_sid[:4]}... Token: {auth_token[:4]}...")
    client = Client(account_sid, auth_token)
    
    # Try sending an SMS to a dummy number just to see if auth fails immediately
    # Or just fetch the account details to verify credentials
    account = client.api.accounts(account_sid).fetch()
    print("Account status:", account.status)
except Exception as e:
    print(f"Twilio Error: {e}")
