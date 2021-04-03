from rest_framework import serializers
from core.models import EmployeeRange


class EmployeeRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRange
        fields = '__all__'
