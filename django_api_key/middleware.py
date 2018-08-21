import re

from django.conf import settings
from django.core.exceptions import PermissionDenied, ValidationError
from django.utils.deprecation import MiddlewareMixin

from django_api_key.models import APIKey, IPAccess
from ipware import get_client_ip
from ipware.defaults import IPWARE_PRIVATE_IP_PREFIX

IGNORE_API_KEY_CHECK_FOR = getattr(
    settings,
    "IGNORE_API_KEY_CHECK_FOR",
    ["/admin/.*", "/docs/.*"])

IGNORE_API_KEY_CHECK_FOR = [re.compile(x) for x in IGNORE_API_KEY_CHECK_FOR]


class APIKeyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        for i in IGNORE_API_KEY_CHECK_FOR:
            if i.search(request.path):
                return

        api_key = request.META.get('HTTP_API_KEY', '')
        if not api_key:
            auth_header = request.META.get('HTTP_AUTHORIZATION', '')
            try:
                key, value = auth_header.split()
                if key.lower() == "api_key":
                    api_key = value
            except ValueError:
                pass

        client_ip, is_routable = get_client_ip(request)
        if client_ip and not client_ip.startswith(IPWARE_PRIVATE_IP_PREFIX):
            try:
                ip_access_object = IPAccess.objects.get(ip=client_ip)
                if ip_access_object.is_path_valid(request.path):
                    request.ip_access = ip_access_object
                    return
            except IPAccess.DoesNotExist:
                pass

        try:
            api_key_object = APIKey.objects.get(key=api_key)
        except (APIKey.DoesNotExist, ValidationError):
            raise PermissionDenied('API key missing or invalid.')

        if not api_key_object.is_path_valid(request.path):
            raise PermissionDenied('API key missing or invalid.')

        request.api_key = api_key_object
