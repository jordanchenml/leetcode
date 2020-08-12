'''
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively.
Could you implement both?
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

# Recursive
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head)

    def reverse(self, node, prev = None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self.reverse(n, node)
