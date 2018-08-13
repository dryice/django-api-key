"""Tests for the models of the django_api_key app."""
from django.test import TestCase
from mixer.backend.django import mixer


class APIKeyModelTests(TestCase):
    def test_no_key_no_access(self):
        key = mixer.blend('django_api_key.APIKey')
        print(key.path_re)
        print(key.name)
