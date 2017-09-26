#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num001.py 
@time: 2017/9/26 16:32 
@description: 
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        >>> Solution().twoSum([2, 7, 11, 15], 9)
        [0, 1]
        """
        complement_map = {}
        for index, x in enumerate(nums):
            if complement_map.get(x, None) is None:
                complement_map[target - x] = index
            else:
                return [complement_map.get(x), index]


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
