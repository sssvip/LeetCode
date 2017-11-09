#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num643.py 
@time: 2017/11/9 14:20 
@description: 


Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        >>> Solution().findMaxAverage([1,12,-5,-6,50,3],4)
        12.75
        >>> Solution().findMaxAverage([4,0,4,3,3],5)
        2.8
        >>> Solution().findMaxAverage([0,1,1,3,3],4)
        2.0
        """
        if not nums:
            return 0
        max_sum = sum(nums[:k])
        temp_sum = max_sum
        for x in range(1, len(nums) - k + 1):
            temp_sum = temp_sum - nums[x - 1] + nums[x + k - 1]
            max_sum = max(temp_sum, max_sum)
        return max_sum / float(k)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
