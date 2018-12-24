# -*- coding:utf-8 -*-
# @Script: first_non_repeating_character.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2018-12-21 00:34:02
# @Last Modified By: Pradip Patil
# @Last Modified: 2018-12-24 21:58:07
# @Description: https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC


def firstNotRepeatingCharacter(s):
    seen = set()
    for i, c in enumerate(s):
        if c not in seen and c not in s[i+1:]:
            return c
        seen.add(c)
    return '_'


'''Alternative version

def firstNotRepeatingCharacter(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'

'''
