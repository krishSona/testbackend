import urllib3.request
import json
from daily_salary import settings
from services.sms.templates import otp
import os
from core.models import Setting


def call(phone_number, template, *args):
    if not (settings.ENV == "production"):
        setting = Setting.objects.filter(key='tester_phone').first()
        if setting and len(setting.value) == 10:
            phone_number = setting.value
        else:
            phone_number = None
    if phone_number:
        apikey = settings.CORE_KALEYRA_API_KEY
        sender = 'NSQURD'
        message = getattr(otp,template)(args)
        data = json.dumps({'type': 'OTP', 'sender': sender, 'to': '91'+phone_number,'body': message })
        headers = {'Content-Type': 'application/json', 'api-key': apikey}
        http = urllib3.PoolManager()
        response = http.request(
            "POST",
            "https://api.kaleyra.io/v1/HXAP1679963808IN/messages?",
            body=data,
            headers=headers
            )
        return json.loads(response.data)

