# -*- coding: utf-8 -*-
"""Parameters and constants."""
RESERVER_VERSION = "0.1"
RESERVER_NAME = "reserver"
PYPI_TEST_URL = "https://test.pypi.org/project"
PYPI_MAIN_URL = "https://pypi.org/project"
PACKAGE_PARAMETERS = {
    "description": "This name has been reserved using Reserver",
    "author": "Development Team",
    "author_email": "test@test.com",
    "url": "https://url.com",
    "download_url": "https://download_url.com",
    "source": "https://github.com/source",
    "license": "MIT",
}
VALIDATIONS = {
    "email": r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
    "url": r'^(http|https)://[a-zA-Z0-9.-_]+\.[a-zA-Z]{2,}(/\S*)?$',
}
