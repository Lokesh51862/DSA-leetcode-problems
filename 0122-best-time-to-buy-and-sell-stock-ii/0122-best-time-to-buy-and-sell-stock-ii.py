class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        res=0
        n=prices
        for r in range(1,len(prices)):
            if n[l]<n[r]:
                res+=n[r]-n[l]
                l+=1
            else:
                l=r
            r+=1
        return res
            

        