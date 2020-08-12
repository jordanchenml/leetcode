'''
Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = ListNode()
        dummy = prev
        prev.next = head
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next

class Solution2:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head