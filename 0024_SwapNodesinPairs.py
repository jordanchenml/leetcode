'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be c
hanged.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next or cur.next.next:
            first = cur.next
            second = cur.next.next
            cur.next = second
            first.next = second.next
            second.next = first
            cur = cur.next.next
        return dummy.next


# Recursive
class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_head)
        return head
