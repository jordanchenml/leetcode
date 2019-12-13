'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

from typing import List
import itertools
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ''' "eat", "tea", "tan", "ate", "nat", "bat" '''
        # sorted(strs, key=sorted) -> 依照組成單字的三個字母排序
        print(sorted(strs, key=sorted))
        # ['bat', 'eat', 'tea', 'ate', 'tan', 'nat']

        for key, g in itertools.groupby(sorted(strs, key=sorted), sorted):
            # for a in itertools.groupby(sorted(strs, key=sorted), sorted):
            #     print(a)
            print(key)
            # print(sorted(g))
            print(list(g))
            # ['a', 'b', 't']
            # ['bat']
            # ['a', 'e', 't']
            # ['ate', 'eat', 'tea']
            # ['a', 'n', 't']
            # ['nat', 'tan']

        return [list(g) for _, g in
                itertools.groupby(sorted(strs, key=sorted), sorted)]


def test():
    from itertools import groupby

    things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"),
              ("vehicle", "speed boat"), ("vehicle", "school bus")]

    for key, group in groupby(things, sorted):
        for thing in group:
            print("A %s is a %s." % (thing[1], key))
        print(" ")


if __name__ == '__main__':
    a = Solution()
    print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # test()
