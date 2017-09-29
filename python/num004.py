#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-29 18:23:23
# @Author  : David:admin@dxscx.com
# @Link    : http://blog.dxscx.com
# @Version : 1.0


"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        >>> print Solution().findMedianSortedArrays([1,3],[2])
        2
        >>> print Solution().findMedianSortedArrays([1,2],[3,4])
        2.5
        """
        m,n=len(nums1),len(nums2)
        even_count=0
        if (m+n) % 2==0:
            even_count=1
        median_index=(m+n)/2+even_count
        i,j=0,0
        while i+j<median_index+1:
            if i+j>=median_index:
                ans=min(nums1[i],nums2[j])
                if not even_count:
                    return ans
                else:
                    return (ans+min(nums1[i],nums2[j]))/2
            if i > m-1:
                j+=1
            elif j > n-1:
                i+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1

        


if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)