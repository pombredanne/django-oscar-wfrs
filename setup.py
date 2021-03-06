#!/usr/bin/env python
import codecs
import os.path
from setuptools import setup
from versiontag import get_version, cache_git_tag


packages = [
    'wellsfargo',
    'wellsfargo.api',
    'wellsfargo.connector',
    'wellsfargo.dashboard',
    'wellsfargo.management',
    'wellsfargo.management.commands',
    'wellsfargo.migrations',
    'wellsfargo.tests',
]

setup_requires = [
    'versiontag>=1.0.3',
]

requires = [
    'celery>=3.1.23',
    'Django>=1.8.12',
    'djangorestframework>=3.3.2',
    'django-oscar>=1.2.1',
    'django-oscar-accounts>=0.4rc1',
    'django-oscar-api>=1.0.4',
    'django-localflavor>=1.3',
    'instrumented-soap>=1.1.0',
]


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)

def read(fname):
    return codecs.open(fpath(fname), encoding='utf-8').read()

cache_git_tag()

setup(
    name='django-oscar-wfrs',
    description="An extension on-top of django-oscar-accounts to allow interfacing with Wells Fargo Retail Services.",
    version=get_version(pypi=True),
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    author='Craig Weber',
    author_email='crgwbr@gmail.com',
    url='https://gitlab.com/thelabnyc/django-oscar-wfrs',
    license='ISC',
    packages=packages,
    include_package_data=True,
    install_requires=requires,
    setup_requires=setup_requires
)
