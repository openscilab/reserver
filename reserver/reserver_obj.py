# -*- coding: utf-8 -*-
"""Reserver modules."""

# -*- coding: utf-8 -*-
"""PyMilo modules."""
from .reserver_func import does_package_exist, generate_template_setup_py
from .util import is_platform_linux
from os import environ, path, getcwd, remove
from shutil import rmtree
from sys import executable
from subprocess import check_output, CalledProcessError

class Uploader:
    """
    The Reserver Uploader class reserves a package name by uploading a template repo to pypi account.

    >>> uploader = Uploader(API_TOKEN, is_test_pypi_account = True) # API_TOKEN refers to pypi(or test pypi)'s account api.
    >>> uploader.upload_to_pypi(PACKAGE_NAME) # uploads package to the given test pypi account.
    """

    def __init__(self, api_token, is_test_pypi_account = False ):
        """
        Initialize the Reserver Uploader instance.

        :param api_token: pypi account's api token
        :type api_token: str
        :param is_test_pypi_account: indicates the given api_token is for a test.pypi account or not.
        :type is_test_pypi_account: bool
        :return: an instance of the Reserver Uploader
        """
        self.username = "__token__"
        self.password = api_token
        self.test_pypi = is_test_pypi_account
