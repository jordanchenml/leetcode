'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                return True
            else:
                map[nums[i]] = 1
        return False

class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


if __name__ == '__main__':
    a = Solution()
    print(a.containsDuplicate([1,5,-2,-4,0]))