from rest_framework import serializers
from core.models import Employee
from authentication.serializers import UserSerializer
from api.v1.department.serializers import DepartmentSerializer
from api.v1.designation.serializers import DesignationSerializer
from api.v1.ifs.serializers import IfsSerializer
from api.v1.company.serializers import CompanySerializer
from api.v1.level.serializers import LevelSerializer


class EmployeeListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    company = CompanySerializer()
    ifs = IfsSerializer(required=False)
    level = LevelSerializer(required=False)
    department = DepartmentSerializer(required=False)
    designation = DesignationSerializer(required=False)

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        user_validated_data = validated_data.pop('user')
        user_set_serializer = self.fields['user']
        user = user_set_serializer.create(user_validated_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee


class EmployeeUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
