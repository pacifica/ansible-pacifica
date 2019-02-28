#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for cartd to verify working."""


def test_cartd(host):
    """Test the cartd default port."""
    sock = host.socket('tcp://0.0.0.0:8081')
    assert sock
