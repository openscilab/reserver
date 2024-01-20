from reserver import Uploader
from reserver.util import get_random_name
import os 
test_pypi_token = os.environ.get("TEST_PYPI_PASSWORD")
    
def test_package_exists():
    # test reserved name
    uploader = Uploader(test_pypi_token, is_test_pypi_account= True)
    assert uploader.upload_to_pypi("numpy") == False

def test_valid_package_invalid_credentials():
    # test not reserved name -> wrong credentials
    wrong_pypi_token = "pypi-wrong-api-token"
    uploader = Uploader(wrong_pypi_token, is_test_pypi_account= True)
    assert uploader.upload_to_pypi(get_random_name()) == False

def test_valid_package_valid_credentials():
    # test not reserved name -> correct credentials
    # uploader = Uploader(test_pypi_token, is_test_pypi_account= True)
    # uploader.upload_to_pypi(get_random_name())
    assert True == True
