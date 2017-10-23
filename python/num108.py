#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-22 17:42:05
# @Author  : David:admin@dxscx.com
# @Link    : http://blog.dxscx.com
# @Version : 1.0

"""

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        >>> print Solution.tree_to_array(Solution().sortedArrayToBST([1,2,3,4,5,6]))
        [4, 2, 6, 1, 3, 5]
        >>> print Solution.tree_to_array(Solution().sortedArrayToBST([-1,0,1,2]))
        [1, 0, 2, -1]
        >>> print Solution.tree_to_array(Solution().sortedArrayToBST([0,1,2,3,4,5]))
        [3, 1, 5, 0, 2, 4]
        """
        if not nums:
            return None
        mid=len(nums)/2
        root=TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])
        return root


    # just for test
    @classmethod
    def tree_to_array(cls,root):
        if not root:
            return []
        result=[]
        result.append(root.val)        
        current_level_nodes=[root]
        while any(current_level_nodes):
            next_level_nodes=[]
            for x in current_level_nodes:
                next_level_nodes.append(None if x is None else x.left)
                next_level_nodes.append(None if x is None else x.right)
                result.append(None if x is None or x.left is None else x.left.val)
                result.append(None if x is None or x.right is None else x.right.val)
            current_level_nodes=next_level_nodes
        # remove None
        while not result[-1]:
            result.pop()
        return result


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
