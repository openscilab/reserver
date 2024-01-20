# -*- coding: utf-8 -*-
"""Reserver modules."""
from .reserver_func import does_package_exist, generate_template_setup_py
from .util import is_platform_linux
from os import environ, path, getcwd, remove
from shutil import rmtree
from sys import executable
from subprocess import check_output, CalledProcessError


class Uploader:
    """
    The Reserver Uploader class reserves a package name by uploading a template repo to pypi account.

    >>> uploader = Uploader(API_TOKEN, is_test_pypi_account = True) # API_TOKEN refers to pypi(or test pypi)'s account api.
    >>> uploader.upload_to_pypi(PACKAGE_NAME) # uploads package to the given test pypi account.
    """

    def __init__(self, api_token, is_test_pypi_account=False):
        """
        Initialize the Reserver Uploader instance.

        :param api_token: pypi account's api token
        :type api_token: str
        :param is_test_pypi_account: indicates the given api_token is for a test.pypi account or not.
        :type is_test_pypi_account: bool
        :return: an instance of the Reserver Uploader
        """
        self.username = "__token__"
        self.password = api_token
        self.test_pypi = is_test_pypi_account

    def upload_to_pypi(self, package_name):
        """
        Upload a template package to pypi or test_pypi.

        :param package_name: package name
        :type package_name: str
        :param to_test_pypi: boolean flag to indicate uploading to pypi test or not
        :type to_test_pypi: bool
        :return: None
        """
        if does_package_exist(package_name, self.test_pypi):
            print("This package already exists in PyPI.")
            return
        generate_template_setup_py(package_name)

        environ["TWINE_USERNAME"] = self.username
        environ["TWINE_PASSWORD"] = self.password

        generated_setup_file_path = path.join(getcwd(), package_name + "_setup.py")
        generated_egginfo_file_path = path.join(getcwd(), package_name + ".egg-info")
        generated_built_folder = path.join(getcwd(), "build")
        generated_dist_folder = path.join(getcwd(), "dist")
        generated_tar_gz_file = path.join(generated_dist_folder, "*.tar.gz")
        generated_wheel_file = path.join(generated_dist_folder, "*.whl")
        # prevent from uploading any other previously build library in this path.
        if path.exists(generated_dist_folder):
            rmtree(generated_dist_folder)

        commands = [
            executable + " -m pip install --upgrade pip",
            executable + " -m pip install setuptools wheel twine",
            executable + " -m pip install --upgrade setuptools",
            executable + " " + generated_setup_file_path + " sdist bdist_wheel "]
        if is_platform_linux():
            # handle the place build files get generated.
            # pip install "importlib-metadata<5.0" for
            # https://bobbyhadz.com/blog/entrypoints-object-has-no-attribute-get
            commands.append(executable + " -m pip install \"importlib-metadata<5.0\"")
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
            print("running this command: ", command)
            try:
                check_output(command, shell=True, text=True)
            except CalledProcessError as e:
                publish_failed = True
                error = e.output

        if publish_failed:
            print(f"Publish to PyPI failed because of: ", error)
        else:
            print("Congratulations! You have successfully reserved the PyPI package: ", package_name)
        remove(generated_setup_file_path)
        rmtree(generated_egginfo_file_path)
        rmtree(generated_built_folder)
        rmtree(generated_dist_folder)
