# -*- coding: utf-8 -*-
"""Reserver modules."""
import chardet
from re import sub
from sys import executable
from os import environ, path, getcwd, remove
from .util import has_named_parameter, remove_dir
from subprocess import check_output, CalledProcessError
from .reserver_func import does_package_exist, generate_template_setup_py


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
        :type names: vararg
        :return: Number of successfully reserved packages
        """
        reserved_successfully = 0
        if user_params_path == None:
            for name in names:
                if self.upload(name):
                    reserved_successfully += 1
        elif isinstance(user_params_path, str):
            for name in names:
                if self.upload(name, user_parameters=user_params_path):
                    reserved_successfully += 1
        elif isinstance(user_params_path, list):
            if len(user_params_path) == 1:
                for name in names:
                    if self.upload(name, user_parameters=user_params_path[0]):
                        reserved_successfully += 1
            elif len(user_params_path) == len(names):
                for index, name in enumerate(names):
                    if self.upload(name, user_parameters=user_params_path[index]):
                        reserved_successfully += 1
            else:
                raise ReserverBaseError(UNEQUAL_PARAM_NAME_LENGTH_ERROR)
        return reserved_successfully

    def upload(self, package_name, user_parameters=None):
        """
        Upload a template package to pypi or test_pypi.

        :param package_name: package name
        :type package_name: str
        :param user_parameters: user-customized package parameters
        :type user_parameters: dict
        :return: True if the package is successfully reserved, False otherwise
        """
        if does_package_exist(package_name, self.test_pypi):
            print("This package already exists in PyPI.")
            return False

        if user_parameters != None:
            user_parameters = read_json(user_parameters)
        
        generate_template_setup_py(package_name, user_parameters)

        environ["TWINE_USERNAME"] = self.username
        environ["TWINE_PASSWORD"] = self.password

        generated_setup_file_path = path.join(getcwd(), package_name + "_setup.py")
        generated_package_folder = path.join(getcwd(), package_name)
        package_name_replaced = sub('-', '_', package_name)
        generated_egginfo_file_path = path.join(getcwd(), package_name_replaced + ".egg-info")
        generated_built_folder = path.join(getcwd(), "build")
        generated_dist_folder = path.join(getcwd(), "dist")
        generated_tar_gz_file = path.join(generated_dist_folder, "*.tar.gz")
        generated_wheel_file = path.join(generated_dist_folder, "*.whl")
        # prevent from uploading any other previously build library in this path.
        if path.exists(generated_dist_folder):
            remove_dir(generated_dist_folder)

        commands = [executable + " " + generated_setup_file_path + " sdist bdist_wheel "]
        if self.test_pypi:
            commands += [
                executable + " -m twine upload --repository testpypi " + generated_tar_gz_file,
                executable + " -m twine upload --repository testpypi " + generated_wheel_file,
            ]
        else:
            commands += [
                executable + " -m twine upload --verbose " + generated_tar_gz_file,
                executable + " -m twine upload --verbose " + generated_wheel_file,
            ]
        # Run the commands
        publish_failed = False
        error = None
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
                except:
                    error = error.decode('utf-8')
                if command == commands[-2]:
                    if "403" in error and "Invalid or non-existent authentication information" in error:
                        error = "Invalid or non-existent authentication information(PyPI API Key)."
                    if "400" in error and "too similar to an existing project" in error:
                        error = "Given package name is too similar to an existing project in PyPI."
                    if "400" in error and "isn't allowed." in error:
                        error = "Given package name has conflict with the module name of a previously taken package."
                    if "400" in error and "isn't allowed (conflict with Python Standard Library" in error:
                        error = "Given package name has conflict with Python Standard Library module name."
                break

        if "TWINE_USERNAME" in environ:
            environ.pop("TWINE_USERNAME")
        if "TWINE_PASSWORD" in environ:
            environ.pop("TWINE_PASSWORD")

        remove(generated_setup_file_path)
        remove_dir(generated_package_folder)
        remove_dir(generated_egginfo_file_path)
        remove_dir(generated_built_folder)
        remove_dir(generated_dist_folder)

        if publish_failed:
            print(f"Publish to PyPI failed because of: ", error)
            return False
        else:
            print("Congratulations! You have successfully reserved the PyPI package: ", package_name)
            return True
