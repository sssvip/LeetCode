#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num067.py 
@time: 2017/10/8 15:53 
@description: 

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        >>> Solution().addBinary("11","1")
        '100'
        """
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
