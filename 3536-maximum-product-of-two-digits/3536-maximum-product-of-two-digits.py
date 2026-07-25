class Solution:
    def maxProduct(self, n: int) -> int:
        m1=-1 
        m2=-1
        while n!=0:
            rem=n%10
            if m1<=rem:
                m2=m1
                m1=rem
            elif m2<rem:
                m2=rem
            n//=10
        return m1*m2


            
        