from rest_framework import serializers
from workers.models import Worker, Company


class WorkerSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()

    class Meta:
        model = Worker
        fields = ['id', 'name', 'balance', 'phone', 'company']