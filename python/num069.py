#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num069.py 
@time: 2017/10/9 15:00 
@description: 

Implement int sqrt(int x).

Compute and return the square root of x.

"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        >>> Solution().mySqrt(0)
        0
        """
        # import math
        # return int(math.sqrt(x))
        return int(x ** 0.5)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
