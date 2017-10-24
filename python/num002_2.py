#!/usr/bin/env python
# encoding: utf-8

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num002_2.py 
@time: 2017/9/27 12:25 
@description: 
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
        >>> Solution.get_num_str_from_node(Solution().addTwoNumbers(Solution.construct_nodes("5"), Solution.construct_nodes("5")))
        10
        """
        head = current_node = ListNode(0)
        ten_digit = 0
        while l1 or l2 or ten_digit:
            temp_sum = ten_digit
            if l1:
                temp_sum += l1.val
                l1 = l1.next
            if l2:
                temp_sum += l2.val
                l2 = l2.next
            digit, ten_digit = temp_sum % 10, temp_sum / 10
            current_node.next = ListNode(digit)
            current_node = current_node.next
        return head.next

    # just for test
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
