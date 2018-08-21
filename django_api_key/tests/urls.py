"""URLs to run the tests."""
from django.contrib import admin
from django.urls import path

from django_api_key.tests.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test)
]
