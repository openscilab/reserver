# -*- coding: utf-8 -*-
"""Reserver functions."""
from requests import get
from .reserver_param import PYPI_TEST_URL, PYPI_MAIN_URL
from hashlib import sha256
from time import time
from os import mkdir, rmdir


def get_random_name():
    """
    Generate a random str based on current timestamp.

    :return: str
    """
    return sha256(str(time()).encode("utf-8")).hexdigest()


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
    packages=[""" + "\"" + package_name + "\"" + "," + """],
    version='0.0.0',
    description='This name has been reserved using Reserver',
    long_description=\"\"\"
    This name has been reserved using [Reserver](https://github.com/openscilab/reserver).
    \"\"\",
    long_description_content_type='text/markdown',
    author='Development Team',
    author_email='test@test.com',
    url='https://url.com',
    download_url='https://download_url.com',
    keywords="python3 python reserve reserver reserved",
    project_urls={
            'Source': 'https://github.com/source',
    },
    install_requires="",
    python_requires='>=3.6',
    classifiers=[
        \'Development Status :: 1 - Planning\',
        \'Programming Language :: Python :: 3.6\',
        \'Programming Language :: Python :: 3.7\',
        \'Programming Language :: Python :: 3.8\',
        \'Programming Language :: Python :: 3.9\',
        \'Programming Language :: Python :: 3.10\',
        \'Programming Language :: Python :: 3.11\',
        \'Programming Language :: Python :: 3.12\',
    ],
    license='MIT',
)

"""
    with open(package_name + "_setup.py", "w+") as f:
        f.writelines(setup_py_content)

    try:
        mkdir(package_name)
    except FileExistsError:
        rmdir(package_name)
        mkdir(package_name)
    with open(package_name + "/__init__.py", "w") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write("\"\"\"" + package_name + " modules." + "\"\"\"")
