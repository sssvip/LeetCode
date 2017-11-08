#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num581.py 
@time: 2017/11/7 20:29 
@description: 

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        >>> print Solution().findUnsortedSubarray([1,2,3,4])
        0
        >>> print Solution().findUnsortedSubarray([1,3,2,1,5,6])
        3
        >>> print Solution().findUnsortedSubarray([2,6,4,8,10,9,15])
        5
        """
        n = len(nums)
        if n < 1:
            return 0
        snums = sorted(nums)
        start = 0
        end = 0
        for x in range(n):
            if snums[x] != nums[x]:
                start = x
                break
        for x in range(n):
            if snums[n - x - 1] != nums[n - x - 1]:
                end = n - x - 1
                break
        return end - start + 1 if (end - start) > 0 else 0


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
