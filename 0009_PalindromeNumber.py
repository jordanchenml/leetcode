'''
Determine whether an integer is a palindrome. An integer is a palindrome when it
reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes
121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Could you solve it without converting the integer to a string?
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

class Solution1:
    def isPalindrome(self, x: int) -> bool:
        p = x
        a = 0
        while p > 9:
            a += p % 10
            a *= 10
            p //= 10
        a += p
        if a == x and x >= 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution1()
    print(s.isPalindrome(-121))