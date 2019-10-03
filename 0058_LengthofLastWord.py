'''
Input: "Hello World"
Output: 5
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip(' ').split(' ')[-1])
a = Solution()
print(a.lengthOfLastWord('a '))

txt = "     banana     "

x = txt.rstrip()
y = txt.strip()
z = txt.lstrip()

print("of all fruits", x, "is my favorite")
print("of all fruits", y, "is my favorite")
print("of all fruits", z, "is my favorite")
