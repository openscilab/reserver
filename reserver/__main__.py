# -*- coding: utf-8 -*-
"""Reserver main."""
import argparse
from art import tprint
from .reserver_param import RESERVER_VERSION
from .reserver_func import reserver_help
from .reserver_obj import PyPIUploader


def main():
    """
    CLI main function.

    :return: None
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--name',
        nargs='+',
        help='Name(s) to get reserved',
        required=True
    )
    parser.add_argument(
        '--token',
        help='The token for (main|test) PyPI account',
        required=True
    )
    parser.add_argument('--test', action='store_true', help='Flag identifying test account or not')
    parser.add_argument('--version', help="version", action='store_true', default=False)
    parser.add_argument('-v', help="version", action='store_true', default=False)
    args = parser.parse_known_args()[0]
    if args.version or args.v:
        print(RESERVER_VERSION)
    names = args.name
    test_pypi = True if args.test else False
    pypi_token = args.token
    if names and pypi_token:
        PyPIUploader(pypi_token, test_pypi).batch_upload(names)
    else:
        tprint("Reserver")
        tprint("V:" + RESERVER_VERSION)
        reserver_help()
        parser.print_help()


if __name__ == "__main__":
    main()
