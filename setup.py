# coding: utf-8
# Copyright 2013 The Font Bakery Authors.
# Copyright 2017-2021 The Google Fonts Tools Authors.
# Copyright 2022 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# See AUTHORS.txt for the list of Authors and LICENSE.txt for the License.
import os
from setuptools import setup

# Read the contents of the README file
with open('README.md') as f:
    long_description = f.read()

setup(
    name="glyphsets",
    use_scm_version={"write_to": "Lib/glyphsets/_version.py"},
    url='https://github.com/googlefonts/glyphsets/',
    description='A python API for evaluating coverage of glyph sets in font projects.',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    author=('Dave Crossland, '
            'Eli Heuer, '
            'Felipe Sanches, '
            'Lasse Fister, '
            'Marc Foley, '
            'Roderick Sheeter'),
    author_email='dave@lab6.com',
    package_dir={'': 'Lib'},
    packages=['glyphsets'],
    package_data={'glyphsets': [
                      "encodings/*.nam",
                      "encodings/GF Glyph Sets/*.nam",
                      "*.json",
                  ]
                 },
    entry_points={"console_scripts": ["glyphsets = glyphsets.__main__:main"]},
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Fonts',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    python_requires=">=3.7",
    setup_requires=['setuptools_scm>=4,<6.1'],
    install_requires=[
        'setuptools',
        'FontTools[ufo]',
        'glyphsLib',
        'defcon',
    ]
)
