# -*- coding: utf-8 -*-
"""Reserver Functions."""
from requests import get
from .reserver_param import PYPI_TEST_URL, PYPI_MAIN_URL


def does_package_exist(suggested_name, test_pypi):
    """
    Check whether a package with the given name exists or not.

    :param suggested_name: given name to search in pypi(or test.pypi)
    :type suggested_name: str
    :param test_pypi: indicates to search in test.pypi or not
    :type test_pypi: bool
    :return: whether given name does exist in the pypi or not(as a boolean value)
    """
    if not isinstance(suggested_name, str):
        suggested_name = str(suggested_name)
    if test_pypi:
        url = PYPI_TEST_URL + "/" + suggested_name + "/"
    else:
        url = PYPI_MAIN_URL + "/" + suggested_name + "/"
    response = get(url, timeout=5)
    return not response.status_code == 404


def generate_template_setup_py(package_name):
    """
    Generate a template `setup.py` file for given package name.

    :param package_name: given name to generate template `setup.py` for it.
    :type package_name: str
    :return: None
    """
    setup_py_content = """
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# invalid email
# download url
# url
# project urls

setup(
    name =""" + "\"" + package_name + "\"" + """,
    packages=[],
    version='0.0.0',
    description='DESCRIPTION',
    long_description="LONG_DESCRIPTION",
    long_description_content_type='text/markdown',
    author='Development Team',
    author_email='test@test.com',
    url='https://url.com',
    download_url='https://download_url.com',
    keywords="python3 python",
    project_urls={
            'Source': 'https://github.com/source',
    },
    install_requires="",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
    ],
    license='MIT',
)

    """
    with open(package_name + "_setup.py", "w+") as f:
        f.writelines(setup_py_content)
