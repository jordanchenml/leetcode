'''
Given two binary trees, write a function
to check if they are the same or not.

Two binary trees are considered the same
if they are structurally identical and the
nodes have the same value.

# Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''

# Definition for a binary tree node.

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

# DFS
class Solution1:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q: return p == q
        if p.val != q.val: return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right

#Stack
class Solution2:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2: continue
            if not n1 or not n2: return n1 == n2
            if n1.val != n2.val: return False
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        return True

#Queue
class Solution3:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = collections.deque([(p, q)])
        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2: continue
            if not n1 or not n2: return n1 == n2
            if n1.val != n2.val: return False
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
        return True



