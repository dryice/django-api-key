DRF API Key
============

Per URL api-key control for Django

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-api-key

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/dryice/django-api-key.git#egg=django_api_key

Add ``django_api_key`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'django_api_key',
    )

Migrate your database

.. code-block:: bash

    ./manage.py migrate django_api_key


Add the ``django_api_key`` URLs to your ``MIDDLEWARE``

.. code-block:: python

    MIDDLEWARE = [
        ...,
        'django_api_key.middleware.APIKeyMiddleware',
    ]

(Optional) adjust the URLs that you don't want api_key check. Default is:

.. code-block:: python

    IGNORE_API_KEY_CHECK_FOR = ["/admin/.*", "/docs/.*"]

Visit /admin/django_api_key/ipaccess/ and add rules accordingly



Usage
-----

TODO: 


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python3.7 django-api-key
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 2.0 and Django 2.1) and run the tests against both
environments.
