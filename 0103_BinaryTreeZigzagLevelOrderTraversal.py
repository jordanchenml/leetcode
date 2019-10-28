'''
Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q = [[root]]
        for level in q:
            record = []
            for node in level:
                if node.left:
                    record.append(node.left)
                if node.right:
                    record.append(node.right)
            if record:
                q.append(record)

        #zigzag order
        res = []
        for index, level in enumerate(q):
            tmp = [x.val for x in level]
            if index % 2 == 0:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
        return res



if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    rightLeft = TreeNode(15)
    rightRight = TreeNode(7)
    root.left = left
    root.right = right
    right.left = rightLeft
    right.right = rightRight

    a = Solution()
    print(a.zigzagLevelOrder(root))