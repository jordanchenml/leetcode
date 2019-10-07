'''
For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
'''

from typing import List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # dfs recursively
    def levelOrderBottom1(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level + 1)].append(root.val)
            self.dfs(root.left, level + 1, res)
            self.dfs(root.right, level + 1, res)

    # dfs + stack
    def levelOrderBottom2(self, root: TreeNode) -> List[List[int]]:
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level + 1)].append(node.val)
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        return res

    # bfs + queue
    def levelOrderBottom3(self, root: TreeNode) -> List[List[int]]:
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level + 1)].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return res

    def levelOrderBottom4(self, root: TreeNode) -> List[List[int]]:
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if level == len(res):
                    res.append([])
                res[level].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return res[::-1]

    def levelOrderBottom5(self, root: TreeNode) -> List[List[int]]:
        res, queue = [], [root]
        while queue:
            res.append([node.val for node in queue if node])
            queue = [child for node in queue if node for child in
                     (node.left, node.right)]
        return res[-2::-1]
