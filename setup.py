from setuptools import setup, find_packages

setup(
    name='unit_test_generator',
    version='0.1.0',
    description='Generate Pytest unit tests from Python functions.',
    packages=find_packages(exclude=['venv']),
    install_requires=[
        'pytest>=6.0.1',
        'click>=7.1.2',
    ],
    entry_points={
        'console_scripts': [
            'generate-unit-test=src.main:generate_unit_test',
        ],
    },
)