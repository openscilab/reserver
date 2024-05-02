# -*- coding: utf-8 -*-
"""utility module."""
from inspect import signature


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
