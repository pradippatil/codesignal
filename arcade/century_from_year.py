# -*- coding:utf-8 -*-
# @Script: century_from_year.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2018-12-17 23:34:46
# @Last Modified By: Pradip Patil
# @Last Modified: 2018-12-17 23:35:58
# @Description: https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN
'''
Given a year, return the century it is in. The first century spans from the
year 1 up to and including the year 100, the second - from the year 101 up to
and including the year 200, etc.
'''


def centuryFromYear(year):
    if year % 100 == 0:
        return year/100
    else:
        return year//100 + 1
