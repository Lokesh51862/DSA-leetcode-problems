class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        Min=nums.index(min(nums))
        Max=nums.index(max(nums))
        l=min(Min,Max)
        r=max(Min,Max)
        rtol=r+1
        ltor=n-l
        op=(l+1)+(n-r)

        return min(rtol,ltor,op)
        