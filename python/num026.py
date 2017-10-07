#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num026.py 
@time: 2017/10/7 15:14 
@description: 

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> a=[1,2,3,3,5,5,6]
        >>> Solution().removeDuplicates(a)
        5
        >>> print a
        [1, 2, 3, 5, 6, 5, 6]
        >>> Solution().removeDuplicates([1,1,1])
        1
        """
        if not nums:
            return 0
        pre_num = nums[0]
        total = 1
        inplace_pointer = 1
        for x in nums:
            if x != pre_num:
                total += 1
                nums[inplace_pointer] = x
                inplace_pointer += 1
            pre_num = x
        return total


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
