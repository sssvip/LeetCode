#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num58.py 
@time: 2017/10/8 15:05 
@description: 

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        >>> Solution().lengthOfLastWord(" ")
        0
        >>> Solution().lengthOfLastWord("a ")
        1
        """
        total = 0
        for x in s[::-1]:
            if x == ' ':
                if not total:
                    continue
                return total
            total += 1
        return total


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
