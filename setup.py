# -*- coding: utf-8 -*-
"""Setup module."""

from setuptools import setup

def read_description():
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return '''PyPI Package Name Reserver'''


setup(
    name='reserver',
    packages=['reserver',],
    version='0.8',
    description='PyPI package name reserver',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Reserver Development Team',
    author_email='reserver@openscilab.com',
    url='https://github.com/openscilab/reserver',
    download_url='https://github.com/openscilab/reserver/tarball/v0.8',
    keywords='pypi pip package name reserve reserver reservation python',
    project_urls={
        'Source': 'https://github.com/openscilab/reserver',
    },
    install_requires=[
        'art>=5.3',
        'setuptools>=40.8.0',
        'wheel>=0.35.0',
        'twine>=3.5.0',
        'chardet>=4.0.0',
        'build>=0.9.0'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',

    ],
    license='MIT',
    entry_points={
            'console_scripts': [
                'reserver = reserver.__main__:main',
            ]
    }
)
