# -*- coding: utf-8 -*-
"""Utility functions."""

from hashlib import sha256
from time import time


def get_random_name():
    """
    Generate a random str based on current timestamp.

    :return: str
    """
    return sha256(str(time()).encode("utf-8")).hexdigest()
