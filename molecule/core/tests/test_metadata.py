#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for metadata to verify working."""


def test_metadata(host):
    """Test the metadata default port."""
    sock = host.socket('tcp://0.0.0.0:8121')
    assert sock
