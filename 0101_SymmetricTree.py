'''
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.mirrorVisit(root.left, root.right)

    def mirrorVisit(self, left, right):
        if left is None and right is None:
            return True
        try:
            if left.val == right.val:
                if self.mirrorVisit(left.left, right.right) and self.mirrorVisit(left.right, right.left):
                    return True
            return False
        except:
            return False
