#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for notifictaions to verify working."""

def test_notifications_socket(host):
    """Test the notifications default socket."""
    sock = host.socket('tcp://0.0.0.0:8070')
    assert sock
