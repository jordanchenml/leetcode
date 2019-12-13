'''
Given a positive integer n, generate a square matrix filled with elements from 1
to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A, lo = [], n * n + 1
        while lo > 1:
            lo, hi = lo - len(A), lo
            print(list(range(lo, hi)))
            A = [list(range(lo, hi))] + list(zip(*A[::-1]))
        return A


class Solution1:
    def generateMatrix(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n * n):
            A[i][j] = k + 1
            print("A[{}][{}] = {}".format(i, j, A[i][j]),
                  ", A[(i+di)%n][(j+dj)%n] = A[({}+{})%{}][({}+{})%{}] = A[{}][{}] = {}".format(
                      i,
                      di,
                      n,
                      j,
                      dj,
                      n,
                      (i + di) % n,
                      (j + dj) % n,
                      A[(i + di) % n][(j + dj) % n]))
            if A[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            print("di = {}".format(di), ", dj = {}\n".format(dj))
            i += di
            j += dj
        return A


if __name__ == '__main__':
    a = Solution1()
    print(a.generateMatrix(3))
