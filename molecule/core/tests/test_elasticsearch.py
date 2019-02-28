#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for elasticsearch to verify working."""


def test_elasticsearch(host):
    """Test the elasticsearch default port."""
    sock = host.socket('tcp://0.0.0.0:9200')
    assert sock
