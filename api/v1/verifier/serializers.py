from rest_framework import serializers
from core.models import Verifier


class VerifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verifier
        fields = '__all__'
