#!/usr/bin/env python
from setuptools import find_packages, setup

install_requires = [
    'blessed',
    'rich',
    'textual'
]

setup(
    name='telnetceol',
    version="0.1",
    license='MIT',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    python_requires='~=3.7',
    dependency_links=[],
    entry_points={},
    scripts=['scripts/ceol'],
)
