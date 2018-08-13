from django.core.exceptions import PermissionDenied
from ipware import get_client_ip

from django_api_key.models import APIKey, IPAccess


class APIKeyMiddleware(object):
    def process_request(self, request):
        api_key = request.META.get('HTTP_API_KEY', '')

        client_ip, is_routable = get_client_ip(request)
        if client_ip and is_routable:
            try:
                ip_access_object = IPAccess.objects.get(ip=client_ip)
                if ip_access_object.is_valid(request.path):
                    request.ip_access = ip_access_object
                    return
            except IPAccess.DoesNotExist:
                pass

        try:
            api_key_object = APIKey.objects.get(key=api_key)
        except APIKey.DoesNotExist:
            raise PermissionDenied('API key missing or invalid.')

        if not api_key_object.is_valid(request.path):
            raise PermissionDenied('API key missing or invalid.')

        request.api_key = api_key_object
