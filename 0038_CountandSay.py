'''
1

11

21

1211

111221

312211

13112221

'''

class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            # original
            # s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))

            # decomposed
            v = ''  # accumulator string
            # iterate the characters (digits) grouped by digit
            for digit, group in itertools.groupby(result):
                count = len(list(group))  # eg. the 2 in two 1s
                v += "%i%s" % (count, digit)  # create the 21 string and accumulate it
            result = v  # save to result for the next for loop pass

        # return the accumulated string
        return result

class Solution1:
    def countAndSay(self, n):
        s = '1'
        for _ in range(n-1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count)+let
                    let = l
                    count = 1
            temp += str(count)+let
            s = temp
        return s

a = Solution1()
print(a.countAndSay(5))


