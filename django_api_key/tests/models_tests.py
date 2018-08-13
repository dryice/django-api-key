"""Tests for the models of the django_api_key app."""
from django.test import Client, TestCase

from django_api_key.models import APIKey


class APIKeyModelTests(TestCase):
    def test_no_key_no_access(self):
        c = Client()
        response = c.get('/admin/')
        self.assertEqual(response.status_code, 403)

    def test_correct_key_can_access(self):
        me = APIKey.objects.create(name="test", path_re="/admin.*")

        c = Client()
        response = c.get('/admin/', follow=True, HTTP_API_KEY=me.key)
        self.assertEqual(response.status_code, 200)
