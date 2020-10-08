#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for elasticsearch to verify working."""


def test_mysql_socket(host):
    """Test the postgresql default port."""
    sock = host.socket('tcp://0.0.0.0:3306').is_listening
    assert sock


def check_mysql_service(host):
    """Check that the postgresql service is running on the host."""
    assert host.service('mariadb').is_running
