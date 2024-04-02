#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# author: songquanheng
# email: wannachan@outlook.com
# date: 2022/10/19 周三 15:54:16
# description: 日期时间类

from datetime import datetime


class DateUtils:
    """日期时间的辅助类"""

    """
    将当前时刻转化为2024-04-01 22:32:13的格式
    """
    @staticmethod
    def now_str():
        now = datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')

    """
    将当前时刻转化为2024-04-01 22:32:13-112345的格式，包好毫秒数
    """
    @staticmethod
    def now_str_in_millis():
        now = datetime.now()
        return now.strftime('%Y-%m-%d-%H-%M-%S-%f')

    """
    将当前时刻转化为2024-04-01的格式
    """
    @staticmethod
    def now_date():
        return datetime.now().strftime('%Y-%m-%d')


    """
    将传入的时刻转化为相应的毫秒数整数
    """
    @staticmethod
    def timestamp_in_millis(now: datetime):
        print(datetime.timestamp(now))
        return int(datetime.timestamp(now) * 1000)


    """
    计算两个python 的datetime对象的间隔的毫秒数
    """
    
    @staticmethod
    def duration_in_millis(start_time: datetime, end_time: datetime):
        assert isinstance(start_time, datetime)
        assert isinstance(end_time, datetime)
        if start_time < end_time:
            return DateUtils.timestamp_in_millis(end_time) - DateUtils.timestamp_in_millis(start_time)

        return DateUtils.timestamp_in_millis(start_time) - DateUtils.timestamp_in_millis(end_time)

