'''
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        last = self.generateParenthesis(n - 1)
        res = []
        for t in last:
            curr = t + ')'
            for i in range(len(curr)):
                if curr[i] == ')':
                    res.append(curr[:i] + '(' + curr[i:])
        return list(set(res))

if __name__ == '__main__':
    a = Solution()
    print(a.generateParenthesis(53))
