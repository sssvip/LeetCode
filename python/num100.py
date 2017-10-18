#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-18 21:02:23
# @Author  : David:admin@dxscx.com
# @Link    : http://blog.dxscx.com
# @Version : 1.0

"""

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        >>> root=TreeNode(10)
        >>> root.left=TreeNode(11)
        >>> root.right=TreeNode(12)
        >>> test_root=TreeNode(10)
        >>> test_root.left=TreeNode(11)
        >>> test_root.right=TreeNode(12)
        >>> print Solution().isSameTree(root,test_root)
        True
        >>> test_root.left.left=TreeNode(13)
        >>> print Solution().isSameTree(root,test_root)
        False
        """
        if p and q:
            if p.val != q.val:
                return False
        elif not p and not q:
            return True
        else:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)