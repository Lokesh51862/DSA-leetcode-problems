class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            first=1
            sec=2
            for i in range(3,n+1):
                l=first+sec
                first,sec=sec,l
        return sec
        