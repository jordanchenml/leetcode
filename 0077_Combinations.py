'''
Given two integers n and k, return all possible combinations of k numbers
out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(range(1, n + 1), k, res, [])
        return res

    def helper(self, array, k, res, path):
        if k > len(array):
            return
        if k == 0:
            res.append(path)
        else:
            for i in range(len(array)):
                self.helper(array[i + 1:], k - 1, res, path + [array[i]])


if __name__ == '__main__':
    a = Solution()
    print(a.combine(4, 2))