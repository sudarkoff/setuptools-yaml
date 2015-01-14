setuptools-yaml
===============

Use `YAML <http://www.yaml.org/>`__ for your project description

.. image:: https://travis-ci.org/sudarkoff/setuptools-yaml.svg?branch=master
    :target: https://travis-ci.org/sudarkoff/setuptools-yaml


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


See also
========

- pbr_


.. _pbr: http://docs.openstack.org/developer/pbr/
