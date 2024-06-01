# -*- coding: utf-8 -*-
"""utility module."""
from inspect import signature
import os
import shutil


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
