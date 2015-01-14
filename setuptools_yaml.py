import inspect
import os
import logging

import yaml


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def metadata_yaml(dist, attr, value):
    logger.debug(
        'metadata_yaml: '
        'dist = %r; attr = %r; value = %r',
        dist, attr, value)
    frame = _get_code_object()
    setup_py_path = inspect.getsourcefile(frame)
    yaml_filename = os.path.join(os.path.dirname(setup_py_path), value)
    logger.debug('yaml_filename = %r', yaml_filename)
    with open(yaml_filename) as yaml_file:
        metadata = yaml.load(yaml_file)
    for keyname in metadata.keys():
        setattr(dist.metadata, keyname, metadata[keyname])


def _get_code_object():
    frame = inspect.currentframe()

    while frame:
        code = frame.f_back.f_code
        if code.co_filename.endswith('setup.py'):
            return code
        frame = frame.f_back
