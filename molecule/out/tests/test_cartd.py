#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for cartd to verify working."""

def test_cartd_socket(host):
    """Test the cartd default socket."""
    sock = host.socket('tcp://0.0.0.0:8081')
    assert sock
