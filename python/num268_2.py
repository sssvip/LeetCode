#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num268.py 
@time: 2017/11/6 16:38 
@description: 

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> print Solution().missingNumber([0]) 
        1
        >>> print Solution().missingNumber([0,1,2]) 
        3
        >>> print Solution().missingNumber([0,1,3]) 
        2
        """
        return sum(xrange(len(nums) + 1)) - sum(nums)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
