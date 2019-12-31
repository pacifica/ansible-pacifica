#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for policy to verify working."""

def test_policy_socket(host):
    """Test the policy default socket."""
    sock = host.socket('tcp://0.0.0.0:8181').is_listening
    assert sock

def check_policy_service(host):
    """Check that the policy service is running on the host"""
    assert host.service("policy").is_running