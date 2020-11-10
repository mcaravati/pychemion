from setuptools import find_packages, setup

setup(
    name='pychemion',
    packages=find_packages(include=['pychemion']),
    version='0.1.0',
    description='A library to control CHEMION glasses',
    author='mcaravati',
    license='CC BY-NC-SA 4.0',
    install_requires=['bluepy'],
    setup_requires=['pytest-runner'],
    tests_requires=['pytest'],
    test_suite='tests',
)