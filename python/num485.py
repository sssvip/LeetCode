#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num485.py 
@time: 2017/11/10 10:41 
@description: 

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> print Solution().findMaxConsecutiveOnes([1,1,0,1,1,1])
        3
        """
        max_sum = 0
        temp_sum = 0
        for x in nums:
            if x == 0:
                max_sum = max(max_sum, temp_sum)
                temp_sum = 0
            else:
                temp_sum += 1
        return max(max_sum, temp_sum)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
