from rest_framework import serializers
from core.models import Statement

from api.v1.employee.serializers import EmployeeListSerializer


class StatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statement
        fields = '__all__'


class StatementListSerializer(serializers.ModelSerializer):

    employee = EmployeeListSerializer()

    class Meta:
        model = Statement
        fields = '__all__'
