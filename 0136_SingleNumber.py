'''
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
'''

from typing import List
from functools import reduce
import operator


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
            print(res)
        return res

    def singleNumber2(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)

    def singleNumber3(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

    def singleNumber4(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


if __name__ == '__main__':
    a = Solution()
    print(a.singleNumber([4, 1, 2, 1, 2]))
