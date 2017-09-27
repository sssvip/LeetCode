#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num002.py 
@time: 2017/9/27 9:21 
@description: 

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        >>> Solution.get_num_str_from_node(Solution().addTwoNumbers(Solution.construct_nodes("123"), Solution.construct_nodes("123")))
        642
        >>> Solution.get_num_str_from_node(Solution().addTwoNumbers(Solution.construct_nodes("123123"), Solution.construct_nodes("123123")))
        642642
        """
        num1, num2 = self.get_num_str_from_node(l1), self.get_num_str_from_node(l2)
        total = num1 + num2
        return self.construct_nodes(str(total)[::-1])

    @classmethod
    def get_num_str_from_node(cls, node):
        """
        implement by list (str is alternative)
        :param node: 
        :return: 
        """
        result = list()  # support long node
        while node is not None:
            result.append(str(node.val))
            node = node.next
        return int("".join(result[::-1]))

    @classmethod
    def construct_nodes(cls, num_str):
        """
        :param num_str: not allow None or ""
        :return: 
        """
        head = ListNode(num_str[0])
        current_node = head
        for x in num_str[1:]:
            current_node.next = ListNode(x)
            current_node = current_node.next
        return head


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
