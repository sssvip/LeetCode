#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-28 22:25:36
# @Author  : David:admin@dxscx.com)
# @Link    : http://blog.dxscx.com
# @Version : 1.0

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        >>> print Solution().lengthOfLongestSubstring("bdbf")
        3
        >>> print Solution().lengthOfLongestSubstring("abcdd")
        4
        """
        max_length=0
        pre_substr=""
        for x in s:
        	indexof=pre_substr.find(x)
        	if indexof>=0:
    			pre_substr=pre_substr[indexof+1:]
    		pre_substr=pre_substr + x
    		max_length=max(max_length,len(pre_substr))
    	return max_length


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
	#print Solution().lengthOfLongestSubstring("abcdd")