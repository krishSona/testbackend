from core.models import EmployeeRange
from django.core.exceptions import ValidationError
from django.test import TestCase

from rest_framework.test import APIRequestFactory
import json
from api.v1.employee_range.views import EmployeeRangeViewSet


class EmployeeRangeModelTestCase(TestCase):
    def test_EmployeeRange_must_have_number(self):
        try:
            EmployeeRange.objects.create()
        except:
            self.assertRaises(ValidationError)


class DesignationViewTestCase(TestCase):
    # Test for GET(retrieve)
    def test_employee_range_view_set(self):
        request = APIRequestFactory().get("/api/v1/employee_range/")
        employee_range_detail = EmployeeRangeViewSet.as_view({'get': 'retrieve'})
        employee_range = EmployeeRange.objects.create(number="100-200")
        response = employee_range_detail(request, pk=employee_range.pk)
        self.assertEqual(response.status_code, 200)

    # Test for GET(list)
    def test_employee_range_list(self):
        request = APIRequestFactory().get("/api/v1/employee_range/")
        employee_range_list = EmployeeRangeViewSet.as_view({'get': 'list'})
        response = employee_range_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE/POST
    def test_employee_range_create(self):
        data = json.dumps({
            "number": "0-100"
        })
        request = APIRequestFactory().post(
            '/api/v1/employee_range/', data=data, content_type='application/json')
        employee_range_data = EmployeeRangeViewSet.as_view({'post': 'create'})
        response = employee_range_data(request)
        self.assertEqual(response.status_code, 201)

    # Test for PUT/PATCH
    def test_employee_range_update(self):
        data = json.dumps({
            "number": "0-100"
        })
        request = APIRequestFactory().put(
            '/api/v1/employee_range/', data=data, content_type='application/json')
        employee_range_data = EmployeeRangeViewSet.as_view({'put': 'update'})
        employee_range = EmployeeRange.objects.create(number="100-200")
        response = employee_range_data(request, pk=employee_range.pk)
        self.assertEqual(response.status_code, 200 or 204)






