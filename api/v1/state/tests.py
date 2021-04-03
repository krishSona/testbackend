from core.models import State
from django.core.exceptions import ValidationError
from django.test import TestCase

from rest_framework.test import APIRequestFactory
import json
from api.v1.state.views import StateViewSet


class StateModelTestCase(TestCase):
    def test_state_must_have_name(self):
        try:
            State.objects.create()
        except:
            self.assertRaises(ValidationError)


class StateViewTestCase(TestCase):
    # Test for GET(retrieve)
    def test_state_view_set(self):
        request = APIRequestFactory().get("/api/v1/state/")
        state_detail = StateViewSet.as_view({'get': 'retrieve'})
        state = State.objects.create(name="Uttar Pradesh")
        response = state_detail(request, pk=state.pk)
        self.assertEqual(response.status_code, 200)

    # Test for GET(list)
    def test_state_list(self):
        request = APIRequestFactory().get("/api/v1/state/")
        state_list = StateViewSet.as_view({'get': 'list'})
        response = state_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE/POST
    def test_state_create(self):
        data = json.dumps({
            "name": "Uttar Pradesh"
        })
        request = APIRequestFactory().post(
            '/api/v1/state/', data=data, content_type='application/json')
        state_data = StateViewSet.as_view({'post': 'create'})
        response = state_data(request)
        self.assertEqual(response.status_code, 201)

    # Test for PUT/PATCH
    def test_state_update(self):
        data = json.dumps({
            "name": "Uttar Pradesh"
        })
        request = APIRequestFactory().put(
            '/api/v1/state/', data=data, content_type='application/json')
        state_data = StateViewSet.as_view({'put': 'update'})
        state = State.objects.create(name="Haryana")
        response = state_data(request, pk=state.pk)
        self.assertEqual(response.status_code, 200 or 204)
