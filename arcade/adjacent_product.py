# -*- coding:utf-8 -*-
# @Script: adjacent_product.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2018-12-18 00:13:22
# @Last Modified By: Pradip Patil
# @Last Modified: 2018-12-18 00:22:41
# @Description: https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m
'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
'''


def adjacentElementsProduct(inputArray):
    max_product = None
    for i in range(0, len(inputArray)-1):
        product = inputArray[i] * inputArray[i+1]
        if max_product is None:
            max_product = product
        elif max_product < product:
            max_product = product
        else:
            continue
    return max_product


'''Shorter versions:

def adjacentElementsProduct(inputArray):
    return max(a * b for a, b in zip(inputArray[:-1], inputArray[1:]))

def adjacentElementsProduct(inputArray):
    return max(inputArray[i] * inputArray[i+1] for i in range(0, len(inputArray)-1)))

'''
