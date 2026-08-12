class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res=0
        l=0
        d={}
        for r in range(len(nums)):
            if nums[r] in d:
                d[nums[r]]+=1
            else:
                d[nums[r]]=1
            while d[nums[r]]>k:
                d[nums[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res

        