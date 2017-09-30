#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-30 18:46:56
# @Author  : David:admin@dxscx.com
# @Link    : http://blog.dxscx.com
# @Version : 1.0

"""
Determine whether an integer is a palindrome. Do this without extra space.

"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        >>> Solution().isPalindrome(123321)
        True
        >>> Solution().isPalindrome(1233212)
        False
        """
        #return x>=0 and x==int(str(x)[::-1])
        return str(x)==str(x)[::-1]



    # def isPalindrome(self, x):
    #     """
    #     :type x: int
    #     :rtype: bool
    #     >>> Solution().isPalindrome(123321)
    #     True
    #     >>> Solution().isPalindrome(1233212)
    #     False
    #     """
    #     x=str(x)
    #     for index in xrange(len(x)):
    #         if index>=len(x)/2:
    #             return True
    #         if x[index] !=x[len(x)-index-1]:
    #             return False
    #     return True
        


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)