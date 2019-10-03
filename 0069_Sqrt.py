'''
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# Since the return type is an integer, the decimal digits are truncated and
only the integer part of the result is returned.

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
'''

import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))

class Solution1:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        for i in range(x+1):
            if i * i > x:
                return i - 1
class Solution2:
    def mySqrt(self, x: int) -> int:
        r = x
        while r * r > x:
            r = int(r - (r*r - x)/(2*r))
        return r

class Solution3:
    def mySqrt(self, x: int) -> int:
        l = 0
        h = x
        while l <= h:
            mid = (l + h) / 2
            if mid ** 2 <= x:
                l = mid + 1
            else:
                h = mid - 1
        return int(l - 1)


a = Solution3()
print(a.mySqrt(90))