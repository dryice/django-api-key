"""Tests for the models of the django_api_key app."""
from django.test import Client, TestCase


class APIKeyModelTests(TestCase):
    def test_no_key_no_access(self):
        c = Client()
        response = c.get('/admin/')
        self.assertEqual(response.status_code, 403)
