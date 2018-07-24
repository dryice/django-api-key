DRF API Key
============

Per URL api-key control for DRF

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install drf-api-key

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/dryice/drf-api-key.git#egg=drf_api_key

TODO: Describe further installation steps (edit / remove the examples below):

Add ``drf_api_key`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'drf_api_key',
    )

Add the ``drf_api_key`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = [
        url(r'^api_key/', include('drf_api_key.urls')),
    ]

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load drf_api_key_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate drf_api_key


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 drf-api-key
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.8 and Django 1.9) and run the tests against both
environments.
