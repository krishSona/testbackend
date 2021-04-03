from core.models import Booking
from django.core.exceptions import ValidationError
from django.test import TestCase

from rest_framework.test import APIRequestFactory
import json
from api.v1.booking.views import BookingViewSet


class BookingModelTestCase(TestCase):
    def test_booking_required_fields(self):
        booking = Booking(name='abc')
        with self.assertRaises(ValidationError):
            booking.full_clean()


class BookingViewTestCase(TestCase):
    # Test for GET(list)
    def test_booking_list(self):
        request = APIRequestFactory().get("/api/v1/booking/")
        booking_list = BookingViewSet.as_view({'get': 'list'})
        response = booking_list(request)
        self.assertEqual(response.status_code, 200)

    # Test for CREATE/POST
    def test_booking_create(self):
        data = json.dumps({
            "name": "Upendra Kumar",
            "phone": "8795069822",
            "email": "upendra@gmail.com",
            "company": "Global",
            "status": 0,
            "category": 1,
        })
        request = APIRequestFactory().post(
            '/api/v1/booking/', data=data, content_type='application/json')
        booking_data = BookingViewSet.as_view({'post': 'create'})
        response = booking_data(request)
        self.assertEqual(response.status_code, 200)
