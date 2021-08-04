class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        i=0
        while i<l-1:
            j=i+1
            if nums[i] == nums[j] :
                nums.pop(j)
                l-=1
            else:
                i+=1
        return len(nums)
                
            
        
