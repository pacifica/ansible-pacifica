#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Default testing for pacifica services."""


def test_pacifica_env(host):
    """Test the pacifica virtual env is there."""
    for inst_file in ['/usr/bin/gcc', '/usr/bin/make', '/usr/bin/python3', '/usr/bin/pip3']:
        run_file = host.file(inst_file)
        assert run_file.exists
        assert run_file.user == 'root'
        assert run_file.group == 'root'
