class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            sumq=0
            while n>0:
                digit=n%10
                sumq+=digit*digit
                n//=10
            n=sumq
        return n==1



        