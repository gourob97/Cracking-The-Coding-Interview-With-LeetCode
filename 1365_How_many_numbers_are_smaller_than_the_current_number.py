class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        
        result = []
        
        for i in range(len(nums)):
            
            result.append(0)
            
            currnum = nums[i]
            
            
            for j in range(len(nums)):
                if i!=j:
                    if nums[j]<currnum:
                        result[i]+=1
                        
            
        return result

