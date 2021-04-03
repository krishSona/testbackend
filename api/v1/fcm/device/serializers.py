from rest_framework import serializers
from fcm_django.models import FCMDevice


class FCMDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = FCMDevice
        fields = '__all__'
