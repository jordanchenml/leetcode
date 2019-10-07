'''
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid
palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_s = [t.lower() for t in s if t.isalnum()]
        if len(valid_s) <= 1:
            return True
        mid = len(valid_s)
        for i in range(mid):
            if valid_s[i] != valid_s[len(valid_s) - 1 - i]:
                return False
        return True


class Solution1:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1;
            r -= 1
        return True
