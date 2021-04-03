from rest_framework.serializers import ModelSerializer
from core.models import QrCode


class QrCodeSerializer(ModelSerializer):

    class Meta:
        model = QrCode
        fields = '__all__'
