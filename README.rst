setuptools-yaml
===============

Use `YAML <http://www.yaml.org/>`__ for your project description


Install
=======

1. Install this module

.. code:: console

    pip install setuptools-yaml


Use
===

.. code:: python

    #!/usr/bin/env python
    # setup.py

    from setuptools import setup

    setup(
        ...
        setup_requires=['setuptools-yaml'],
        metadata_yaml='project.yml',
        ...
    )

The plugin will read the specified file and populate the relevant metadata fields
of your distribution.

