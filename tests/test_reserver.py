from reserver import Uploader
import os 
test_pypi_token = os.environ.get("TEST_PYPI_PASSWORD")
    
def test_reserver():

    # test reserved name
    uploader = Uploader(test_pypi_token, is_test_pypi_account= True)
    uploader.upload_to_pypi("numpy")
