# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# test_calculator.py

from src.caculator import add, sub


def test_add_positive_numbers():
    """Test that the add function correctly adds two positive numbers."""
    result = add(3, 4)
    assert result == 7

def test_add_negative_numbers():
    """Test that the add function correctly adds two negative numbers."""
    result = add(-3, -4)
    assert result == -7

def test_add_positive_and_negative_numbers():
    """Test that the add function correctly adds a positive and a negative number."""
    result = add(3, -2)
    assert result == 1

def test_add_zero():
    """Test that the add function returns zero when both numbers are zero."""
    result = add(0, 0)
    assert result == 0
    
def test_add_positive_numbers():
    """Test that the add function correctly adds two positive numbers."""
    result = sub(3, 4)
    assert result == -1

# 可选：使用参数化测试来测试更多的情况
from pytest import mark

@mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 2, 1),
    (-1, -2, -3),
    (0, 0, 0)
])
def test_add_with_parameters(a, b, expected):
    """Test the add function with various parameters."""
    result = add(a, b)
    assert result == expected