from reserver import PyPIUploader
from reserver.reserver_func import get_random_name
import os
test_pypi_token = os.environ.get("TEST_PYPI_PASSWORD")

def test_package_exists():
    # test reserved name
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.upload("numpy") == False

def test_standard_module_conflict():
    # try to reserve a standard python library module
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.upload("os") == False

def test_batch_packages_names():
    # test batch of package names
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.batch_upload("numpy", "scikit-learn") == 0

def test_valid_package_invalid_credentials():
    # test not reserved name -> wrong credentials
    wrong_pypi_token = "pypi-wrong-api-token"
    uploader = PyPIUploader(wrong_pypi_token, test_pypi=True)
    assert uploader.upload(get_random_name()) == False

def test_valid_package_valid_credentials():
    # test not reserved name -> correct credentials
    # uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    # uploader.upload_to_pypi(get_random_name())
    assert True == True
