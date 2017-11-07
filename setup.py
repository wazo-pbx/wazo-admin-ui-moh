#!/usr/bin/env python3
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo_admin_ui_moh',
    version='0.1',

    description='Wazo Admin Music On Hold',

    author='Wazo Authors',
    author_email='dev@wazo.community',

    url='http://wazo.community',

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    entry_points={
        'wazo_admin_ui.plugins': [
            'moh = wazo_plugind_admin_ui_moh_official.plugin:Plugin',
        ]
    }
)
