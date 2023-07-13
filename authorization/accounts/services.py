from twilio.rest import Client
from django.conf import settings


def send_code(phone_number, verification_code):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f'Your verification code: {verification_code}',
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number.as_e164
    )
    return message.sid
