from django.test import TestCase
from api.v1.authentication.views import UserLoginView, RefreshTokenView
from authentication.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.test import APIRequestFactory
import json


class AuthenticationViewTestCase(TestCase):

    def test_user_login_view(self):
        user = User.objects.create_user(
            username='upendra@gmail.com', password='django1234')
        data = json.dumps({
            "username": "upendra@gmail.com",
            "password": "django1234",
        })
        request = APIRequestFactory().post(
            '/api/v1/authentication/token/', data=data, content_type='application/json')
        login_data = UserLoginView.as_view()
        response = login_data(request)
        self.assertEqual(response.status_code, 200)

    def test_refresh_token_view(self):
        user = User.objects.create_user(
            username='upendra@gmail.com', password='django1234')
        refresh = RefreshToken.for_user(user)
        data = json.dumps({
            "refresh": str(refresh)
        })
        request = APIRequestFactory().post(
            '/api/v1/authentication/token/refresh/', data=data, content_type='application/json')
        refresh_token_data = RefreshTokenView.as_view()
        response = refresh_token_data(request)
        self.assertEqual(response.status_code, 200)
