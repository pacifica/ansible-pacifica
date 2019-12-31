#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for archiveinterface to verify working."""


def test_archiveinterface_socket(host):
    """Test the archiveinterface default socket."""
    sock = host.socket('tcp://0.0.0.0:8080')
    assert sock


def test_archiveinterface_configs(host):
    """Test archiveinterface configs are present."""
    test_files = [
        '/opt/default/archiveinterface.ini',
        '/opt/default/archiveinterface-cp.ini',
        '/opt/default/archiveinterface',
        '/etc/systemd/system/archiveinterface.service'
    ]
    for test_file in test_files:
        run_file = host.file(test_file)
        assert run_file.exists
