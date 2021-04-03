from rest_framework import serializers
from core.models import Company
from api.v1.employer.serializers import EmployerSerializer
from api.v1.industry.serializers import IndustrySerializer
from api.v1.employee_range.serializers import EmployeeRangeSerializer
from api.v1.city.serializers import CitySerializer
from api.v1.state.serializers import StateSerializer


class CompanySerializer(serializers.ModelSerializer):
    employer_set = EmployerSerializer(many=True, required=False)
    industry = IndustrySerializer(required=False)
    employee_range = EmployeeRangeSerializer(required=False)
    city = CitySerializer(required=False)
    state = StateSerializer(required=False)

    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        employer_validated_data = validated_data.pop('employer_set')
        company = Company.objects.create(**validated_data)
        employer_set_serializer = self.fields['employer_set']
        for each in employer_validated_data:
            each['company'] = company
        employers = employer_set_serializer.create(employer_validated_data)
        return company


class CompanyAutoCompleteListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id', 'name']


class PrincipalCompanyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id', 'name', 'rid']


class CompanyDomainListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id', 'name', 'domain_name']
