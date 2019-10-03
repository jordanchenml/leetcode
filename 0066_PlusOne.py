'''
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    #     return [i for i in str(int(''.join([str(i) for i in digits])) + 1)]
        if len(digits) == 0:
            digits = [1]
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            digits.extend([0])
        else:
            digits[-1] += 1
        return digits

class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [i for i in str(int(''.join([str(i) for i in digits])) + 1)]


a = Solution()
print(a.plusOne([1, 2, 4, 5 ,9]))
