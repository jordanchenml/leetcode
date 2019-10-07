'''
Given a non-negative index k where k ≤ 33,
return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

Example:
Input: 3
Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?
'''

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        res.append([1])
        res.append([1, 1])
        if rowIndex == 0:
            return res[0]
        if rowIndex == 1:
            return res[1]
        for i in range(2, rowIndex + 1):
            new = []
            new.append(1)
            for i in range(len(res[-1]) - 1):
                new.append(res[-1][i] + res[-1][i + 1])
            new.append(1)
            res.append(new)
        return res[-1]


class Solution1:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row


a = Solution1()
print(a.getRow(3))
