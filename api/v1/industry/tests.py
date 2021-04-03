from core.models import Industry
from django.core.exceptions import ValidationError
from django.test import TestCase

from rest_framework.test import APIRequestFactory
import json
from api.v1.industry.views import IndustryViewSet


class IndustryModelTestCase(TestCase):
    def test_industry_must_have_name(self):
        try:
            Industry.objects.create()
        except:
            self.assertRaises(ValidationError)


class IndustryViewTestCase(TestCase):
    # Test for GET(retrieve)
    def test_industry_view_set(self):
        request = APIRequestFactory().get("/api/v1/industry/")
        industry_detail = IndustryViewSet.as_view({'get': 'retrieve'})
        industry = Industry.objects.create(name="IT")
        response = industry_detail(request, pk=industry.pk)
        self.assertEqual(response.status_code, 200)

    # Test for GET(list)
    def test_industry_list(self):
        request = APIRequestFactory().get("/api/v1/industry/")
        industry_list = IndustryViewSet.as_view({'get': 'list'})
        response = industry_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE/POST
    def test_industry_create(self):
        data = json.dumps({
            "name": "IT"
        })
        request = APIRequestFactory().post(
            '/api/v1/industry/', data=data, content_type='application/json')
        industry_data = IndustryViewSet.as_view({'post': 'create'})
        response = industry_data(request)
        self.assertEqual(response.status_code, 201)

    # Test for PUT/PATCH
    def test_industry_update(self):
        data = json.dumps({
            "name": "Health"
        })
        request = APIRequestFactory().put(
            '/api/v1/industry/', data=data, content_type='application/json')
        industry_data = IndustryViewSet.as_view({'put': 'update'})
        industry = Industry.objects.create(name="Kolkata")
        response = industry_data(request, pk=industry.pk)
        self.assertEqual(response.status_code, 200 or 204)
