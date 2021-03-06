# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 JinTian.
#
# This file is part of alfred
# (see http://jinfagang.github.io).
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
"""
install alfred into local bin dir.
"""
from setuptools import setup, find_packages
from setuptools import setup, Extension
import io
from os import path

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='visiontransformers',
      version='0.0.1',
      keywords=['deep learning', 'script helper', 'tools'],
      description='''
      All vision transformers that you need
      ''',
      long_description=long_description,
      long_description_content_type='text/markdown',
      license='Apache 2.0',
      packages=[
          'visiontransformers/formers',
          'visiontransformers/common'
      ],
      # package_dir={'alfred': 'alfred'},
    #   entry_points={
    #       'console_scripts': [
    #           'alfred = alfred.alfred:main'
    #       ]
    #   },
      include_package_data=True,
      author="Lucas Jin",
      author_email="jinfagang19@163.com",
      url='https://github.com/jinfagang/visiontransformers',
      platforms='any',
      install_requires=['alfred-py', 'einops']
      )
