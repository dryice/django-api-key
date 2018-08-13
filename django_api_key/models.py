"""Models for the django_api_key app."""
import re
import uuid

from django.db import models


class KeyGroup(models.Model):
    name = models.CharField(max_length=128, unique=True)
    path_re = models.CharField(max_length=1024, default=".*",
                               help_text="An RE that the api-keys in this group can access")

    def __str__(self):
        return self.name


class AccessItem(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=128, unique=True)
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
        """Return the RE object for the item.

        If a path_re is given, use it.
        Otherwise try to use the path_re from group. If no group is defined, allow all paths.
        """
        if not self.path_re:
            if self.group:
                return re.compile(self.group.path_re)
            else:
                return re.compile(".*")
        else:
            return re.compile(self.path_re)

    def is_path_valid(self, path):
        """Check if the path could be accessed by this item."""
        return self.url_re.search(path)


class APIKey(AccessItem):
    key = models.UUIDField(default=uuid.uuid4, editable=False)


class IPAccess(AccessItem):
    ip = models.GenericIPAddressField()
