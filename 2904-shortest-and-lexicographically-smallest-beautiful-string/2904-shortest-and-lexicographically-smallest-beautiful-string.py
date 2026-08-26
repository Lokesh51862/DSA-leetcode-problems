class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l=0
        one=0
        res=""
        for r in range(len(s)):
            if s[r]=='1':
                one+=1
            if one==k:
                while s[l]=="0":
                    l+=1
                sub=s[l:r+1]
                if res=="":
                    res=sub
                elif len(res)>len(sub):
                    res=sub
                elif len(res)==len(sub) and sub<res:
                    res=sub
                one-=1
                l+=1
        return res

        