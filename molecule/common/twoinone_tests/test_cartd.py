#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for cartd to verify working."""


def test_cartd_socket(host):
    """Test the cartd default socket."""
    for port in [8081, 8082]:
        sock = host.socket('tcp://0.0.0.0:{}'.format(port))
        assert sock


def check_cartd_backend_service(host):
    """Check that the cartd backend service is running on the host."""
    for svc_id in [1, 2]:
        assert host.service('cartd_{}_backend'.format(svc_id)).is_running


def check_cartd_frontend_service(host):
    """Check that the cartd frontend service is running on the host."""
    for svc_id in [1, 2]:
        assert host.service('cartd_{}_frontend'.format(svc_id)).is_running


def test_cartd_return(host):
    """Check that cartd returns properly."""
    for port in [8081, 8082]:
        command = """curl --digest -L -D - http://localhost:{}/""".format(port)
        cmd = host.run(command)
        assert 'HTTP/1.1 200 OK' in cmd.stdout
