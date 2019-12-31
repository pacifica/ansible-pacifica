#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for unqueid to verify working."""

def test_uniqueid_socket(host):
    """Test the uniqueid default port."""
    sock = host.socket('tcp://0.0.0.0:8051').is_listening
    assert sock

def check_uniqueid_service(host):
    """Check that the uniqueid service is running on the host"""
    assert host.service("uniqueid").is_running