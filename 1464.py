class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1st = 0
        max2nd = 0
        
        for num in nums:
            if num>max1st:
                max2nd = max1st
                max1st = num
            elif num>max2nd:
                max2nd =num
                
        return (max1st-1)*(max2nd-1)
