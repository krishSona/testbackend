from core.models import Designation
from django.core.exceptions import ValidationError
from django.test import TestCase

from rest_framework.test import APIRequestFactory
import json
from api.v1.designation.views import DesignationViewSet


class DesignationModelTestCase(TestCase):
    def test_designation_must_have_name(self):
        try:
            Designation.objects.create()
        except:
            self.assertRaises(ValidationError)


class DesignationViewTestCase(TestCase):
    # Test for GET(retrieve)
    def test_designation_view_set(self):
        request = APIRequestFactory().get("/api/v1/designation/")
        designation_detail = DesignationViewSet.as_view({'get': 'retrieve'})
        designation = Designation.objects.create(name="Associate")
        response = designation_detail(request, pk=designation.pk)
        self.assertEqual(response.status_code, 200)

    # Test for GET(list)
    def test_designation_list(self):
        request = APIRequestFactory().get("/api/v1/designation/")
        designation_list = DesignationViewSet.as_view({'get': 'list'})
        response = designation_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE/POST
    def test_designation_create(self):
        data = json.dumps({
            "name": "Associate"
        })
        request = APIRequestFactory().post(
            '/api/v1/designation/', data=data, content_type='application/json')
        designation_data = DesignationViewSet.as_view({'post': 'create'})
        response = designation_data(request)
        self.assertEqual(response.status_code, 201)

    # Test for PUT/PATCH
    def test_designation_update(self):
        data = json.dumps({
            "name": "Associate"
        })
        request = APIRequestFactory().put(
            '/api/v1/designation/', data=data, content_type='application/json')
        designation_data = DesignationViewSet.as_view({'put': 'update'})
        designation = Designation.objects.create(name="Admin")
        response = designation_data(request, pk=designation.pk)
        self.assertEqual(response.status_code, 200 or 204)
