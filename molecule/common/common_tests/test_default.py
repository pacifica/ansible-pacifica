#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Default testing for pacifica services."""


def test_pacifica_env(host):
    """Test the pacifica virtual env is there."""
    check_bins = [
        '/opt/default/bin/activate',
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
