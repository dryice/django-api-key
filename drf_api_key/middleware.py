from django.core.exceptions import PermissionDenied

from drf_api_key.models import APIKey


class APIKeyMiddleware(object):
    def process_request(self, request):
        api_key = request.META.get('HTTP_API_KEY', '')

        try:
            api_key_object = APIKey.objects.get(key=api_key)
        except APIKey.DoesNotExist:
            raise PermissionDenied('API key missing or invalid.')

        if not api_key_object.is_valid(request.path):
            raise PermissionDenied('API key missing or invalid.')

        request.api_key = api_key_object
