from unittest import mock
from json.decoder import JSONDecodeError

import pytest

from chat.model import User
from main import TrackerClient


@pytest.fixture
def tracker(config, http_client):
    return TrackerClient(config=config, http_client=http_client)


def test_get_users_failed(http_client, tracker):
    http_client.get.return_value = mock.Mock(status_code=401)
    with pytest.raises(Exception):
        tracker.get_users.__wrapped__()


def test_get_users_bad_json(http_client, tracker):
    http_client.get.return_value = mock.Mock(status_code=200, json=mock.Mock(side_effect=JSONDecodeError('', '', 0)))
    assert not tracker.get_users()


def test_get_users(http_client, tracker):
    data = [
        {'ip': '127.0.0.1', 'name': 'michael'},
        {'ip': '10.0.0.1', 'name': 'daniel'},
    ]
    http_client.get.return_value = mock.Mock(status_code=200, json=mock.Mock(return_value=data))
    assert tracker.get_users() == [
        User('127.0.0.1', 'michael'),
        User('10.0.0.1', 'daniel'),
    ]
