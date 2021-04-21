#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Default testing for pacifica services."""


def test_pacifica_env(host):
    """Test the pacifica virtual env is there."""
    check_bins = [
        '/usr/bin/gcc',
        '/usr/bin/make',
        '/usr/bin/python3',
        '/usr/bin/pip3'
    ]
    for inst_file in check_bins:
        run_file = host.file(inst_file)
        assert run_file.exists
        assert run_file.user == 'root'
        assert run_file.group == 'root'
    run_file = host.file('/opt/default/bin/activate')
    assert run_file.exists
    assert run_file.user == 'pacifica'
    assert run_file.group == 'pacifica'


def test_pacifica_python(host):
    """Make sure we are running Python 3.8."""
    python_version = host.run('/opt/default/bin/python --version')
    assert python_version.rc == 0
    assert '3.8' in python_version.stdout
