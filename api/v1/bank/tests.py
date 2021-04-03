from rest_framework.test import APIRequestFactory
import json

from api.v1.bank.views import BankViewSet
from core.models import Bank
from django.core.exceptions import ValidationError
from django.test import TestCase


class BankModelTestCase(TestCase):
    def test_bank_must_have_name(self):
        try:
            Bank.objects.create()
        except:
            self.assertRaises(ValidationError)


class BankViewTestCase(TestCase):
    # Test for GET(retrieve)
    def test_bank_view_set(self):
        request = APIRequestFactory().get("/api/v1/bank/")
        bank_detail = BankViewSet.as_view({'get': 'retrieve'})
        bank = Bank.objects.create(name="bob")
        response = bank_detail(request, pk=bank.pk)
        self.assertEqual(response.status_code, 200)

    # Test for GET(list)
    def test_bank_list(self):
        request = APIRequestFactory().get("/api/v1/bank/", {'title': 'bob'})
        bank_detail = BankViewSet.as_view({'get': 'list'})
        response = bank_detail(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE/POST
    def test_bank_create(self):
        data = json.dumps({
            "name": "BOB"
        })
        request = APIRequestFactory().post(
            '/api/v1/bank/', data=data, content_type='application/json')
        bank_data = BankViewSet.as_view({'post': 'create'})
        response = bank_data(request)
        self.assertEqual(response.status_code, 201)

    # Test for PUT/PATCH
    def test_bank_update(self):
        data = json.dumps({
            "name": "BOB"
        })
        request = APIRequestFactory().put(
            '/api/v1/bank/', data=data, content_type='application/json')
        bank_data = BankViewSet.as_view({'put': 'update'})
        bank = Bank.objects.create(name="bob")
        response = bank_data(request, pk=bank.pk)
        self.assertEqual(response.status_code, 200 or 204)




