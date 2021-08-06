class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prevSum = nums[0]
        currSum = 0
        l = len(nums)
        
        for n in nums:
            
            if currSum<0:
                currSum =0
                
            currSum += n
            
            if currSum > prevSum:
                prevSum = currSum
                
        return prevSum
    
