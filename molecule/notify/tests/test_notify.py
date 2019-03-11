#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing module for notifictaions to verify working."""


def test_notifications(host):
    """Test the notifications default port."""
    sock = host.socket('tcp://0.0.0.0:8070')
    assert sock
