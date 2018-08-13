"""Tests for the models of the django_api_key app."""
from django.test import Client, TestCase

from django_api_key.models import APIKey, IPAccess
from ipware.defaults import IPWARE_PRIVATE_IP_PREFIX


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

    def test_incorrect_key_can_not_access(self):
        APIKey.objects.create(name="test", path_re="/admin.*")

        c = Client()
        response = c.get('/admin/', follow=True, HTTP_API_KEY="random_key")
        self.assertEqual(response.status_code, 403)

    def test_incorrect_path_can_not_access(self):
        me = APIKey.objects.create(name="test", path_re="/admin111.*")

        c = Client()
        response = c.get('/admin/', follow=True, HTTP_API_KEY=me.key)
        self.assertEqual(response.status_code, 403)

    def test_no_key_whitelisted_ip_can_access(self):
        self.skipTest("waiting for new release with https://github.com/un33k/django-ipware/pull/42")
        IPAccess.objects.create(name="test", path_re="/admin.*", ip="127.0.0.1")

        with self.settings(IPWARE_NON_PUBLIC_IP_PREFIX=IPWARE_PRIVATE_IP_PREFIX):
            c = Client()
            response = c.get('/admin/', follow=True)
            self.assertEqual(response.status_code, 200)

    def test_non_routable_ip_can_not_access(self):
        IPAccess.objects.create(name="test", path_re="/admin.*", ip="127.0.0.1")
        c = Client()

        # by default localhost is not routable
        response = c.get('/admin/', follow=True)
        self.assertEqual(response.status_code, 403)
