<div align="center">
    <img src="https://github.com/openscilab/reserver/raw/main/otherfiles/reserver.png" width="300" height="300">
    <br/>
    <br/>
    <a href="https://codecov.io/gh/openscilab/reserver"><img src="https://codecov.io/gh/openscilab/reserver/branch/main/graph/badge.svg" alt="Codecov"/></a>
    <a href="https://badge.fury.io/py/reserver"><img src="https://badge.fury.io/py/reserver.svg" alt="PyPI version" height="18"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
    <a href="https://discord.gg/RD2y6SGuY3"><img src="https://img.shields.io/discord/1064533716615049236.svg" alt="Discord Channel"></a>
</div>

----------

## Disclaimer 
<p align="justify">
⚠️The intention of this package is facilitating the reservation of package names on PyPI for legitimate and appropriate purposes. We explicitly disclaim any responsibility for the misuse or spamming of this tool, particularly in the excessive reservation of package names. Users are advised to be cautious and ensure the  legitimate use of this package to avoid potential consequences such as the suspension of their PyPI account. By using this package, users acknowledge and agree to these terms.
</p>

## Overview
<p align="justify">
Reserver is an open source Python package that offers the ability to quickly reserve a PyPI package name. Got a notion? Before it's taken, immediately reserve the product name!
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
            <img src="https://github.com/openscilab/reserver/actions/workflows/test.yml/badge.svg?branch=main">
        </td>
        <td align="center">
            <img src="https://github.com/openscilab/reserver/actions/workflows/test.yml/badge.svg?branch=dev">
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

```python
from reserver import PyPIUploader
uploader = PyPIUploader(PYPI_API_TOKEN, test_pypi= False)
uploader.upload("CONSIDERED_NAME_FOR_YOUR_PACKAGE")
```

## Issues & bug reports

Just fill an issue and describe it. We'll check it ASAP! or send an email to [reserver@openscilab.com](mailto:reserver@openscilab.com "reserver@openscilab.com"). 

- Please complete the issue template
 
You can also join our discord server

<a href="https://discord.gg/RD2y6SGuY3"><img src="https://img.shields.io/discord/1064533716615049236.svg?style=for-the-badge" alt="Discord Channel"></a>

## References

1. box: <a href="https://www.flaticon.com/free-icons/box" title="box icons">Box icons created by Good Ware - Flaticon</a>
2. reserve plate: <a href="https://www.flaticon.com/free-icons/reserved" title="reserved icons">Reserved icons created by Freepik - Flaticon</a>


## Show your support

### Star this repo
Give a ⭐️ if this project helped you!

### Donate to our project
If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .			

<a href="https://openscilab.com/#donation" target="_blank"><img src="https://github.com/openscilab/reserver/raw/main/otherfiles/donation.png" height="90px" width="270px" alt="Reserver Donation"></a>
