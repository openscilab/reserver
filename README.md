<div align="center">
    <img src="https://github.com/openscilab/reserver/raw/main/otherfiles/logo.png" width="300" height="300">
    <br/>
    <br/>
    <a href="https://codecov.io/gh/openscilab/reserver">
        <img src="https://codecov.io/gh/openscilab/reserver/branch/main/graph/badge.svg" alt="Codecov"/>
    </a>
    <a href="https://badge.fury.io/py/reserver">
        <img src="https://badge.fury.io/py/reserver.svg" alt="PyPI version" height="18">
    </a>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3">
    </a>
    <a href="https://discord.gg/RD2y6SGuY3">
        <img src="https://img.shields.io/discord/1064533716615049236.svg" alt="Discord Channel">
    </a>
</div>

----------

## Table of contents

* [Overview](https://github.com/openscilab/reserver#overview)
* [Installation](https://github.com/openscilab/reserver#installation)
* [Usage](https://github.com/openscilab/reserver#usage)
* [Issues & Bug Reports](https://github.com/openscilab/reserver#issues--bug-reports)
* [Todo](https://github.com/openscilab/reserver/blob/main/TODO.md)
* [Contribution](https://github.com/openscilab/reserver/blob/main/.github/CONTRIBUTING.md)
* [Authors](https://github.com/openscilab/reserver/blob/main/AUTHORS.md)
* [License](https://github.com/openscilab/reserver/blob/main/LICENSE)
* [Show Your Support](https://github.com/openscilab/reserver#show-your-support)
* [Changelog](https://github.com/openscilab/reserver/blob/main/CHANGELOG.md)
* [Code of Conduct](https://github.com/openscilab/reserver/blob/main/.github/CODE_OF_CONDUCT.md)


## Overview
<p align="justify">
Reserver is an open source Python package that provides functionality to easily reserve a pypi package name. Have an idea? Reserve the package name instantly before it gets taken!
</p>
<table>
    <tr>
        <td align="center">PyPI Counter</td>
        <td align="center">
            <a href="http://pepy.tech/project/reserver">
                <img src="http://pepy.tech/badge/reserver">
            </a>
        </td>
    </tr>
    <tr>
        <td align="center">Github Stars</td>
        <td align="center">
            <a href="https://github.com/openscilab/reserver">
                <img src="https://img.shields.io/github/stars/openscilab/reserver.svg?style=social&label=Stars">
            </a>
        </td>
    </tr>
</table>
<table>
    <tr> 
        <td align="center">Branch</td>
        <td align="center">main</td>
        <td align="center">dev</td>
    </tr>
    <tr>
        <td align="center">CI</td>
        <td align="center">
            <img src="https://github.com/openscilab/reserver/workflows/CI/badge.svg?branch=main">
        </td>
        <td align="center">
            <img src="https://github.com/openscilab/reserver/workflows/CI/badge.svg?branch=dev">
            </td>
    </tr>
</table>


## Installation

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)
- Run `pip install reserver==0.1`
### Source code
- Download [Version 0.1](https://github.com/openscilab/reserver/archive/v0.1.zip) or [Latest Source](https://github.com/openscilab/reserver/archive/dev.zip)
- Run `pip install .`

## Usage
### Secure your desired PyPI package name!
```python
from reserver import Uploader
uploader = Uploader(PYPI_API_TOKEN, is_test_pypi_account= False)
uploader.upload_to_pypi("CONSIDERED_NAME_FOR_YOUR_PACKAGE")
```

## Issues & bug reports

Just fill an issue and describe it. We'll check it ASAP! or send an email to [info@openscilab.com](mailto:info@openscilab.com "info@openscilab.com"). 

- Please complete the issue template
 
You can also join our discord server

<a href="https://discord.gg/RD2y6SGuY3">
    <img src="https://img.shields.io/discord/1064533716615049236.svg?style=for-the-badge" alt="Discord Channel">
</a>


## Show Your Support


### Star this repo

Give a ⭐️ if this project helped you!

### Donate to our project
If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .			

<a href="https://openscilab.com/#donation" target="_blank"><img src="https://github.com/openscilab/reserver/raw/main/otherfiles/donation.png" height="90px" width="270px" alt="Reserver Donation"></a>