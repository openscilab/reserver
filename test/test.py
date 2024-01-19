from reserver import Uploader
import os 
test_pypi_token = os.environ.get("TEST_PYPI_PASSWORD")
    
def test():

    # test reserved name
    uploader = Uploader(test_pypi_token, is_test_pypi_account= True)
    uploader.upload_to_pypi("numpy")

    # test not reserved name -> correct credentials
    # uploader = Uploader(test_pypi_token, is_test_pypi_account= True)
    # uploader.upload_to_pypi(get_random_name())

    # test not reserved name -> wrong credentials
    # wrong_pypi_token = "pypi-wrong-api-token"
    # uploader = Uploader(wrong_pypi_token, is_test_pypi_account= True)
    # uploader.upload_to_pypi(get_random_name())
