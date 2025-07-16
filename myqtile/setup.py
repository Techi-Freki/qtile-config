import os

from setuptools import setup, find_packages


working_dir = os.getcwd()

with open(f'{working_dir}/README.md', 'r') as readme:
    README = readme.read()

with open(f'{working_dir}/VERSION', 'r') as version:
    VERSION = version.readline()

with open(f'{working_dir}/requirements.txt', 'r') as requirements:
    REQUIREMENTS = requirements.readlines()

setup(
    name='myqtile',
    version=VERSION,
    packages=find_packages(),
    url='https://github.com/Techi-Freki/myqtile',
    license='MIT',
    author='Techi-Freki',
    author_email='techifreki@proton.me',
    description='A qtile configuration wrapper',
    include_package_data=True,
    long_description=README,
    long_description_content_type='markdown/text',
    install_requires=REQUIREMENTS
)
