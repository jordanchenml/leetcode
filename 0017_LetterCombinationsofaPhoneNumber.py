'''
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in
any order you want.
'''

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        index = 0
        path = ''
        kvmaps = {'2': 'abc',
                  '3': 'def',
                  '4': 'ghi',
                  '5': 'jkl',
                  '6': 'mno',
                  '7': 'pqrs',
                  '8': 'tuv',
                  '9': 'wxyz'}
        self.dfs(digits, index, res, path, kvmaps)
        return res

    def dfs(self, digits, index, res, path, kvmaps):
        if index == len(digits):
            if path != '':
                res.append(path)
            return
        for j in kvmaps[digits[index]]:
            self.dfs(digits, index + 1, res, path + j, kvmaps)


