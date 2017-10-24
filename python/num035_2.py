#!/usr/bin/env python
# encoding: utf-8

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num35.py 
@time: 2017/10/7 16:35 
@description: 

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

"""


class Solution(object):

    def searchInsert(self, nums, target):
        """
        Time: O(log(n))
        Space: O(1) 
        :type nums: List[int]
        :type target: int
        :rtype: int
        >>> Solution().searchInsert([0,1,2,4,56],5)
        4
        >>> Solution().searchInsert([1,3,5,6],5)
        2
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
