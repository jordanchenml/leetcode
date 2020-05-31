'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
'''

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursively
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.ret = []
        self.helper(root)
        return self.ret

    def helper(self, root):
        if root:
            self.ret.append(root.val)
            self.helper(root.left)
            self.helper(root.right)

#iteratively
class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        while(stack):
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
