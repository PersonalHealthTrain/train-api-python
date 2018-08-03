from distutils.core import setup

requires = [
    'requests==2.19.1'
]

setup(
    name='PHT Train API for Python',
    version='0.1dev',
    requires=requires,
    packages=['pht']
)
