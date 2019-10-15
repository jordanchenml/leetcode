'''
Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of
zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ls = len(nums)
        res = []
        nums.sort()
        for i in range(ls - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, ls - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if tmp == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    k -= 1
                    j += 1
                elif tmp > 0:
                    k -= 1
                else:
                    j += 1
        return res


a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
