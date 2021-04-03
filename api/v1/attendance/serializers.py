from core.models import Attendance
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField


class AttendanceSerializer(serializers.ModelSerializer):
    start_at = serializers.TimeField(input_formats=['%I:%M %p', ], required=False)
    end_at = serializers.TimeField(input_formats=['%I:%M %p', ], required=False)
    image = Base64ImageField(required=False)

    class Meta:
        model = Attendance
        fields = '__all__'


class AttendanceStatementListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ['date', 'salary', 'description']
