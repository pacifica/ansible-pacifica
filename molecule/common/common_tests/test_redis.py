#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for redis to verify working."""


def test_redis_socket(host):
    """Test the redis default socket."""
    sock = host.socket('tcp://0.0.0.0:6379')
    assert sock


def check_redis_service(host):
    """Check that the redis service is running on the host."""
    assert host.service('redis').is_running
