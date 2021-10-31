#!/usr/bin/env python

from setuptools import setup, find_packages

long_description = '''
This project performs API testing on the Jokes API.
'''

version = "1.0.0"

requirements = [
]

if __name__ == '__main__':
    setup(
        name='python_api_testing_in_docker',
        version=version,
        description='Pytest API Testing',
        long_description=long_description,
        author="hiren",
        packages=find_packages(
            include=[
                'tests',
            ]
        ),
        license='MIT',
        install_requires=requirements,
        classifiers=[
            'Framework :: Pytest',
            'Intended Audience :: Developers',
            'Intended Audience :: Software Developers in Test',
            'Programming Language :: Python :: 3.7',
            'Topic :: Software API Testing',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
    )
