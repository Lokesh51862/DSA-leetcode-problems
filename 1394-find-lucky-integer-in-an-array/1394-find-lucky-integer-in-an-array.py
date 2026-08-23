class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        res=-1
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]]+=1
            else:
                d[arr[i]]=1
        for k,v in d.items():
            if k==v:
                res=max(res,k)
        return res
        
