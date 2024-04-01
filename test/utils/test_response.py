# !/usr/bin/env python
# -*- encoding: utf-8 -*-


from src.utils.response import Response

def test_success():
    suc = Response.success("zjlab is a good lab")
    assert suc.msg == "zjlab is a good lab"
    
def test_error():
    fail = Response.error()
    assert fail.msg == 'error'

def test_is_sucessful():
    suc = Response.success()    
    assert suc.is_successful() == True
