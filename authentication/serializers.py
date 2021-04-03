from rest_framework import serializers
from authentication.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password','last_login','otp','otp_valid_till','is_active','is_admin', 'groups']
        extra_kwargs = {
            'username': {'validators': []}
        }

    def validate_password(self, data):
        value = data
        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)


class UserWithPasswordSerializer(serializers.ModelSerializer):
    """
    this serializer is used to create a user with password from employer serializer.
    """
    class Meta:
        model = User
        exclude = ['last_login','otp','otp_valid_till','is_active','is_admin']
        extra_kwargs = {
            'username': {'validators': []},
            'password': {'write_only': True}
        }

    def validate_password(self, data):
        value = data
        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)