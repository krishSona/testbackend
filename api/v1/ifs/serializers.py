from rest_framework import serializers
from core.models import Ifs
from api.v1.bank.serializers import BankSerializer


class IfsSerializer(serializers.ModelSerializer):
    bank = BankSerializer()

    class Meta:
        model = Ifs
        fields = '__all__'
