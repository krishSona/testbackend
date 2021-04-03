from django.test import TestCase
from api.v1.services.views import SmsOtpView, ActivationEmailView
from authentication.models import User

from rest_framework.test import APIRequestFactory
import json


class ServicesViewTestCase(TestCase):

    def test_sms_send_view(self):
        user = User.objects.create_user(
            username='7007501490'
        )
        data = json.dumps({
            "phone": "7007501490",
            "template": "login"
        })
        request = APIRequestFactory().post(
            '/api/v1/services/sms/otp/', data=data, content_type='application/json'
        )
        sms_data = SmsOtpView.as_view()
        response = sms_data(request)
        self.assertEqual(response.status_code, 200)

    # def test_activation_email_view(self):
    #     user = User.objects.create_user(
    #         username='7007501490'
    #     )
    #     data = json.dumps({
    #         "subject": "testing activation email",
    #         "message": "blah blah blah",
    #         "from_email": "upendrakumarvipin@gmail.com",
    #         "to_email": "upendra@instasalary.app"
    #     })
    #     request = APIRequestFactory().post(
    #         '/api/v1/services/activation_email/', data=data, content_type='application/json'
    #     )
    #     activation_email_data = ActivationEmailView.as_view()
    #     response = activation_email_data(request)
    #     self.assertEqual(response.status_code, 200)
