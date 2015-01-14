from setuptools import Distribution

from setuptools_yaml import metadata_yaml


def test_setuptools_yaml():
    dist = Distribution()
    metadata_yaml(dist, attr='metadata.yml', value='project.yml')
    assert dist.metadata.url == 'https://github.com/sudarkoff/setuptools-yaml'
    assert dist.metadata.scripts['test'] == 'tox'
    assert dist.metadata.scripts['run'] == 'echo "testing..."'
    assert dist.metadata.scripts['build'] == 'python setup.py sdist'
