#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for elasticsearch to verify working."""

def test_postgresql_socket(host):
    """Test the postgresql default port."""
    sock = host.socket('tcp://127.0.0.1:5432').is_listening
    assert sock

def check_postgresql_service(host):
    """Check that the postgresql service is running on the host"""
    assert host.service("postgresql").is_running