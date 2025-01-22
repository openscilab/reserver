# -*- coding: utf-8 -*-
"""utility module."""
import os
import json
import shutil
from inspect import signature
from .errors import ReserverBaseError
from .params import INVALID_CONFIG_FILE_NAME_ERROR, PARAM_FILE_DOES_NOT_EXIST_ERROR


def has_named_parameter(func, param_name):
    """
    Check whether the given function has a parameter named param_name or not.

    :param func: function to check it's params
    :type func: function
    :param param_name: parameter's name
    :type param_name: str

    :return: boolean
    """
    _signature = signature(func)
    parameter_names = [p.name for p in _signature.parameters.values()]
    return param_name in parameter_names


def remove_dir(dirpath):
    """
    Check whether the given path exists or not and remove it if it does.

    :param dirpath: path to the directory
    :type dirpath: str

    :return: None
    """
    if os.path.exists(dirpath) and os.path.isdir(dirpath):
        shutil.rmtree(dirpath)


def read_json(file_name):
    """
    Read the json file and return the python obj of it.

    :param file_name: name of the .json file
    :type file_name: str
    :return: obj
    """
    if not isinstance(file_name, str):
        raise ReserverBaseError(INVALID_CONFIG_FILE_NAME_ERROR)
    if os.path.isfile(file_name):
        config_file = open(file_name)
        return json.load(config_file)
    else:
        raise ReserverBaseError(PARAM_FILE_DOES_NOT_EXIST_ERROR)
