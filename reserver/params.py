# -*- coding: utf-8 -*-
"""Parameters and constants."""
OVERVIEW = """
Reserver is an open source Python package that offers the ability to quickly reserve a PyPI package name. Got a notion? Before it's taken, immediately reserve the product name!
"""
RESERVER_VERSION = "0.5"
RESERVER_NAME = "reserver"
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
INVALID_CONFIG_FILE_NAME_ERROR = "Given file name for user-defined package params is not a string."
PARAM_FILE_DOES_NOT_EXIST_ERROR = "Given file doesn't exist."
INVALID_INPUT_USER_PARAM = "Invalid input for user params."
UNEQUAL_PARAM_NAME_LENGTH_ERROR = "You should pass either one single file path to be used for the package parameters \
or per each package name, there should be a specific dedicated file path."

MAIN_PYPI_REVOKE_TOKEN_MESSAGE = "Security Tip: Please consider revoking your PyPI token from https://pypi.org/manage/account/token if no longer needed."
TEST_PYPI_REVOKE_TOKEN_MESSAGE = "Security Tip: Please consider revoking your test PyPI token from https://test.pypi.org/manage/account/token if no longer needed."
