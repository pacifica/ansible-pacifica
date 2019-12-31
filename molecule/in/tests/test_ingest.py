#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for ingest to verify working."""


def test_ingest_socket(host):
    """Test the ingest default socket."""
    sock = host.socket('tcp://0.0.0.0:8066')
    assert sock


def check_ingest_backend_service(host):
    """Check that the ingest backend service is running on the host."""
    assert host.service('ingest_backend').is_running


def check_ingest_frontend_service(host):
    """Check that the ingest frontend service is running on the host."""
    assert host.service('ingest_frontend').is_running


# def test_ingest_return(host):
#     """Check that ingest returns properly."""
#     command = """curl --digest -L -D - http://localhost:8066/"""
#     cmd = host.run(command)
#     assert 'HTTP/1.1 200 OK' in cmd.stdout
