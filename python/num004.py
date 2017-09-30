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
        >>> print Solution().findMedianSortedArrays([1,2,3],[1,2])
        2
        >>> print Solution().findMedianSortedArrays([2,3],[])
        2.5
        >>> print Solution().findMedianSortedArrays([2,3],[1])
        2
        >>> print Solution().findMedianSortedArrays([1,3],[2])
        2
        >>> print Solution().findMedianSortedArrays([1,2],[3,4])
        2.5
        >>> print Solution().findMedianSortedArrays([2,2,2,2],[2,2,2])
        2
        >>> print Solution().findMedianSortedArrays([1],[1])
        1
        >>> print Solution().findMedianSortedArrays([2,2,2],[2,2,2,2])
        2
        """
        if not nums1:
            return self.deal_empty_array(nums2)
        if not nums2:
            return self.deal_empty_array(nums1)
        m,n=len(nums1),len(nums2)
        pre_num,after_num=0,0
        even=(m+n)%2-1
        #print "even"+str(even)
        median_index=(m+n)/2+(m+n)%2-even
        i,j=0,0
        while i+j<=median_index:
            i,j,pre_num,after_num=self.next_min(nums1,nums2,i,j)
            if i+j>=median_index-2:
                if even and pre_num!=after_num:
                    return (pre_num+after_num)/2.0
                else:
                    return pre_num
            # slide pointer·
            # pre_num,after_num=nums1[i],nums2[j]

    def next_min(self,nums1,nums2,i,j):
        current_min=max(nums1[i],nums2[j])
        m,n=len(nums1),len(nums2)
        if i>=m-1 and j>=n-1:
            return i,j,current_min,current_min
        if i>=m-1:
            j+=1
            return i,j,current_min,nums2[j]
        if j>=n-1:
            i+=1
            return i,j,current_min,nums1[i]
        if nums1[i+1]<=nums2[j+1]:
            i+=1
        else:
            j+=1
        return i,j,current_min,min(nums1[i],nums2[j])

    def deal_empty_array(self,nums):
        n=len(nums)
        if n%2==0:
            return (nums[n/2-1]+nums[n/2])/2.0
        else:
            return nums[n/2]
        


if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
    #print Solution().next_min([1,2,3],[1,2],0,1)