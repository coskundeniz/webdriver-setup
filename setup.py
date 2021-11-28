#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import setuptools


with open('README.md', 'r') as f:
    README = f.read()

REQUIRED_PACKAGES = [
    'selenium',
    'webdriver-manager'
]

setuptools.setup(
    name='webdriver-setup',
    version='1.1.0',
    description=('Easy to use webdriver instance creation api'),
    long_description=README,
    long_description_content_type="text/markdown",
    author='Coşkun Deniz',
    author_email='coskun.denize@gmail.com',
    url='https://github.com/coskundeniz/webdriver-setup',
    packages=['webdriver_setup'],
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=REQUIRED_PACKAGES,
    keywords=['webdriver', 'selenium', 'browser automation',
              'testing', 'test automation'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows'
    ]
)
