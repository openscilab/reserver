# -*- coding: utf-8 -*-
"""Functions."""
from requests import get 
from .reserver_param import PYPI_TEST_URL, PYPI_MAIN_URL

def does_package_exist(suggested_name, test_pypi):
    if not isinstance(suggested_name, str):
        suggested_name = str(suggested_name)
    if test_pypi:
        url = PYPI_TEST_URL + "/" + suggested_name + "/"
    else:
        url = PYPI_MAIN_URL + "/" + suggested_name + "/"
    response = get(url)
    return not response.status_code == 404
