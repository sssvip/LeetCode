#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num665.py 
@time: 2017/11/9 11:48 
@description: 


Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 
4
 to 
1
 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].

"""


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        >>> print Solution().checkPossibility([1,4,3])
        True
        >>> print Solution().checkPossibility([4,2,1])
        False
        >>> print Solution().checkPossibility([4,2,3])
        True
        >>> print Solution().checkPossibility([2,3,3,2,4])
        True
        """
        for x in range(1, len(nums)):
            if nums[x] < nums[x - 1]:
                # replace element
                temp = nums[x]
                nums[x] = nums[x - 1]
                if self.check(nums):
                    return True
                else:
                    nums[x - 1] = nums[x] = temp
                    return self.check(nums)
        return True

    def check(self, nums):
        for x in range(1, len(nums)):
            if nums[x] < nums[x - 1]:
                return False
        return True


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
