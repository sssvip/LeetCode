#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-30 20:15:21
# @Author  : David:admin@dxscx.com
# @Link    : http://blog.dxscx.com
# @Version : 1.0

"""
Write a function to find the longest common prefix string amongst an array of strings.

Seen this question in a real interview before? 
"""


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        >>> Solution().longestCommonPrefix(["a"])
        a
        """
        if not strs:
            return ""
        ans = ""
        # O(m) m==>the length longest prefix str
        for index in xrange(len(strs[0])):
            temp_char = ''
            for x in strs:  # O(n)
                if index <= len(x) - 1 and temp_char == '':
                    temp_char = x[index]
                # fast break==> the reason of O(m*n)
                if index >= len(x) or x[index] != temp_char:
                    return ans
            ans += temp_char
        return ans

if __name__ == '__main__':
    #import doctest
    # doctest.testmod(verbose=True)
    print Solution().longestCommonPrefix(["abcc", "abcd", "abcs"])
