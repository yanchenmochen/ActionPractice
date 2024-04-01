# !/usr/bin/env python
# -*- encoding: utf-8 -*-


from src.utils.response import Response

def test_success():
    suc = Response.success("zjlab is a good lab")
    assert suc.code == 0
    assert suc.msg == "zjlab is a good lab"
    
def test_error():
    fail = Response.error()
    
    assert fail.code == -1
    assert fail.msg == 'error'
    
