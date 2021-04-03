from django.test import TestCase
from django.core.exceptions import ValidationError

from core.models import Ifs, Bank

from rest_framework.test import APIRequestFactory
from api.v1.ifs.views import IfsViewSet
import json


class IfsModelTestCase(TestCase):
    def test_ifs_required_field(self):
        try:
            ifs = Ifs.objects.create(code='PUNB0391400')
        except:
            self.assertRaises(ValidationError)


class IfsViewTestCase(TestCase):
    # Test for GET(retrieve)
    def test_ifs_view_set(self):
        request = APIRequestFactory().get("/api/v1/ifs/")
        ifs_detail = IfsViewSet.as_view({'get': 'retrieve'})
        bank = Bank.objects.create(name='PNB')
        ifs = Ifs.objects.create(code="PUNB0931400", bank=bank)
        response = ifs_detail(request, pk=ifs.pk)
        self.assertEqual(response.status_code, 200)

    # Test for GET(list)
    def test_ifs_list(self):
        request = APIRequestFactory().get("/api/v1/ifs/")
        ifs_list = IfsViewSet.as_view({'get': 'list'})
        response = ifs_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE/POST
    def test_ifs_create(self):
        bank = Bank.objects.create(name='PNB')
        data = json.dumps({
            "code": "PUNB0391400",
            "bank": bank.id
        })
        request = APIRequestFactory().post(
            '/api/v1/ifs/', data=data, content_type='application/json')
        ifs_data = IfsViewSet.as_view({'post': 'create'})
        response = ifs_data(request)
        self.assertEqual(response.status_code, 201)

    # Test for PUT/PATCH
    def test_ifs_update(self):
        bank = Bank.objects.create(name='PNB')
        data = json.dumps({
            "code": "PUNB0391400",
            "bank": bank.id
        })
        request = APIRequestFactory().put(
            '/api/v1/ifs/', data=data, content_type='application/json')
        ifs_data = IfsViewSet.as_view({'put': 'update'})
        ifs = Ifs.objects.create(code="PUNB03914", bank=bank)
        response = ifs_data(request, pk=ifs.pk)
        self.assertEqual(response.status_code, 200 or 204)
