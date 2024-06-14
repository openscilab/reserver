# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
### Changed
## [0.2] - 2024-06-17
### Added
- `CLI` handler
- `Python 3.6` support
- `has_named_parameter` method in `util.py`
- `feature_request.yml` template
- `config.yml` for issue template
- `batch_upload` method in `PyPIUploader`
- `SECURITY.md`
### Changed
- `upload` method in `reserver_obj.py`
- `does_package_exist` method in `reserver_func.py`
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

[Unreleased]: https://github.com/openscilab/reserver/compare/v0.2...dev
[0.2]: https://github.com/openscilab/reserver/compare/v0.1...v0.2
[0.1]: https://github.com/openscilab/reserver/compare/0ae5bb9...v0.1