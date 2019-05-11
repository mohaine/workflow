# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='workflow',
    version='1.0.0',
    description='Simple Workflow',
    long_description=readme,
    author='Michael Graessle',
    author_email='mike@graessle.net',
    url='https://github.com/mohaine/workflow',
    license=license,
    packages=find_packages(exclude=('tests'))
)
