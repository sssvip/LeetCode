#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num217.py 
@time: 2017/11/8 17:47 
@description: 

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.



"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        >>> print Solution().containsDuplicate([1,2,3,21])
        False
        >>> print Solution().containsDuplicate([1,2,3,21,1])
        True
        """
        return len(set(nums)) != len(nums)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
