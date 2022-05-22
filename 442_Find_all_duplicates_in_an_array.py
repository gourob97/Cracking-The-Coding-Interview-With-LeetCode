class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result =[]
        
        for i in range(len(nums)):
            
            #check if already visited
            check =abs(nums[i])-1
            
            if nums[check]<0:
                result.append(abs(nums[i]))
            #if not already visited
            else:
                nums[check] *= -1
                
        return result
        
        
        
