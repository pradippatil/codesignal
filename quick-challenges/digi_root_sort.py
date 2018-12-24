# -*- coding:utf-8 -*-
# @Script: solution.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2018-12-15 22:42:08
# @Last Modified By: Pradip Patil
# @Last Modified: 2018-12-15 22:42:35
# @Description: https://app.codesignal.com/skill-test/cSs5ucjzWqSoD6Dbu


def digitRootSort(a):

    digit_root = dict()

    for n in a:
        for i in str(n):
            if n in digit_root:
                digit_root[n] += int(i)
            else:
                digit_root[n] = int(i)

    print(digit_root)

    digit_root_transpose = dict()

    for k, v in digit_root.items():
        if v in digit_root_transpose:
            digit_root_transpose[v].append(k)
        else:
            digit_root_transpose[v] = [k]
    sorted_digit_root = list()

    for k, v in sorted(digit_root_transpose.items()):
        sorted_digit_root.extend(sorted(v))
    return sorted_digit_root
