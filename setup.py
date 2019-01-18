from setuptools import setup

setup(
    name='pht',
    description='PHT Train API for Python',
    version='1.0rc2',
    packages=[
        'pht',
        'pht.internal',
        'pht.internal.describe',
        'pht.internal.describe.formula',
        'pht.internal.describe.property',
        'pht.rebase',
        'pht.response',
        'pht.train']
)
