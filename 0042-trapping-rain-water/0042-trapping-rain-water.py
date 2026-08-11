class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=[0]*len(height),[0]*len(height)
        res=0
        l[0]=height[0]
        r[-1]=height[-1]
        for i in range(1,len(height)):
            l[i]=max(height[i],l[i-1])
        for i in range(len(height)-2,-1,-1):
            r[i]=max(height[i],r[i+1])
        for i in range(len(height)):
            res+=min(l[i],r[i])-height[i]
        return res



        