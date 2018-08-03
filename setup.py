from setuptools import setup

requires = [
    'requests==2.19.1'
]

setup(
    name='PHT Train API for Python',
    version='0.1.dev0',
    install_requires=requires,
    packages=['pht']
)
