#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-26 20:50:01
# @Author  : David:admin@dxscx.com
# @Link    : http://blog.dxscx.com
# @Version : 1.0

"""

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

"""


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "node.val->%s  node.left:%s  node.right:%s" % (self.val, self.left, self.right)


class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        >>> print Solution().minDepth(Solution.construct_tree([1, 2, 3, 4, None, None, 5]))
        3
        >>> print Solution().minDepth(Solution.construct_tree([0]))
        1
        """
        if not root:
            return 0
        return self.deal_level([root])

    def deal_level(self, nodes):
        next_level_nodes = []
        for node in nodes:
            if node.left is None and node.right is None:
                return 1
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)
        return self.deal_level(next_level_nodes) + 1

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

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
