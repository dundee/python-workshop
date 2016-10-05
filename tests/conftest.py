import os
import sys
from unittest import mock

import pytest

sys.path.append(
    os.path.join(os.path.dirname(__file__), '..')
)

from chat.config import DEFAULT_CONFIG


@pytest.fixture
def config():
    return DEFAULT_CONFIG


@pytest.fixture
def http_client():
    return mock.Mock()
