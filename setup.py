from setuptools import setup, find_packages

setup(
    name='nativeETL',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[ 
        # 'PyYAML',
    ],
    entry_points={  
        'console_scripts': [
            'nativeETL=nativeETL.cli:main',
        ],
    },
)
