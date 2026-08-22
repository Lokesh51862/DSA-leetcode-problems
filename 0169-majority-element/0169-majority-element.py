class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        n=len(nums)//2
        for k,v in d.items():
            if v>n:
                return k
                break
        
        
        