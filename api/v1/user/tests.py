from authentication.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase


class UserModelTestCase(TestCase):
    def setUp(self):
        self.username = "upendra.kumar"
        self.password = "upendra@123"

        self.test_user = User.objects.create_user(
            username=self.username
        )

    def test_username_is_required(self):
        try:
            User.objects.create()
        except:
            self.assertRaises(ValidationError)

    def test_create_user(self):
        self.assertIsInstance(self.test_user, User)

    def test_default_user_is_active(self):
        self.assertTrue(self.test_user.is_active)

    def test_default_user_is_staff(self):
        self.assertFalse(self.test_user.is_staff)

    def test_default_user_is_superuser(self):
        self.assertFalse(self.test_user.is_admin)
