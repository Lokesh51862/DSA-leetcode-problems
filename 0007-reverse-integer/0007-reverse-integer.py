class Solution:
    def reverse(self, x):
        if x < 0:
            sign = -1
        else:
            sign = 1

        y = abs(x)
        rev = ""

        while y > 0:
            l = y % 10
            rev += str(l)
            y //= 10

        if rev == "":
            return 0

        ans = sign * int(rev)

        if ans < -2**31 or ans > 2**31 - 1:
            return 0

        return ans