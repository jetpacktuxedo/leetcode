"""
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1, list2 = ([], [])
        # convert this dumb linked list into a real list
        while l1 or l2:
            if l1:
                # add the digits to the front of the lists to reverse the order
                list1.insert(0, str(l1.val))
                l1 = l1.next
            if l2:
                list2.insert(0, str(l2.val))
                l2 = l2.next

        # pretty sure this isn't the intended solution lol. Collapse the lists
        # down into ints, sum them, and then reverse that process
        outlist = list(str(int(''.join(list1)) + int(''.join(list2))))

        # convert the list back into a ListNode object
        old_lout = None
        for digit in outlist:
            lout = ListNode(int(digit))
            lout.next = old_lout
            old_lout = lout
        return lout
