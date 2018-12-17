# -*- coding:utf-8 -*-
# @Script: solution.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2018-12-16 15:34:56
# @Last Modified By: Pradip Patil
# @Last Modified: 2018-12-17 23:55:31
# @Description: https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q


def firstDuplicate(a):
    seen = set()
    for n in a:
        if n in seen:
            return n
        else:
            seen.add(n)
    return -1
