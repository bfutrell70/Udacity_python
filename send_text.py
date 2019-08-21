# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'dfkjgdk;fjhdfkjgadfgb'
auth_token = "skjlgdkjfsgkjdfgkjdghkj"
client = Client(account_sid, auth_token)

# NOTE: when creating a Twilio trial account I'm sure it gives you a trial phone number
# 	  however when you signed up a long time ago there is no phone number
#	   PHONE NUMBERS MUST BE PURCHASED
#       if a phone number is not used within 30 days the phone number is released
message = client.messages.create(
	body = "My name is Ron Burgundy?",
	to = "+9197411959",		# Replace with your phone number
	from_ = "+9197411959"	  # Replace with your Twilio number
)
print(message.sid)
