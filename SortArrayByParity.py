class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        s=0
        e=len(nums)-1
        
        while(s<e):
            if nums[e]%2==0:  #if even  then swap
                while(nums[s]%2==0 and s<e):
                    s+=1
                    
                temp=nums[e]
                nums[e]=nums[s]
                nums[s]=temp
            e-=1
        
        
        return nums
        
