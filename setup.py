from setuptools import setup
import os 

packages = [r[0] for r in os.walk('pht') if not r[0].endswith('__pycache__') ]
setup(
    name='pht',
    description='PHT Train API for Python',
    version='1.0rc2',
    packages=packages
)

