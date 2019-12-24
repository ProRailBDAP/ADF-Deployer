from setuptools import (
    find_packages,
    setup,
)

version = '1.0.0a0'

setup(
    name='ADFDeployer',
    description='Continuously deploy an Azure Data Factory repository.',
    version=version,
    packages=find_packages(),
    install_requires=[
        'azure >= 4.0.0',
        'requests >= 2.22.0',
    ],
    entry_points={
        'console_scripts': [
            'adf-deployer = ADFDeployer.runner:main'
        ]
    },
)
