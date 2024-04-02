# !/usr/bin/env python
# -*- encoding: utf-8 -*-

# test_rectangle.py

import pytest
from src.common.rectangle import Rectangle

# 测试周长计算
def test_perimeter():
    rect = Rectangle(3, 4)
    assert rect.perimeter() == 14

# 测试面积计算
def test_area():
    rect = Rectangle(5, 6)
    assert rect.area() == 30

# 测试除以零的情况
def test_area_with_zero():
    rect = Rectangle(5, 0)
    # with pytest.raises(ZeroDivisionError):
    #     rect.area()
    assert rect.area() == 0

def test_perimeter_mock(monkeypatch):
    rect = Rectangle(3, 4)
    
    # 模拟perimeter方法返回一个固定值
    def mock_perimeter(self):
        return 20
    monkeypatch.setattr(Rectangle, 'perimeter', mock_perimeter)
    assert rect.perimeter() == 20

    # 模拟perimeter方法抛出异常
    def mock_perimeter_that_raises(self):
        raise ValueError("Perimeter calculation failed")
    monkeypatch.setattr(Rectangle, 'perimeter', mock_perimeter_that_raises)
    with pytest.raises(ValueError):
        rect.perimeter()

    # 模拟area方法返回一个固定值
    def mock_area(self):
        return 100
    monkeypatch.setattr(Rectangle, 'area', mock_area)
    assert rect.area() == 100

    # 模拟area方法抛出异常
    def mock_area_that_raises(self):
        raise ZeroDivisionError("Area calculation failed")
    monkeypatch.setattr(Rectangle, 'area', mock_area_that_raises)
    with pytest.raises(ZeroDivisionError):
        rect.area()