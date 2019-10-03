'''
Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(eval('0b' + a) + eval('0b' + b))[2:]

class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]


a = Solution1()
str1 = "1"
str2 = "11"
print(a.addBinary(str1, str2))