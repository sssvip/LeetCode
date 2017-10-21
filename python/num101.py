#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-19 19:57:15
# @Author  : David:admin@dxscx.com
# @Link    : http://blog.dxscx.com
# @Version : 1.0

"""

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

        
                   1
               /      \
              2         2
            /   \     /   \
           3     4   4     3
          /\    /\   /\    /\    
         5 6   7  8 8  7  6  5   
        [1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]


But the following [1,2,2,None,3,None,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def children_count(self):
        count=0
        if self.left:
            count+=self.left.children_count()
        if self.right:
            count+=self.right.children_count()
        return count+1
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        >>> print Solution().isSymmetric(Solution.construct_tree([1,2,2,3,4,4,3]))
        True
        >>> print Solution().isSymmetric(Solution.construct_tree([1,2,3,3,4,4,3]))
        False
        """
        def mirror(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return (node1.val == node2.val) and (mirror(node1.left,node2.right)) and (mirror(node1.right,node2.left))
        return mirror(root,root)

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

    # Submission Result: Time Limit Exceeded
    # 185 / 193 test cases passed.
    def isSymmetric_deprecated(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        current_level_nodes=[root]
        while any(current_level_nodes):
            for index in range(len(current_level_nodes)/2):
                compare_node=current_level_nodes[-(index+1)]
                if not compare_node and current_level_nodes[index]:
                    return False
                if not current_level_nodes[index] and compare_node:
                    return False
                if current_level_nodes[index] and compare_node:
                    if current_level_nodes[index].val != compare_node.val:
                            return False
            next_level_nodes=[]
            for x in current_level_nodes:
                next_level_nodes.append(None if not x else x.left)
                next_level_nodes.append(None if not x else x.right)
            current_level_nodes=next_level_nodes
        return True

    
        

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
