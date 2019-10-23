'''
Given a string, find the length of the longest substring without repeating
characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence
             and not a substring.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                # update the res
                res = max(res, i - start)
                # here should be careful, like "abba"
                start = max(start, dic[ch] + 1)
            dic[ch] = i
        # return should consider the last
        # non-repeated substring
        return max(res, len(s) - start)


if __name__ == '__main__':
    a = Solution()
    print(a.lengthOfLongestSubstring('pwwkew'))
