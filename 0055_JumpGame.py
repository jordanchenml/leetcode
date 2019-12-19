'''
Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last
             index.
'''

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal

    def canJump1(self, nums: List[int]) -> bool:
        """
        这个题的tag是贪心，贪心策略是我们每次都选取最优的策略，然后前面已经选好了的就不用管了。
        这个题的贪心方法是，我们使用一个变量reach保存当前能到达的最后位置索引，
        那么在每个位置的时候判断这个位置能不能到达，
        即位置的索引大于了reach说明前面无论怎么走也走不到这个位置，
        就返回False好了。如果这个位置可以到达，那么要维护一下这个reach，
        更新策略是当前位置索引+这个数字代表的能向右走多少步，
        这个代表了到达当前位置的时候向右能到达的最远距离，在这个最远距离以内的任何位置都能到，
        因为每次跳的步数可以变小的。那么进行了这么一次循环以后，每个位置都判断为能到达，
        所以结果返回True就好了。
        """
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True



if __name__ == '__main__':
    a = Solution()
    print(a.canJump1([2,3,1,1,4]))