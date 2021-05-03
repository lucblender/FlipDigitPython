from setuptools import find_packages, setup

setup(
    name='flipdigit',
    packages=find_packages(include=['flipdigit']),
    version='0.1.0',
    description='Small flip digit library',
    author='Lucas Bonvin',
    license='MIT',
    install_requires=['pyserial']
)