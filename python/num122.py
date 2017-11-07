#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num122.py 
@time: 2017/11/7 19:51 
@description: 

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        >>> Solution().maxProfit([1,2,4])
        3
        >>> Solution().maxProfit([1,2,3,4,5,6,1,4,1])
        8
        """
        if not prices:
            return 0
        max_profit = 0
        for x in range(1, len(prices)):
            diff = prices[x] - prices[x - 1]
            if diff > 0:
                max_profit += diff
        return max_profit


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
