#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for cartd to verify working."""
from pytest import mark


def test_cartd_socket(host):
    """Test the cartd default socket."""
    sock = host.socket('tcp://0.0.0.0:8081')
    assert sock


def check_cartd_backend_service(host):
    """Check that the cartd backend service is running on the host."""
    assert host.service('cartd_backend').is_running


def check_cartd_frontend_service(host):
    """Check that the cartd frontend service is running on the host."""
    assert host.service('cartd_frontend').is_running


@mark.skip(reason='no way of currently testing this')
def test_cartd_return(host):
    """Check that cartd returns properly."""
    command = """curl --digest -L -D - http://localhost:8081/"""
    cmd = host.run(command)
    assert 'HTTP/1.1 200 OK' in cmd.stdout
