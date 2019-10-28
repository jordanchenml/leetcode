'''
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

The thought follows a simple rule:
If the sum of a subarray is positive, it has possible to make the next value
bigger, so we keep do it until it turn to negative.
If the sum is negative, it has no use to the next element, so we break.
it is a game of sum, not the elements.
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


# Dynamic Programming
class Solution2:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        l = len(nums)
        if l == 0: return 0
        res = now = nums[0]
        for i in range(1, l):
            if now > 0:
                now += nums[i]
            else:
                now = nums[i]

            if now > res:
                res = now
        return res

a = Solution1()
print(a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
