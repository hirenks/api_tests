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
        description='Pytest Configuration Example',
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
            'Development Status :: 1 - Planning',
            'Framework :: Pytest',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: Software Development',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
    )
