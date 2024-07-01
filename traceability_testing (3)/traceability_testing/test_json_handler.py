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
def test_read_json(json_handler_instance, temp_file_path):
    '''Test reading JSON data from a file using JsonHandler.'''
    data = {"test": "data"}
    json_handler_instance.write_json(data, temp_file_path)
    read_data = json_handler_instance.read_json(temp_file_path)
    assert read_data == data

@requirement("REQ-102")
def test_write_json(json_handler_instance, temp_file_path):
    '''Test writing and reading JSON data using JsonHandler.'''
    data = {"test": "data"}
    json_handler_instance.write_json(data, temp_file_path)
    read_data = json_handler_instance.read_json(temp_file_path)
    assert read_data == data

@requirement("REQ-103")
def test_check_key(json_handler_instance):
    '''Test checking for key in JSON data using JsonHandler.'''
    data = {"test": "data"}
    assert json_handler_instance.check_key(data, 'test')

@requirement("REQ-104")
def test_update_json(json_handler_instance, temp_file_path):
    '''Test updating JSON data using JsonHandler.'''
    data = {"test": "data"}
    json_handler_instance.write_json(data, temp_file_path)
    json_handler_instance.update_json("test", "new data", temp_file_path)
    updated_data = json_handler_instance.read_json(temp_file_path)
    assert updated_data["test"] == "new data"