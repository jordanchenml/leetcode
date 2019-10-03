'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
'''

# Time Limit Exceeded
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        cnt = 0
        ugly = 0
        while cnt < n:
            ugly = ugly + 1
            if self.isUgly(ugly):
                cnt = cnt + 1
            ugly = ugly + 1
        return ugly

    def isUgly(self, num: int) -> bool:
        for i in 2, 3, 5:
            while num % i == 0 < num:
                num = num / i
        return num == 1

class Solution1:
    def nthUglyNumber(self, n: int) -> int:
        if n < 0:
            return 0
        dp = [1] * n
        two, three, five = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(2 * dp[two], 3 * dp[three], 5 * dp[five])
            if dp[i] == 2 * dp[two]:
                two += 1
            if dp[i] == 3 * dp[three]:
                three += 1
            if dp[i] == 5 * dp[five]:
                five += 1
        return dp [-1]