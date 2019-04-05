"""
Install Script for the PHT package. Use `python setup install` to install the 'pht' module
"""
from setuptools import setup, find_packages

setup(
    name='pht',
    author="Lukas Zimmermann",
    author_email="luk.zim91@gmail.com",
    description='PHT Train API for Python',
    keywords='PHT train',
    url='https://github.com/PersonalHealthTrain/train-api-python',
    version='1.0rc11',
    packages=find_packages()
)
