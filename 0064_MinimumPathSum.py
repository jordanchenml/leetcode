'''
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        r, c = len(grid), len(grid[0])
        for i in range(1, c):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, r):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] = min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]
        return grid[-1][-1]

    # O(m*n) space
    def minPathSum1(self, grid):
        if not grid:
            return
        r, c = len(grid), len(grid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0][0] = grid[0][0]
        for i in range(1, r):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, c):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

    # O(n) space
    def minPathSum2(self, grid):
        if not grid:
            return
        r, c = len(grid), len(grid[0])
        cur = [0] * c
        cur[0] = grid[0][0]
        for i in range(1, c):
            cur[i] = cur[i - 1] + grid[0][i]
        print(cur)
        for i in range(1, r):
            cur[0] += grid[i][0]
            for j in range(1, c):
                cur[j] = min(cur[j - 1], cur[j]) + grid[i][j]
        return cur[-1]

    # change the grid itself
    def minPathSum3(self, grid):
        if not grid:
            return
        r, c = len(grid), len(grid[0])
        for i in range(1, c):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, r):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


if __name__ == '__main__':
    a = Solution()
    print(a.minPathSum2([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
