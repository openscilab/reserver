# -*- coding: utf-8 -*-
"""Parameters and constants."""
OVERVIEW = """
Reserver is an open source Python package that offers the ability to quickly reserve a PyPI package name. Got a notion? Before it's taken, immediately reserve the product name!
"""
RESERVER_VERSION = "0.2"
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
INVALID_PACKAGE_PARAMETER_NAME_ERROR = "Given parameter doesn't exist among the supported user allowed parameters."
INVALID_PACKAGE_PARAMETER_VALUE_ERROR = "Invalid value for {parameter} that should be a valid {regex}"