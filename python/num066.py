#!/usr/bin/env python
# encoding: utf-8

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num066.py 
@time: 2017/10/8 15:25 
@description: 

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

"""


class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        >>> Solution().plusOne([0])
        [1]
        """
        digits_str = "".join([str(i) for i in digits])
        return [int(i) for i in str(int(digits_str) + 1)]


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
