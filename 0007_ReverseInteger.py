class Solution:
    def reverse(self, x: int) -> int:
        s = [1, -1][x < 0]
        # a = 1 if x > 0 else -1
        ret = s * int(str(abs(x))[::-1])
        return ret if -(2**31)-1 < ret < 2**31 else 0