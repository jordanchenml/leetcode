'''
Given a non-negative integer numRows, generate
the first numRows of Pascal's triangle.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = []
        res.append([1])
        res.append([1, 1])
        for i in range(2, numRows):
            new = []
            new.append(1)
            for i in range(len(res[-1]) - 1):
                new.append(res[-1][i] + res[-1][i + 1])
            new.append(1)
            res.append(new)
        return res

class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            result.append([0] * (i + 1))
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    result[i][j] = 1
                else:
                    result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result

a = Solution()
print(a.generate(6))