#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for metadata to verify working."""


def test_metadata_socket(host):
    """Test the metadata default socket."""
    sock = host.socket('tcp://0.0.0.0:8121').is_listening
    assert sock


def check_metadata_service(host):
    """Check that the metadata service is running on the host."""
    assert host.service('metadata').is_running


def test_metadata_return(host):
    """Check that metadata returns properly."""
    command = """curl --digest -L -D - http://localhost:8121/"""
    cmd = host.run(command)
    assert 'HTTP/1.1 200 OK' in cmd.stdout
