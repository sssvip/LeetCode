#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num083.py 
@time: 2017/10/17 11:25 
@description: 

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        result = "{}".format(self.val)
        current_node = self.next
        while current_node:
            result += "->{}".format(current_node.val)
            current_node = current_node.next
        return result


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        >>> print Solution().deleteDuplicates(Solution.construct_nodes("11223"))
        1->2->3
        >>> print Solution().deleteDuplicates(Solution.construct_nodes("112235677"))
        1->2->3->5->6->7
        >>> print Solution().deleteDuplicates(Solution.construct_nodes("1122356778"))
        1->2->3->5->6->7->8
        """
        if not head:
            return []
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    # just for test
    @classmethod
    def construct_nodes(cls, num_str):
        """
        :param num_str: not allow None or ""
        :return: 
        """
        head = ListNode(int(num_str[0]))
        current_node = head
        for x in num_str[1:]:
            current_node.next = ListNode(int(x))
            current_node = current_node.next
        return head


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
