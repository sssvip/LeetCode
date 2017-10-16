#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num070.py 
@time: 2017/10/16 12:36 
@description: 

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        >>> Solution().climbStairs(1)
        1
        >>> Solution().climbStairs(2)
        2
        >>> Solution().climbStairs(3)
        3
        >>> Solution().climbStairs(4)
        5
        >>> Solution().climbStairs(5)
        8
        """
        cache = {}
        return self.calc(0, n, cache)

    def calc(self, i, n, cache):
        if i > n:
            return 0
        if i == n:
            return 1
        key = "{}->{}".format(i, n)
        if key not in cache:
            result = self.calc(i + 1, n, cache) + self.calc(i + 2, n, cache)
            cache[key] = result
            # print "{}:{}".format(key, result) # show the recurse process
            return result
        else:
            return cache[key]


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
    # Solution().climbStairs(100)
