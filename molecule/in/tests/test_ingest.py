#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for ingest to verify working."""

def test_ingest_socket(host):
    """Test the ingest default socket."""
    sock = host.socket('tcp://0.0.0.0:8066')
    assert sock
