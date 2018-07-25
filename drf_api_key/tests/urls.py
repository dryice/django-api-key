"""URLs to run the tests."""
from django.contrib import admin

from compat import include, url

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
