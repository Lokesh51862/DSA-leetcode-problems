class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=s.lower()
        l=0
        r=len(st)-1
        while l<r:    
            while l<r and not st[l].isalnum():
                l+=1
            while l<r and not st[r].isalnum():
                r-=1
            if st[l]!=st[r]:
                return False
            l+=1
            r-=1
        return True
        