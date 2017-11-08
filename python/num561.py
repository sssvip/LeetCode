#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num561.py 
@time: 2017/11/8 17:34 
@description: 

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

"""


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> print Solution().arrayPairSum([1, 2, 3, 4, 5, 6])
        9
        >>> print Solution().arrayPairSum([1, 2, 3, 4, 5, 6, 7, 8])
        16
        """
        snums = sorted(nums)
        return sum(snums[::2])


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
