"""Models for the drf_api_key app."""
import re
import uuid

from django.db import models


class KeyGroup(models.Model):
    name = models.CharField(max_length=128, unique=True)
    path_re = models.CharField(max_length=1024, default=".*",
                               help_text="An RE that the api-keys in this group can access")

    def __str__(self):
        return self.name


class APIKey(models.Model):
    name = models.CharField(max_length=128, unique=True)
    key = models.UUIDField(default=uuid.uuid4, editable=False)
    path_re = models.CharField(max_length=1024, default='',
                               help_text="If left blank, will use the one from group, if no group, will allow all. "
                               "If given, will overwrite group settings ")
    group = models.ForeignKey(KeyGroup, blank=True, null=True, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def url_re(self):
        if not self.path_re:
            if self.group:
                return re.compile(self.group.path_re)
            else:
                return re.compile(".*")
        else:
            return re.compile(self.path_re)
