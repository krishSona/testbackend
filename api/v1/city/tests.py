from core.models import City
from django.core.exceptions import ValidationError
from django.test import TestCase

from rest_framework.test import APIRequestFactory
import json
from api.v1.city.views import CityViewSet


class CityModelTestCase(TestCase):
    def test_city_must_have_name(self):
        try:
            City.objects.create()
        except:
            self.assertRaises(ValidationError)


class CityViewTestCase(TestCase):
    # Test for GET(retrieve)
    def test_city_view_set(self):
        request = APIRequestFactory().get("/api/v1/city/")
        city_detail = CityViewSet.as_view({'get': 'retrieve'})
        city = City.objects.create(name="Delhi")
        response = city_detail(request, pk=city.pk)
        self.assertEqual(response.status_code, 200)

    # Test for GET(list)
    def test_city_list(self):
        request = APIRequestFactory().get("/api/v1/city/")
        city_list = CityViewSet.as_view({'get': 'list'})
        response = city_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE/POST
    def test_city_create(self):
        data = json.dumps({
            "name": "Delhi"
        })
        request = APIRequestFactory().post(
            '/api/v1/city/', data=data, content_type='application/json')
        bank_data = CityViewSet.as_view({'post': 'create'})
        response = bank_data(request)
        self.assertEqual(response.status_code, 201)

    # Test for PUT/PATCH
    def test_city_update(self):
        data = json.dumps({
            "name": "Delhi"
        })
        request = APIRequestFactory().put(
            '/api/v1/city/', data=data, content_type='application/json')
        city_data = CityViewSet.as_view({'put': 'update'})
        city = City.objects.create(name="Kolkata")
        response = city_data(request, pk=city.pk)
        self.assertEqual(response.status_code, 200 or 204)
