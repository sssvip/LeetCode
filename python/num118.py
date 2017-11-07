#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num118.py 
@time: 2017/11/7 16:20 
@description: 

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        >>> Solution().generate(2)
        [[1], [1, 1]]
        >>> Solution().generate(3)
        [[1], [1, 1], [1, 2, 1]]
        >>> Solution().generate(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        """
        result = []
        if numRows < 1:
            return result
        for level in range(1, numRows + 1):
            self.gen_level_arr(result, level)
        return result

    def gen_level_arr(self, nums, level):
        result = [1] * level
        if level <= 2:
            nums.append(result)
        else:
            for x in range(1, len(result) / 2 + 1):
                temp_nums = nums[level - 2]
                result[x] = temp_nums[x - 1] + temp_nums[x]
                result[level - 1 - x] = temp_nums[x - 1] + temp_nums[x]
            nums.append(result)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
