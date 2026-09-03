class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn=min(nums1)
        if mn%2==1:
            return True
        else:
            for i in nums1:
                if i%2!=0:
                    return False
                    break
            return True

