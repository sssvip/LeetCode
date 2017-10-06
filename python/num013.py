#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num013.py 
@time: 2017/10/6 16:57 
@description: 

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        >>> Solution().romanToInt("MCMXCVI")
        1996
        >>> Solution().romanToInt("X")
        10
        """
        ROMAN_INDEX = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        pre_char = None
        total = 0
        for x in s[::-1]:
            if pre_char and ROMAN_INDEX[pre_char] > ROMAN_INDEX[x]:
                total = total - ROMAN_INDEX[x]
            else:
                total += ROMAN_INDEX[x]
            pre_char = x
        return total


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
    # Solution().romanToInt("MCMXCVI")
