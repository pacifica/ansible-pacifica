#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for unqueid to verify working."""


def test_uniqueid(host):
    """Test the uniqueid default port."""
    sock = host.socket('tcp://0.0.0.0:8051')
    assert sock
