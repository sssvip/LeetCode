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
        result = [[1]]
        if numRows < 1:
            return []
        for level in range(numRows - 1):
            self.gen_level_arr(result)
        return result

    def gen_level_arr(self, nums):
        """
        1331==> 01331+13310 ==> 14641
        :param nums: 
        :return: 
        """
        num1 = [0] + nums[-1]
        num2 = nums[-1] + [0]
        nums.append([num1[i] + num2[i] for i in range(len(num1))])


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
