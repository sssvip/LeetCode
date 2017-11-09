#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num219.py 
@time: 2017/11/9 11:36 
@description: 

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        >>> Solution().containsNearbyDuplicate([1,2,3,4,5,2],5)
        True
        """
        used_nums = {}
        for x in range(len(nums)):
            if nums[x] in used_nums and x - used_nums[nums[x]] <= k:
                return True
            used_nums[nums[x]] = x
        return False


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
