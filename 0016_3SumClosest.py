'''
Given an array nums of n integers and an integer target, find three integers in
nums such that the sum is closest to target. Return the sum of the three
integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ls = len(nums)
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(ls - 2):
            j, k = i + 1, ls - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if abs(target - tmp) < abs(target - res):
                    res = tmp
                if tmp < target:
                    j += 1
                else:
                    k -= 1
        return res


a = Solution()
print(a.threeSumClosest([-1, 2, 1, -4], 1))
