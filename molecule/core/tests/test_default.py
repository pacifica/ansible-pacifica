#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Default testing for pacifica virtualenv."""


def test_pacifica_virtualenv(host):
    """Test the pacifica virtualenv."""
    run_file = host.file('/opt/default/bin/activate')
    assert run_file.exists
