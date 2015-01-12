import os
from setuptools import setup

version = '0.2'
long_description_filename = os.path.join(
    os.path.dirname(__file__), 'README.rst')
long_description = open(long_description_filename).read()

setup(
    name="setuptools-yaml",
    version=version,
    author="George Sudarkoff",
    author_email="george@sudarkoff.com",
    url="https://github.com/sudarkoff/setuptools-yaml",
    keywords='distutils setuptools metadata yaml',
    description="Use YAML file for your project metadata",
    long_description=long_description,
    license='MIT',
    install_requires=['pyyaml'],
    py_modules=['setuptools_yaml'],
    zip_safe=False,
    entry_points="""
        [distutils.setup_keywords]
        metadata_yaml=setuptools_yaml:metadata_yaml
        """
)
