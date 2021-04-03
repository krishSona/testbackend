from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from authentication.serializers import UserWithPasswordSerializer
from core.models import Employer


class EmployerSerializer(serializers.ModelSerializer):
    user = UserWithPasswordSerializer()

    photo = Base64ImageField(required=False)

    class Meta:
        model = Employer
        fields = '__all__'

    def create(self, validated_data):
        user_validated_data = validated_data.pop('user')
        user_set_serializer = self.fields['user']
        user = user_set_serializer.create(user_validated_data)
        employer = Employer.objects.create(user=user, **validated_data)
        return employer
