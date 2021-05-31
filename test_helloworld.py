import os
import tempfile

import pytest

from app import app


def test_hello():
    """Start with a blank database."""
    client = app.test_client()
    content = client.get('/')
    assert b'hello' in content.data
