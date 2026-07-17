class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if sum(nums)==1 and len(nums)==2:
            return 2
        elif sum(nums)==1 and len(nums)==1:
            return 0
        elif sum(nums)==0:
            return 1
        else:
            n=len(nums)
            s=(n*(n+1))//2
            return s-sum(nums)
        