#!/usr/bin/env python

"""
Auto format the python code
"""

import subprocess

from fabric.api import local

if __name__ == '__main__':
    # import ipdb; ipdb.set_trace()
    py_files = subprocess.check_output(['find', '.', '-name', '*.py', '-not', '-path', './.tox/*']).splitlines()
    file_names = ' '.join([x.decode('utf-8') for x in py_files])
    # file_names = b' '.join(py_files)
    local('isort {}'.format(file_names))
    local('autopep8 --in-place {}'.format(file_names))

    local('flake8 {}'.format(file_names))
