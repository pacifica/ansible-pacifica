#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for notifictaions to verify working."""
from pytest import mark


def test_notifications_socket(host):
    """Test the notifications default socket."""
    sock = host.socket('tcp://0.0.0.0:8070')
    assert sock


def check_notify_backend_service(host):
    """Check that the notify backend service is running on the host."""
    assert host.service('notify_backend').is_running


def check_notify_frontend_service(host):
    """Check that the notify frontend service is running on the host."""
    assert host.service('ingest_frontend').is_running


@mark.skip(reason='no way of currently testing this')
def test_notifications_return(host):
    """Check that notifications returns properly."""
    command = """curl --digest -L -D - http://localhost:8070/"""
    cmd = host.run(command)
    assert 'HTTP/1.1 200 OK' in cmd.stdout
