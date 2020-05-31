'''
Given an array of size n, find the majority element. The majority element is the
element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist
in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        for key in d:
            if d[key] > (len(nums) / 2):
                return key

    def majorityElement1(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            if d[num] > len(nums) / 2:
                return num
            else:
                d[num] += 1

    # def majorityElement2(self, nums: List[int]) -> int:


if __name__ == '__main__':
    a = Solution()
    print(a.majorityElement2([2,2,1,1,1,2,2]))
