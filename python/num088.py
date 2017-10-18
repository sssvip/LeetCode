#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-18 20:28:40
# @Author  : David:admin@dxscx.com
# @Link    : http://blog.dxscx.com
# @Version : 1.0

"""

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        >>> a,b=[1,2,3,4,5,5,5,5,0,0,0,0,0,0,0],[1,2,3,3,3,4,5]
        >>> Solution().merge(a,8,b,7)
        >>> print a
        [1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5]
        """
        while n>0:
            if m>0 and nums1[m-1]>nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m-=1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
                


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)