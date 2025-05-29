# -*- coding: utf-8 -*-
"""Reserver modules."""
import chardet
import platform
from sys import executable
from os import environ, path, getcwd
from .errors import ReserverBaseError
from .functions import generate_template_setup_py
from subprocess import check_output, CalledProcessError
from .params import UNEQUAL_PARAM_NAME_LENGTH_ERROR, REVOKE_TOKEN_MESSAGE
from .utils import has_named_parameter, remove_dir, read_json


class PyPIUploader:
    """
    The Reserver PyPIUploader class reserves a package name by uploading a template repo to pypi account.

    >>> uploader = PyPIUploader(API_TOKEN, is_test_pypi_account = True) # API_TOKEN refers to pypi(or test pypi)'s account api.
    >>> uploader.upload_to_pypi(PACKAGE_NAME) # uploads package to the given test pypi account.
    """

    def __init__(self, api_token, test_pypi=False):
        """
        Initialize the Reserver PyPIUploader instance.

        :param api_token: pypi account's api token
        :type api_token: str
        :param test_pypi: indicates the given api_token is for a test.pypi account or not.
        :type test_pypi: bool
        :return: an instance of the Reserver PyPIUploader
        """
        self.username = "__token__"
        self.password = api_token
        self.test_pypi = test_pypi

    def batch_upload(self, names, user_params_path=None):
        """
        Upload batch of package names to PyPI.

        :param names: packages' names
        :type names: list
        :param user_params_path: path to user-defined packages' parameters
        :type user_params_path: None | str | list
        :return: Number of successfully reserved packages
        """
        reserved_successfully = 0
        if user_params_path is None:
            for name in names:
                if self.upload(name, show_warning=False):
                    reserved_successfully += 1
        elif isinstance(user_params_path, str):
            for name in names:
                if self.upload(name, user_parameters=user_params_path, show_warning=False):
                    reserved_successfully += 1
        elif isinstance(user_params_path, list):
            if len(user_params_path) == 1:
                for name in names:
                    if self.upload(name, user_parameters=user_params_path[0], show_warning=False):
                        reserved_successfully += 1
            elif len(user_params_path) == len(names):
                for index, name in enumerate(names):
                    if self.upload(name, user_parameters=user_params_path[index], show_warning=False):
                        reserved_successfully += 1
            else:
                raise ReserverBaseError(UNEQUAL_PARAM_NAME_LENGTH_ERROR)

        if reserved_successfully > 0 and not self.test_pypi:
            print(REVOKE_TOKEN_MESSAGE)

        return reserved_successfully

    def upload(self, package_name, user_parameters=None, show_warning=True):
        """
        Upload a template package to pypi or test_pypi.

        :param package_name: package name
        :type package_name: str
        :param user_parameters: json file or path to the .json file containing user-defined package parameters
        :type user_parameters: str | dict
        :param show_warning: Whether to show the PyPI token security warning
        :type show_warning: bool
        :return: True if the package is successfully reserved, False otherwise
        """
        if not isinstance(user_parameters, dict) and user_parameters is not None:
            user_parameters = read_json(user_parameters)

        environ["TWINE_USERNAME"] = self.username
        environ["TWINE_PASSWORD"] = self.password

        package_path = path.join(getcwd(), package_name)
        generated_dist_folder = path.join(package_path, "dist")
        generated_tar_gz_file = path.join(generated_dist_folder, "*.tar.gz")
        generated_wheel_file = path.join(generated_dist_folder, "*.whl")
        # prevent from uploading any other previously build library in this path.
        remove_dir(generated_dist_folder)
        build_command = f'"{executable}" -m build "{package_path}" --sdist --wheel'
        if platform.system() == "Windows":
            commands = [f'{build_command} > nul 2>&1']
        else:
            commands = [f'{build_command} > /dev/null 2>&1']
        if self.test_pypi:
            commands += [
                f'"{executable}" -m twine upload --repository testpypi "{generated_tar_gz_file}"',
                f'"{executable}" -m twine upload --repository testpypi "{generated_wheel_file}"',
            ]
        else:
            commands += [
                f'"{executable}" -m twine upload "{generated_tar_gz_file}"',
                f'"{executable}" -m twine upload "{generated_wheel_file}"',
            ]
        # Run the commands
        publish_failed = False
        error = None

        generate_template_setup_py(package_name, user_parameters)

        for command in commands:
            try:
                if has_named_parameter(check_output, "text"):
                    check_output(command, shell=True, text=True)
                else:
                    check_output(command, shell=True)
            except CalledProcessError as e:
                publish_failed = True
                error = e.output
                try:
                    error = error.decode(chardet.detect(error)['encoding'])
                except BaseException:
                    error = error.decode('utf-8')

        # remove credential from env variables
        if "TWINE_USERNAME" in environ:
            environ.pop("TWINE_USERNAME")
        if "TWINE_PASSWORD" in environ:
            environ.pop("TWINE_PASSWORD")
        # remove previously generated files
        remove_dir(package_path)

        if publish_failed:
            print(f"Publish to PyPI failed because of: ", error)
            return False
        else:
            print("Congratulations! You have successfully reserved the PyPI package: ", package_name)
            if show_warning and not self.test_pypi:
                print(REVOKE_TOKEN_MESSAGE)
            return True
