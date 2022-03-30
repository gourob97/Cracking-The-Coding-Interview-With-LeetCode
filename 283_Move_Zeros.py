class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            if nums[i] == 0:
                j= i+1
                flag =0
                while j<len(nums):
                    if nums[j]!=0:
                        nums[i],nums[j]=nums[j],nums[i]
                        flag=1
                        break
                    j+=1
                if flag==0:
                    return
