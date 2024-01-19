# -*- coding: utf-8 -*-
"""Utility functions."""

from platform import system
from hashlib import sha256
from time import time


def is_platform_linux():
    """
    Check whether current platform is linux or not.

    :return: bool
    """
    return system() == "Linux"


def get_random_name():
    """
    Generate a random str based on current timestamp.

    :return: str
    """
    return sha256(str(time()).encode("utf-8")).hexdigest()
