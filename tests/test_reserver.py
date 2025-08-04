import os
import pytest
from reserver import PyPIUploader
from reserver.functions import get_random_name

pypi_token = os.environ.get("TWINE_PASSWORD")
test_pypi_token = os.environ.get("TWINE_TEST_PASSWORD")

def test_package_exists():
    # test reserved name
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.upload("numpy") == False

def test_standard_module_conflict():
    # try to reserve a standard python library module
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.upload("os") == False

def test_valid_package_invalid_credentials():
    # test not reserved name -> wrong credentials
    uploader = PyPIUploader("pypi-wrong-api-token", test_pypi=True)
    assert uploader.upload(get_random_name()) == False

@pytest.mark.end_to_end
def test_valid_package_valid_credentials():
    # test not reserved name -> correct credentials
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.upload(get_random_name()) == True

def test_module_conflict():
    # try to reserve a name which conflicts with the module name of a previously taken package (the taken package itself has a different name, but it's module name has conflict)."
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.upload("freeze") == False

def test_batch_packages_names():
    # test batch of package names
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.batch_upload(["numpy", "scikit-learn"]) == 0

@pytest.mark.end_to_end
def test_batch_upload():
    # try to reserve two non taken package names with per package custom setup.py parameters
    # make sure you are in "tests" directory
    tests_dir = os.path.join(os.getcwd(), "tests")
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.batch_upload(
        [get_random_name(), get_random_name() + get_random_name()],
        [os.path.join(tests_dir, "config.json"), os.path.join(tests_dir,"config2.json")]
        ) == 2
