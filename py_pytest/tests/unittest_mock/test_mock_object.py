# py_pytest/tests/unittest_mock/test_mock_object.py

from unittest.mock import Mock

json = Mock()


def test_called():
    json.loads({"key": "value"})

    json.loads.assert_called()
    json.loads.assert_called_once()


def test_called_with():
    json.loads({"key": "value"})

    json.loads.assert_called_with({"key": "value"})
    json.loads.assert_called_once_with({"key": "value"})


def test_error_called():
    json.loads({"key": "value"})
    json.loads({"key": "value"})

    json.loads.assert_called()
    json.loads.assert_called_once()
