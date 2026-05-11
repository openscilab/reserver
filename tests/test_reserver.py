import os
from pathlib import Path
import pytest
from reserver import PyPIUploader, ReserverBaseError
from reserver.functions import get_random_name

# Dependabot (and fork) PRs do not receive Actions secrets; skip actual reservation tests
# that need a real Test PyPI token. Same tests still run on push / in-repo PRs.
requires_test_pypi_token = pytest.mark.skipif(
    not (os.environ.get("TWINE_TEST_PASSWORD") or "").strip(),
    reason="TWINE_TEST_PASSWORD not set (e.g. Dependabot PR)",
)

test_pypi_token = os.environ.get("TWINE_TEST_PASSWORD")


@requires_test_pypi_token
def test_taken_name():
    # Reserving a name that already exists on (test) PyPI must fail.
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.upload("numpy") == False


@requires_test_pypi_token
def test_stdlib_name():
    # Reserving a Python standard-library module name must fail.
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.upload("os") == False


def test_wrong_token():
    # A syntactically-valid but incorrect token must cause upload to fail.
    uploader = PyPIUploader("pypi-wrong-api-token", test_pypi=True)
    assert uploader.upload(get_random_name()) == False


@pytest.mark.end_to_end
@requires_test_pypi_token
def test_upload_success():
    # Happy path: free name + correct token -> successful reservation.
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.upload(get_random_name()) == True


@requires_test_pypi_token
def test_module_conflict():
    # Name collides with the importable module of a *different* existing
    # package (e.g. project "X" ships module "freeze"). PyPI blocks this.
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.upload("freeze") == False


@requires_test_pypi_token
def test_batch_all_taken():
    # Batch of already-taken names -> zero successful reservations.
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.batch_upload(["numpy", "scikit-learn"]) == 0


@pytest.mark.parametrize("bad_token", [None, "", "   ", 123, b"pypi-bytes"])
def test_invalid_token(bad_token):
    # The library must refuse construction without a real token so callers
    # cannot accidentally hit the network with empty credentials.
    with pytest.raises(ReserverBaseError):
        PyPIUploader(bad_token, test_pypi=True)


def test_cwd_untouched(tmp_path, monkeypatch):
    # Regression: upload() must NOT write into or delete a directory in the
    # user's CWD that happens to share the target package name.
    target_name = "numpy"  # taken -> twine will fail, exercising cleanup
    victim = tmp_path / target_name
    victim.mkdir()
    marker = victim / "marker.txt"
    marker_content = "user data - must not be touched"
    marker.write_text(marker_content, encoding="utf-8")

    monkeypatch.chdir(tmp_path)

    # Snapshot the environment *before* the call. Reserver must leave it
    # untouched (credentials are injected only into the subprocess env).
    env_before = dict(os.environ)

    # Fake token is enough; we assert on cleanup, not on upload outcome details.
    uploader = PyPIUploader("pypi-fake-token-for-cwd-test", test_pypi=True)
    assert uploader.upload(target_name) == False

    assert Path.cwd() == tmp_path
    assert victim.is_dir()
    assert marker.exists()
    assert marker.read_text(encoding="utf-8") == marker_content
    assert [p.name for p in victim.iterdir()] == ["marker.txt"]
    assert dict(os.environ) == env_before


@pytest.mark.end_to_end
@requires_test_pypi_token
def test_batch_success():
    # Batch happy path: two free names with per-package custom params.
    # Invoker must be in the repo root so that "tests/" is resolvable.
    tests_dir = os.path.join(os.getcwd(), "tests")
    uploader = PyPIUploader(test_pypi_token, test_pypi=True)
    assert uploader.batch_upload(
        [get_random_name(), get_random_name() + get_random_name()],
        [os.path.join(tests_dir, "config.json"), os.path.join(tests_dir, "config2.json")]
    ) == 2
