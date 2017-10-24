#!/usr/bin/env python
# encoding: utf-8

""" 
@version: v1.0 
@author: David 
@contact: tangwei@newrank.cn
@file: num021.py 
@time: 2017/10/6 17:25 
@description: 

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

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

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        >>> Solution.get_num_str_from_node(Solution().mergeTwoLists(Solution.construct_nodes("1258"),Solution.construct_nodes("1256")))
        11225568
        >>> Solution.get_num_str_from_node(Solution().mergeTwoLists(Solution.construct_nodes("123"),Solution.construct_nodes("123")))
        112233
        >>> print Solution().mergeTwoLists(Solution.construct_nodes("123"),Solution.construct_nodes("123"))
        1->1->2->2->3->3
        """
        head = ListNode(0)
        current_node = head
        i, j = l1, l2  # two pointer
        self.temp_node = None
        while i or j:
            # has ListNode was empty
            if i and not j:
                current_node.next = i
                current_node = current_node.next
                i = i.next
                continue
            if j and not i:
                current_node.next = j
                current_node = current_node.next
                j = j.next
                continue
            # slide pointer
            if i.val < j.val:
                current_node.next = i
                current_node = current_node.next
                i = i.next
            else:
                current_node.next = j
                current_node = current_node.next
                j = j.next
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
        return int("".join(result))

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
