from setuptools import find_packages, setup
import os

this_folder = os.path.dirname(os.path.realpath(__file__))
requirements_file = this_folder + '/requirements.txt'
install_requires = []

if os.path.isfile(requirements_file):
    with open(requirements_file) as f:
        install_requires = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='flipdigit',
    packages=find_packages(include=['flipdigit']),
    version='0.1.2',
    description='Small flip digit library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Lucas Bonvin',
    license='MIT',
    install_requires=['pyserial'],
    python_requires='>=3.6',
    license_file='LICENSE'
)