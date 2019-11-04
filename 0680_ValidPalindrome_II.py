'''
Given a non-empty string s, you may delete at most one character. Judge whether
you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the
string is 50000.
'''


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True
        else:
            for i in range(len(s)):
                a = s[:i] + s[i + 1:]
                print(a)
                if self.isPalindrome(a):
                    return True
            return False

    def isPalindrome(self, s: str) -> bool:
        if str(s) == str(s)[::-1]:
            return True
        else:
            return False


class Solution1:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True


if __name__ == '__main__':
    s = Solution1()
    print(s.validPalindrome(
        "pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip"))
