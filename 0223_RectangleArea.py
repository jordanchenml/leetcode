'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as
shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.
'''


from typing import List

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int,
                    G: int, H: int) -> int:
        overlap = max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0)
        area1 = (A-C)*(B-D)
        area2 = (E-G)*(F-H)
        return area1 + area2 - overlap


class Solution1:
    def rectangleOverlapArea(self, rec1: List[int], rec2: List[int]):
        l1 = rec1[2] - rec1[0]
        l2 = rec2[2] - rec2[0]
        h1 = rec1[3] - rec1[1]
        h2 = rec2[3] - rec2[1]
        lengh = max(abs(rec2[2] - rec1[0]), abs(rec1[2] - rec2[0]))
        height = max(abs(rec2[3] - rec1[1]), abs(rec1[3] - rec2[1]))
        print(l1)
        print(h1)
        print(l2)
        print(h2)
        print(lengh)
        print(height )
        return lengh * height

if __name__ == '__main__':
    a = Solution()
    print(a.computeArea([-3,0,3,4], [0,-1,9,2]))