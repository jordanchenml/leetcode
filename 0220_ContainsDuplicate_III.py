'''
Given an array of integers, find out whether there are two distinct indices i
and j in the array such that the absolute difference between nums[i] and nums[j]
is at most t and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
'''

from typing import List
import collections


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int,
                                      t: int) -> bool:
        if k < 0 or t < 0:
            return False
        window = collections.OrderedDict()
        for n in nums:
            # Make sure window size
            # Pop out the first element
            if len(window) > k:
                window.popitem(False)

            bucket = n if not t else n // t
            for m in (window.get(bucket - 1), window.get(bucket), window.get(bucket + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            window[bucket] = n
        return False


if __name__ == '__main__':
    a = Solution()
    print(a.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))