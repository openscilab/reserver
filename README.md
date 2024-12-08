<div align="center">
    <img src="https://github.com/openscilab/reserver/raw/main/otherfiles/reserver.png" width="300" height="300">
    <br/>
    <br/>
    <a href="https://codecov.io/gh/openscilab/reserver"><img src="https://codecov.io/gh/openscilab/reserver/branch/main/graph/badge.svg" alt="Codecov"/></a>
    <a href="https://badge.fury.io/py/reserver"><img src="https://badge.fury.io/py/reserver.svg" alt="PyPI version"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
    <a href="https://discord.gg/RD2y6SGuY3"><img src="https://img.shields.io/discord/1064533716615049236.svg" alt="Discord Channel"></a>
</div>

----------

## Disclaimer 
**⚠️ Warning ⚠️**

<p align="justify">

The intention of this package is facilitating the reservation of package names on PyPI for legitimate and appropriate purposes. We explicitly disclaim any responsibility for the misuse or spamming of this tool, particularly in the excessive reservation of package names. Users are advised to be cautious and ensure the  legitimate use of this package to avoid potential consequences such as the suspension of their PyPI account. By using this package, users acknowledge and agree to these terms.
</p>

## Overview
<p align="justify">
Reserver is an open source Python package that offers the ability to quickly reserve a PyPI package name. Got a notion? Before it's taken, immediately reserve the product name!
</p>
<table>
    <tr>
        <td align="center">PyPI Counter</td>
        <td align="center">
            <a href="https://pepy.tech/projects/reserver">
                <img src="https://static.pepy.tech/badge/reserver" alt="PyPI Downloads">
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
- Run `pip install reserver==0.3`
### Source code
- Download [Version 0.3](https://github.com/openscilab/reserver/archive/v0.3.zip) or [Latest Source](https://github.com/openscilab/reserver/archive/dev.zip)
- Run `pip install .`

## Usage

### Programmatically 
Reserve a package name in main PyPI (pypi.org)
```python
from reserver import PyPIUploader
uploader = PyPIUploader(PYPI_TOKEN, test_pypi=False)
uploader.upload("CONSIDERED_NAME_FOR_YOUR_PACKAGE")
```
Reserve batch of names with custom user-defined parameters in test PyPI (test.pypi.org)
```python
uploader = PyPIUploader(TEST_PYPI_TOKEN, test_pypi=True)
uploader.batch_upload(["PACKAGE_NAME_1", "PACKAGE_NAME_2"], ["config1.json", "config2.json"])
```
### CLI
⚠️ You can use `reserver` or `python -m reserver` to run this program
#### Version
```console
reserver -v
reserver --version
```
#### Reserve in test PyPI (test.pypi.org)
```console
reserver --name sample_name1 sample_name2 --token=TEST_PYPI_TOKEN --test
```
#### Reserve in main PyPI (pypi.org)
```console
reserver --name sample_name1 sample_name2 --token=PYPI_TOKEN
```
#### Customizing package parameters

You can customize the following package parameters for reservations on PyPI using the Reserver CLI. The details and defaults are provided in the table below.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `description` | string | `This name has been reserved using Reserver` | A short description of your PyPI package name reservation. |
| `author` | string | `Development Team` | The name of the author or development team. |
| `author_email` | email address | `test@test.com` | An email address for contact. |
| `url` | web address | `https://url.com` | The project's main repository URL. |
| `download_url` | web address | `https://download_url.com` | The download URL for the package. |
| `source` | web address | `https://github.com/source` | The source code repository URL. |
| `license` | string | `MIT` | The license under which your package is distributed. |

There are two ways to define these custom parameters:

**1. Single `param.json` for all packages:**

This approach uses a single JSON file (`param.json`) to define common parameters for all packages. This file could hold information like those described in the table.

Here's how to use this method:

```console
reserver --name sample_name1 sample_name2 --param config.json --token=PYPI_TOKEN
```
**2. Dedicated `param.json` per package:**

This approach allows for more customization by having a separate JSON file for each package. Each file would contain parameters specific to that particular package.

Here's how this method works:

```console
reserver --name sample_name1 sample_name2 --param name1_param.json name2_param.json --token=PYPI_TOKEN
```

Choose the method that best suits your needs. Using a single `param.json` is efficient for packages with similar information, while separate files offer more granular control.

⚠️ You can use all available features on both `pypi.org` and `test.pypi.org`.
## Issues & bug reports

Just fill an issue and describe it. We'll check it ASAP! or send an email to [reserver@openscilab.com](mailto:reserver@openscilab.com "reserver@openscilab.com"). 

- Please complete the issue template
 
You can also join our discord server

<a href="https://discord.gg/RD2y6SGuY3"><img src="https://img.shields.io/discord/1064533716615049236.svg?style=for-the-badge" alt="Discord Channel"></a>

## Show your support

### Star this repo
Give a ⭐️ if this project helped you!

### Donate to our project
If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .			

<a href="https://openscilab.com/#donation" target="_blank"><img src="https://github.com/openscilab/reserver/raw/main/otherfiles/donation.png" height="90px" width="270px" alt="Reserver Donation"></a>
