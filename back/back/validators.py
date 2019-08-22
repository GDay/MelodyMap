import requests
from django.conf import settings
from rest_framework import serializers


def validate_hcaptcha(hcaptcha):
    data = { 'secret': settings.HCAPTCHA_SECRET_KEY, 'response': hcaptcha }
    response = requests.post(settings.HCAPTCHA_SITE_URL, data)
    if 'success' in response.json() and not response.json()['success']:
        raise serializers.ValidationError("hcaptcha is not correct")