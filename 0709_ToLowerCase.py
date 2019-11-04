'''
Implement function ToLowerCase() that has a string parameter str, and returns
the same string in lowercase.

Example 1:
Input: "Hello"
Output: "hello"

Example 2:
Input: "here"
Output: "here"

Example 3:
Input: "LOVELY"
Output: "lovely"
'''


class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ""
        for i in str:
            if ord(i) < ord('a') and ord(i) >= ord('A'):
                i = chr(ord(i) + 32)
            res += i
        return res


class Solution1:
    def toLowerCase(self, str: str) -> str:
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)


if __name__ == '__main__':
    s = Solution()
    print(s.toLowerCase("HELLO"))
