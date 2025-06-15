# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Dummy `README.md` file for the template package
- Warning message regarding PyPI token revoke
- `generate_template_pyproject_toml` in `functions.py`
### Changed
- `batch_upload` method in `uploader.py`
- `upload` method in `uploader.py`
- `generate_template_setup_py` in `functions.py`
- package build command in `publish_pypi.yml`
### Removed
- Python 3.6 support
## [0.4] - 2025-01-08
### Added
- default reviewer added in `dependabot.yml`
- `ReserverBaseError` added in `reserver/__init__.py`
### Changed
- `upload` method in `reserver_obj.py`
- `README.md` updated
- `AUTHORS.md` updated
- GitHub actions are limited to the `dev` and `main` branches
- `generate_template_setup_py` function in `reserver_func.py`
- `Python 3.13` added to `test.yml`
### Removed
- `does_package_exist` function in `reserver_func.py`
## [0.3] - 2024-08-28
### Added
- CLI tests added
- `param` arg in CLI Handler
- more testcases in conflict cases
- `batch_upload` tests
- `read_json` function in `util.py`
### Changed
- `README.md` updated
- `upload` method in `reserver_obj.py`
- `batch_upload` method `reserver_obj.py`
## [0.2] - 2024-06-17
### Added
- `CLI` handler
- `Python 3.6` support
- `has_named_parameter` function in `util.py`
- `feature_request.yml` template
- `config.yml` for issue template
- `batch_upload` method in `PyPIUploader`
- `SECURITY.md`
### Changed
- `upload` method in `reserver_obj.py`
- `does_package_exist` function in `reserver_func.py`
- `test.yml` for `Python 3.6` support
- Logo updated
- Bug report template modified
- `Uploader` changed to `PyPIUploader`
- `README.md` modified
## [0.1] - 2024-02-07
### Added
- `Uploader` class
- Check package name existence
- Upload template package to test PyPI
- Upload template package to PyPI
- Generate template package for a given name
- Handle similar name existence in PyPI
- Handle issue with "-" character `.egginfo` file name

[Unreleased]: https://github.com/openscilab/reserver/compare/v0.4...dev
[0.4]: https://github.com/openscilab/reserver/compare/v0.3...v0.4
[0.3]: https://github.com/openscilab/reserver/compare/v0.2...v0.3
[0.2]: https://github.com/openscilab/reserver/compare/v0.1...v0.2
[0.1]: https://github.com/openscilab/reserver/compare/0ae5bb9...v0.1
