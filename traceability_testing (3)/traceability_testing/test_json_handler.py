"""
Module: test_json_handler.py
This module contains unit tests for JsonHandler class.
"""
import pytest
from json_handler import JsonHandler
def requirement(ides):
    """Decorator to assign requirement ID to test functions."""
    def decorator(function):
        function.requirement = ides
        return function
    return decorator

@pytest.fixture
def json_handler_instance():
    '''Fixture to provide an instance of JsonHandler.'''
    return JsonHandler()

@pytest.fixture
def temp_file_path(tmp_path):
    '''Fixture to provide a temporary file path.'''
    return tmp_path / "test.json"


@requirement("REQ-101")
def test_read_json(json_handler, temp_file):
    '''Test reading JSON data from a file using JsonHandler.'''
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    read_data = json_handler.read_json(temp_file)
    assert read_data == data

@requirement("REQ-102")
def test_write_json(json_handler, temp_file):
    '''Test writing and reading JSON data using JsonHandler.'''
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    read_data = json_handler.read_json(temp_file)
    assert read_data == data

@requirement("REQ-103")
def test_check_key(json_handler):
    '''Test checking for key in JSON data using JsonHandler.'''
    data = {"test": "data"}
    assert json_handler.check_key(data, 'test')

@requirement("REQ-104")
def test_update_json(json_handler, temp_file):
    '''Test updating JSON data using JsonHandler.'''
    data = {"test": "data"}
    json_handler.write_json(data, temp_file)
    json_handler.update_json("test", "new data", temp_file)
    updated_data = json_handler.read_json(temp_file)
    assert updated_data["test"] == "new data"
