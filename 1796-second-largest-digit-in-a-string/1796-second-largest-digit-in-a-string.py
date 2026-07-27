class Solution:
    def secondHighest(self, s: str) -> int:
        m1,m2=-1,-1
        for i in s:
            if i.isdigit():
                if int(i)>m1:
                    m2=m1
                    m1=int(i)
                elif m1>int(i)>m2:
                    m2=int(i)
        return m2
        