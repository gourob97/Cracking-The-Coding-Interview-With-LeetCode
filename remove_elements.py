class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        r=0
        for i in range(l):
            if nums[i] != val:
                nums[r]= nums[i]
                r+=1
        return r
        
        
        
