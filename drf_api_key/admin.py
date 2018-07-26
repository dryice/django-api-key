"""Admin classes for the drf_api_key app."""
from django.contrib import admin

from drf_api_key.models import APIKey, KeyGroup


@admin.register(KeyGroup)
class KeyGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'path_re', ]
    search_fields = ['name', ]


@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ['name', 'key', 'path_re', 'group', 'created', 'updated']
    search_fields = ['name', 'group__name']
