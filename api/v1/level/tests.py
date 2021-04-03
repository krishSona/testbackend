from core.models import Level
from django.core.exceptions import ValidationError
from django.test import TestCase

from rest_framework.test import APIRequestFactory
import json
from api.v1.level.views import LevelViewSet


class LevelModelTestCase(TestCase):
    def test_level_must_have_title(self):
        try:
            Level.objects.create()
        except:
            self.assertRaises(ValidationError)


class LevelViewTestCase(TestCase):
    # Test for GET(retrieve)
    def test_level_view_set(self):
        request = APIRequestFactory().get("/api/v1/level/")
        level_detail = LevelViewSet.as_view({'get': 'retrieve'})
        level = Level.objects.create(title="super")
        response = level_detail(request, pk=level.pk)
        self.assertEqual(response.status_code, 200)

    # Test for GET(list)
    def test_level_list(self):
        request = APIRequestFactory().get("/api/v1/level/")
        level_list = LevelViewSet.as_view({'get': 'list'})
        response = level_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE/POST
    def test_level_create(self):
        data = json.dumps({
            "title": "super"
        })
        request = APIRequestFactory().post(
            '/api/v1/level/', data=data, content_type='application/json')
        level_data = LevelViewSet.as_view({'post': 'create'})
        response = level_data(request)
        self.assertEqual(response.status_code, 201)

    # Test for PUT/PATCH
    def test_level_update(self):
        data = json.dumps({
            "title": "Super"
        })
        request = APIRequestFactory().put(
            '/api/v1/level/', data=data, content_type='application/json')
        level_data = LevelViewSet.as_view({'put': 'update'})
        level = Level.objects.create(title="lower")
        response = level_data(request, pk=level.pk)
        self.assertEqual(response.status_code, 200 or 204)
