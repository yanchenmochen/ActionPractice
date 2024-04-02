# !/usr/bin/env python
# -*- encoding: utf-8 -*-

# 添加关于日期功能类的单元测试
from src.utils.date_utils import DateUtils
import re
import datetime

def test_now_srt():
    now_str = DateUtils.now_str()
    assert now_str.count('-') == 2
    assert now_str.count(':') == 2
    
def test_now_str_in_millis():
    now_str = DateUtils.now_str_in_millis()
    assert now_str.count('-') == 6
    assert now_str.count(':') == 0
    

    # 定义正则表达式
    time_pattern = r'^(\d{4})-(\d{2})-(\d{2})-(\d{2})-(\d{2})-(\d{2})-(\d{6})$'
    assert re.match(time_pattern, now_str)
    
def  test_now_date():
    now = DateUtils.now_date()
    assert now.count(':') == 0
    assert now.count('-') == 2
    

def test_timestamp_in_millis():
    now = datetime.datetime.now()
    res = DateUtils.timestamp_in_millis(now)
    assert res == int(now.timestamp() * 1000)
    
def test_duration_in_millis():
    # 生成特定时间的日期对象 # 假设我们要创建的日期是 2024年4月1日 15点30分0秒
    date1 = datetime.datetime(2024, 4, 1, 15, 30, 0)
    # 创建另一个日期对象作为参考 
    date2 = datetime.datetime(2024, 4, 2, 10, 0, 0)
    # 2024年4月2日 10点0分0秒 # 计算两个日期对象的间隔 # 首先计算两个日期对象的差值（时间差）
    time_difference = date2 - date1
    # 将时间差转换为毫秒数 # 时间差对象包含天数和秒数，我们需要将天数转换为毫秒并加上秒数转换的毫秒
    total_milliseconds = (time_difference.days * 24 * 60 * 60 * 1000) + (time_difference.seconds * 1000) + time_difference.microseconds / 1000
    assert total_milliseconds == DateUtils.duration_in_millis(date1, date2)
    assert total_milliseconds == DateUtils.duration_in_millis(date2, date1)
