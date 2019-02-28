#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for policy to verify working."""


def test_policy(host):
    """Test the policy default port."""
    sock = host.socket('tcp://0.0.0.0:8181')
    assert sock
