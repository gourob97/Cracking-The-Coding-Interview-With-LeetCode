class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swapPos1 = None
        
        #from last last to 2nd index
        for i in range(len(nums)-1,0,-1):
            #if there is redcution in reverse order
            if nums[i-1]<nums[i]:
                swapPos1 = i-1
                break
        
        #immediate greater number than the number in swapPos1
        
        if swapPos1 is not None:
            for i in range(len(nums)-1,swapPos1,-1):
                if nums[i]>nums[swapPos1]:
                    swapPos2 = i
                    break
        
            nums[swapPos1],nums[swapPos2] = nums[swapPos2],nums[swapPos1]
        
            left = swapPos1+1            
        else:
            left = 0
        right = len(nums)-1
        
        while left<right:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1
            right-=1
            

