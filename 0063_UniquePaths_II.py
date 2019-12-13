'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the
diagram below).

The robot can only move either down or right at any point in time. The robot is
trying to reach the bottom-right corner of the grid (marked 'Finish' in the
diagram below).

Now consider if some obstacles are added to the grids. How many unique paths
would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''

from typing import List


# Recursive
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0] * n for _ in range(m)]
        return self.dfs(m - 1, n - 1, memo, obstacleGrid)

    def dfs(self, m, n, memo, obstacleGrid):
        if obstacleGrid[m][n] == 1:
            return 0
        if m < 0 or n < 0:
            return 0
        if m == n == 0:
            return 1
        if memo[m][n]:
            return memo[m][n]
        up = self.dfs(m - 1, n, memo, obstacleGrid)
        left = self.dfs(m, n - 1, memo, obstacleGrid)
        memo[m][n] = up + left
        return memo[m][n]


# DP
class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i is not 0:
                        dp[i][j] += dp[i - 1][j]
                    if j is not 0:
                        dp[i][j] += dp[i][j - 1]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    a = Solution1()
    print(a.uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
