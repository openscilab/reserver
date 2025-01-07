# -*- coding: utf-8 -*-
"""Reserver functions."""
import re
from time import time
from hashlib import sha256
from os import mkdir, rmdir
from .reserver_param import PACKAGE_PARAMETERS, VALIDATIONS, OVERVIEW
from .reserver_param import INVALID_PACKAGE_PARAMETER_NAME_ERROR, INVALID_PACKAGE_PARAMETER_VALUE_ERROR
from .reserver_errors import ReserverBaseError


def get_random_name():
    """
    Generate a random str based on current timestamp.

    :return: str
    """
    return sha256(str(time()).encode("utf-8")).hexdigest()


def get_package_parameter(parameter, user_parameters, regex=None):
    """
    Get the value for the associated package parameter.

    :param parameter: one of the customizable package parameters
    :type parameter: str
    :param user_parameters: user-customized package parameters
    :type user_parameters: dict
    :param regex: name of the regex to get applied
    :type regex: str
    :return: value of the associated parameter
    """
    if not user_parameters or parameter not in user_parameters:
        if parameter in PACKAGE_PARAMETERS:
            return PACKAGE_PARAMETERS[parameter]
        else:
            raise ReserverBaseError(INVALID_PACKAGE_PARAMETER_NAME_ERROR)
    if regex:
        if re.match(VALIDATIONS[regex], user_parameters[parameter]):
            return user_parameters[parameter]
        else:
            raise ReserverBaseError(INVALID_PACKAGE_PARAMETER_VALUE_ERROR.format(parameter=parameter, regex=regex))
    return user_parameters[parameter]


def generate_template_setup_py(package_name, user_parameters):
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
    description=""" + "\"" + get_package_parameter("description", user_parameters) + "\"" + """,
    long_description= \"This name has been reserved using [Reserver](https://github.com/openscilab/reserver).\",
    long_description_content_type='text/markdown',
    author=""" + "\"" + get_package_parameter("author", user_parameters) + "\"" + """,
    author_email=""" + "\"" + get_package_parameter("author_email", user_parameters, "email") + "\"" + """,
    url=""" + "\"" + get_package_parameter("url", user_parameters, "url") + "\"" + """,
    download_url=""" + "\"" + get_package_parameter("download_url", user_parameters, "url") + "\"" + """,
    keywords="python3 python reserve reserver reserved",
    project_urls={
            'Source':""" + "\"" + get_package_parameter("source", user_parameters, "url") + "\"" + """,
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
    license=""" + "\"" + get_package_parameter("license", user_parameters) + "\"" + """,
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


def reserver_help():
    """
    Print Reserver details.

    :return: None
    """
    print(OVERVIEW)
    print("Repo : https://github.com/openscilab/reserver")
    print("Webpage : https://openscilab.com/\n")
