# test_arithmetic.py initial file
'''Module to test arithmetic.py'''
import pytest
from arithmetic import add, subtract, multiply, divide

def test_add():
    '''Function to test function.
    '''
    assert add(1, 2) == 3

def test_subtract():
    '''Function to test subtract function.'''
    assert subtract(2, 1) == 1

def test_multiply():
    '''Function to test multiply function.'''
    assert multiply(2, 3) == 6

def test_divide():
    '''Function to test divide function'''
    assert divide(6, 2) == 3

def test_divide_by_zero():
    '''Function to test divide function'''
    with pytest.raises(ValueError):
        divide(1, 0)
