class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for c in s:
            if c in dict.values():
                stack.append(c)
                print(stack[0])
            elif c in dict.keys():
                if stack == [] or dict[c] != stack.pop():
                    return False
            else:
                return False
        return stack == []


class Solution1:
    def isValid(self, s: str) -> bool:
        lefty = '({['
        righty = ')}]'
        stack = []
        for c in s:
            if c in lefty:
                stack.append(c)
            elif c in righty:
                if len(stack) == 0:
                    return False
                if righty.index(c) != lefty.index(stack.pop()):
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    a = Solution()
    print(a.isValid('()'))
