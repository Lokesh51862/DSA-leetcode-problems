class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=set(nums)
        res=[]
        for i in range(1,len(nums)+1):
            if i not in l:
                res.append(i)
        return res
        