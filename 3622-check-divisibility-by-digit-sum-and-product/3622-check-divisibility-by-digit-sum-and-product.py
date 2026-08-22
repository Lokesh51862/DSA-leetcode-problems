class Solution:
    def checkDivisibility(self, n: int) -> bool:
        pro=1
        s=0
        temp=n
        while temp>0:
            rem=temp%10
            pro*=rem
            s+=rem
            temp//=10
        return n%(pro+s)==0
        