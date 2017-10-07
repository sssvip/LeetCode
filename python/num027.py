#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num027.py 
@time: 2017/10/7 15:42 
@description: 

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        >>> a=[3,2,2,3]
        >>> Solution().removeElement(a,3)
        2
        >>> a[0]==2,a[1]==2
        (True, True)
        >>> Solution().removeElement([1],1)
        0
        >>> Solution().removeElement([2,2,3],2)
        1
        >>> Solution().removeElement([3,3],3)
        0
        """
        if not nums:
            return 0
        pointer = 0
        for x in nums:
            if x != val:
                nums[pointer] = x
                pointer += 1
        return pointer


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
