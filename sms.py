import json
import urllib.request
import urllib.parse
from django.conf import settings


def send(numbers, message):
    apikey = settings.SMS_API_KEY
    sender = settings.SMS_SENDER_ID
    data = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,'message': message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    response = urllib.request.urlopen(request, data)
    _bytes = response.read()
    _string = _bytes.decode('utf-8')
    _json = json.loads(_string)
    return _json['status']