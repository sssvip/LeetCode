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

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        >>> print Solution().maxProfit([1,2,3,4,5,6])
        5
        """
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for x in range(len(prices)):
            if prices[x] <= min_price:
                min_price = prices[x]
            elif prices[x] - min_price >= max_profit:
                max_profit = prices[x] - min_price
        return max_profit


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
