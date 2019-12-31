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


def check_archiveinterface_service(host):
    """Check that the archiveinterface service is running on the host."""
    assert host.service('archiveinterface').is_running


def test_archiveinterface_return(host):
    """Check that the archiveinterface returns properly."""
    command = """curl --digest -L -D - http://localhost:8080/"""
    cmd = host.run(command)
    assert 'HTTP/1.1 200 OK' in cmd.stdout
