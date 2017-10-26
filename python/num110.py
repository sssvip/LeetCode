#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-23 22:52:34
# @Author  : David:admin@dxscx.com
# @Link    : http://blog.dxscx.com
# @Version : 1.0

"""

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

"""


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isBalanced(self, root):
        """
        >>> print Solution().isBalanced(Solution.construct_tree([1,2,3,4,5,6,7]))
        True
        >>> print Solution().isBalanced(Solution.construct_tree([1,2,2,3,4,4,3]))
        True
        """
        if not root:
            return True
        self.error = -999
        return self.check(root) != self.error

    def check(self, root):
        if root is None:
            return 0
        left = self.check(root.left)
        right = self.check(root.right)
        if left == self.error or right == self.error or abs(left - right) > 1:
            return self.error
        return 1 + max(left, right)

    # just for test
    @classmethod
    def construct_tree(cls, nodes_array):
        """
        :type nodes: List [1,2,2,3,4,4,3] 

        :rtype: the root of tree representation use node 
        construct result:
            1
           / \
          2   2
         / \ / \
        3  4 4  3
        """
        nodes = nodes_array
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        pointer = 1
        current_level_nodes = [root]
        while pointer < len(nodes):
            next_level_nodes = []
            for node in current_level_nodes:
                if pointer >= len(nodes):
                    return root
                node.left = TreeNode(nodes[pointer])
                next_level_nodes.append(node.left)
                pointer += 1
                if pointer >= len(nodes):
                    return root
                node.right = TreeNode(nodes[pointer])
                next_level_nodes.append(node.right)
                pointer += 1
            current_level_nodes = next_level_nodes
        return root

    # just for test
    @classmethod
    def tree_to_array(cls, root):
        if not root:
            return []
        result = []
        result.append(root.val)
        current_level_nodes = [root]
        while any(current_level_nodes):
            next_level_nodes = []
            for x in current_level_nodes:
                next_level_nodes.append(None if not x else x.left)
                next_level_nodes.append(None if not x else x.right)
                result.append(None if not x or not x.left else x.left.val)
                result.append(None if not x or not x.right else x.right.val)
            current_level_nodes = next_level_nodes
        # remove None
        while not result[-1]:
            result.pop()
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
