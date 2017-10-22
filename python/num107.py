#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-22 12:24:54
# @Author  : David:admin@dxscx.com
# @Link    : http://blog.dxscx.com
# @Version : 1.0

"""


Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        >>> Solution().levelOrderBottom(Solution.construct_tree([3,9,20,None,None,15,7]))
        [[15, 7], [9, 20], [3]]
        """
        if not root:
            return []
        result=[]
        current_level_nodes=[root]
        while current_level_nodes:
            next_level_nodes=[]
            result.append([])
            for x in current_level_nodes:
                if x and x.val is not None:
                    next_level_nodes.append(x.left)
                    next_level_nodes.append(x.right)
                    result[-1].append(x.val)
            current_level_nodes=next_level_nodes
        return result[len(result)-2::-1]

    # just for test
    @classmethod
    def construct_tree(cls,nodes):
        
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
        root=TreeNode(nodes[0])
        pointer=1
        current_level_nodes=[root]
        while pointer <len(nodes):
            next_level_nodes=[]
            for node in current_level_nodes:
                if pointer>=len(nodes):
                    return root
                node.left=TreeNode(nodes[pointer])
                next_level_nodes.append(node.left)
                pointer+=1
                if pointer>=len(nodes):
                    return root
                node.right=TreeNode(nodes[pointer])
                next_level_nodes.append(node.right)
                pointer+=1
            current_level_nodes=next_level_nodes
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
                next_level_nodes.append(None if not x else x.left)
                next_level_nodes.append(None if not x else x.right)
                result.append(None if not x or not x.left else x.left.val)
                result.append(None if not x or not x.right else x.right.val)
            current_level_nodes=next_level_nodes
        # remove None
        while not result[-1]:
            result.pop()
        return result
        


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
