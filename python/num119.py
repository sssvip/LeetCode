#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num119.py 
@time: 2017/11/7 19:28 
@description: 

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        >>> Solution().getRow(3)
        [1, 3, 3, 1]
        """
        if rowIndex < 1:
            return [1]
        result = []
        for x in range(rowIndex):
            result = self.gen_next_level_arr(result)
        return result

    def gen_next_level_arr(self, nums):
        if not nums:
            nums = [1]
        num1 = [0] + nums
        num2 = nums + [0]
        return [num1[i] + num2[i] for i in range(len(num1))]


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
