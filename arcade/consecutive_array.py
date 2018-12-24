# -*- coding:utf-8 -*-
# @Script: consecutive_array.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2018-12-20 20:59:38
# @Last Modified By: Pradip Patil
# @Last Modified: 2018-12-20 21:00:01
# @Description: https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC


def makeArrayConsecutive2(statues):
    available_sizes = set(statues)
    min_size = min(available_sizes)
    max_size = max(available_sizes)
    return len(set(range(min_size, max_size)) - available_sizes)


'''Shorter versions
def makeArrayConsecutive2(statues):
    return max(statues) - min(statues) - len(statues) + 1

'''
