'''
A sequence of numbers is called arithmetic if it consists of at least three
elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array
is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of the array A is called arithmetic if the sequence:
A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means
that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:
A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4]
itself.
'''

from typing import List


# Recursive
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        N = len(A)
        self.res = 0
        self.slices(A, N-1)
        return self.res

    def slices(self, A, end):
        if end < 2:
            return 0
        op = 0
        if A[end] - A[end - 1] == A[end - 1] - A[end - 2]:
            op = 1 + self.slices(A, end - 1)
            self.res += op
        else:
            self.slices(A, end - 1)
        return op

#DP1
class Solution2:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        cnt = 0
        add = 0
        for i in range(len(A) - 2):
            if A[i + 1] - A[i] == A[i + 2] - A[i + 1]:
                add += 1
                cnt += add
            else:
                add = 0
        return cnt

#DP2
class Solution3:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        N = len(A)
        dp = [0] * N
        for i in range(1 ,N - 1):
            if A[i - 1] + A[i + 1] == A[i] * 2:
                dp[i]  = dp[i - 1] + 1
        return sum(dp)
