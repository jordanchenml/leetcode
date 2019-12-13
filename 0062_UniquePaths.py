'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the
diagram below).

The robot can only move either down or right at any point in time. The robot is
trying to reach the bottom-right corner of the grid (marked 'Finish' in the
diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:
Input: m = 3, n = 2
Output: 3

Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right
corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right


Example 2:
Input: m = 7, n = 3
Output: 28
'''

import math


# DP
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


# Formula
class Solution1:
    def uniquePaths1(self, m: int, n: int) -> int:
        return int(math.factorial(m + n - 2) / (
                math.factorial(m - 1) * math.factorial(n - 1)))


# Recursive
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]
        return self.dfs(m - 1, n - 1, memo)

    def dfs(self, m, n, memo):
        if m == 0 or n == 0:
            return 1
        if memo[m][n]:
            return memo[m][n]
        up = self.dfs(m - 1, n, memo)
        left = self.dfs(m, n - 1, memo)
        memo[m][n] = up + left
        return memo[m][n]


if __name__ == '__main__':
    a = Solution()
    print(a.uniquePaths(7, 3))
