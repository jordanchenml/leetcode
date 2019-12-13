'''
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


# Recursive
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# Dynamic Programming
# Bottom Up
class Solution1:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        res = [-1] * n
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]
        return res[-1]


# Dynamic Programming
# Top Down
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        table = [0] * (n + 1)
        table[0] = 1
        table[1] = 1
        i = 2
        while i <= n:
            if not table[i]:
                table[i] = table[i - 1] + table[i - 2]
            i += 1

        print(table)
        return table[n]


class Solution3:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [1] * 2
        for i in range(2, n + 1):
            dp[1], dp[0] = dp[1] + dp[0], dp[1]
            print(dp[1], dp[0])
        return dp[1]


class Solution4:
    def __init__(self):
        self.memo = {0: 0, 1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        left = self.climbStairs(n - 1)
        self.memo[n - 1] = left
        right = self.climbStairs(n - 2)
        self.memo[n - 2] = right
        return left + right

if __name__ == '__main__':
    a = Solution2()
    print(a.climbStairs(6))
