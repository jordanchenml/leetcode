from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest


class Solution1:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1


a = Solution1()
strs = ["flower", "flow", "flight"]
print(a.longestCommonPrefix(strs))
