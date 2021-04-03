from core.models import Department
from django.core.exceptions import ValidationError
from django.test import TestCase

from rest_framework.test import APIRequestFactory
import json
from api.v1.department.views import DepartmentViewSet


class DepartmentModelTestCase(TestCase):
    def test_department_must_have_name(self):
        try:
            Department.objects.create()
        except:
            self.assertRaises(ValidationError)


class CityViewTestCase(TestCase):
    # Test for GET(retrieve)
    def test_department_view_set(self):
        request = APIRequestFactory().get("/api/v1/department/")
        department_detail = DepartmentViewSet.as_view({'get': 'retrieve'})
        department = Department.objects.create(name="HR")
        response = department_detail(request, pk=department.pk)
        self.assertEqual(response.status_code, 200)

    # Test for GET(list)
    def test_department_list(self):
        request = APIRequestFactory().get("/api/v1/department/")
        department_list = DepartmentViewSet.as_view({'get': 'list'})
        response = department_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE/POST
    def test_department_create(self):
        data = json.dumps({
            "name": "HR"
        })
        request = APIRequestFactory().post(
            '/api/v1/department/', data=data, content_type='application/json')
        department_data = DepartmentViewSet.as_view({'post': 'create'})
        response = department_data(request)
        self.assertEqual(response.status_code, 201)

    # Test for PUT/PATCH
    def test_department_update(self):
        data = json.dumps({
            "name": "HR"
        })
        request = APIRequestFactory().put(
            '/api/v1/department/', data=data, content_type='application/json')
        department_data = DepartmentViewSet.as_view({'put': 'update'})
        department = Department.objects.create(name="Sales")
        response = department_data(request, pk=department.pk)
        self.assertEqual(response.status_code, 200 or 204)
