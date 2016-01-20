import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-simple-wiki',
    version='0.0.1',
    packages=['simple-wiki'],
    include_package_data=True,
    license='GNU GENERAL PUBLIC LICENSE v2',
    description='Simple wiki library for django',
    long_description=README,
    url='http://lynlab.co.kr/',
    author='Do Hoerin',
    author_email='hellodhlyn@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE v2',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)