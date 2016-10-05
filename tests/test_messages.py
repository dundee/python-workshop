from contextlib import contextmanager
from unittest import mock

import pytest

from main import Messages


@pytest.fixture
def messages(config):
    return Messages(db_config=config['database'])


def test_load(messages):
    @contextmanager
    def db_connection_mock(db_config):
        yield mock.Mock(fetchall=mock.Mock(return_value=[
            ('michael', 'hello'),
            ('daniel', 'world'),
        ]))

    with mock.patch('chat.model.db_connection', db_connection_mock):
        messages.load()
        assert messages._messages == [
            {'user_name': 'michael', 'message': 'hello'},
            {'user_name': 'daniel', 'message': 'world'},
        ]
