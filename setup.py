#!/usr/bin/env python

import os
from setuptools import setup


def package_files(directory):
    """Recursively add subfolders and files."""
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

EXTRA_FILES = package_files('notifications')

setup(
    name='django-notifs', version='2.5.5',
    description='Re-usable notification app for Django',
    url='https://github.com/danidee10/django-notifs', author='Osaetin Daniel',
    author_email='osaetindaniel@gmail.com', license='GPL',
    packages=['notifications'], package_data={'': EXTRA_FILES},
    install_requires=['django', 'pika'], zip_safe=False
)
