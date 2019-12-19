'''
Given n, how many structurally unique BST's (binary search trees) that store
values 1 ... n?

Example:
Input: 3
Output: 5

Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

这里有个解题技巧：一般来说求数量，要首先想到使用动态规划（dp），而如果是像下一题的要求，
不只是数量，还要把所有的树都枚举出来，就要使用dfs（深度优先搜索）来遍历决策树了
'''

import math

# Dynamic Programming
class Solution:
    def numTrees(self, n: int) -> int:
        res = [0] * (n + 1)
        res[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                res[i] += res[j] * res[i - 1 - j]
        return res[-1]

# Catalan Number  (2n)!/((n+1)!*n!)
class Solution1:
    def numTrees(self, n: int) -> int:
        return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))


if __name__ == '__main__':
    a = Solution()
    print(a.numTrees(3))