#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for redis to verify working."""


def test_elasticsearch_socket(host):
    """Test the redis default socket."""
    sock = host.socket('tcp://0.0.0.0:6379')
    assert sock
