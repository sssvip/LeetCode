#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-21 12:34:23
# @Author  : David:admin@dxscx.com
# @Link    : http://blog.dxscx.com
# @Version : 1.0

"""

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""

# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        >>> print Solution().maxDepth(Solution.construct_tree([1,2,3,4]))
        3
        >>> print Solution().maxDepth(Solution.construct_tree([1,2,3,4,4,4,4,4]))
        4
        """
        if not root:
            return 0
        return self.travel(root, 1)

    def travel(self, node, current_depth):
        if not node:
            return current_depth
        result = current_depth
        if node.left:
            result = max(self.travel(node.left, current_depth + 1), result)
        if node.right:
            result = max(self.travel(node.right, current_depth + 1), result)
        return result

    # just for test
    @classmethod
    def construct_tree(cls, nodes):
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
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        pointer = 1
        current_level_nodes = [root]
        while pointer < len(nodes):
            next_level_nodes = []
            for node in current_level_nodes:
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
