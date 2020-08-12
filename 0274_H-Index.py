'''
Given an array of citations (each citation is a non-negative integer) of a
researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h
if h of his/her N papers have at least h citations each, and the other N − h
papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
             of them had received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each
             and the remaining two with no more than 3 citations each, her
             h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as
the h-index.
'''

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        h = 0
        for i, c in enumerate(citations):
            h = max(h, min(n - i, c))
        return h


class Solution2:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        l, r = 0, n - 1
        h = 0
        while l <= r:
            mid = l + (r - l) // 2
            h = max(h, min(n - mid, citations[mid]))
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid - 1
        return h

