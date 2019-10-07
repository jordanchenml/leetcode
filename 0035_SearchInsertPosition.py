from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([x for x in nums if x < target])


class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
