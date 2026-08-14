class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        d=set()
        l=0
        for r in range(len(s)):
            while s[r] in d:
                d.remove(s[l])
                l+=1
            else:
                d.add(s[r])
            res=max(r-l+1,res)
        return res
        