class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[0]
        right=[0]
        
        l = len(nums)
        
        for i in range(1,l):
            if i==1:
                left.append(nums[0])
                
            else:
                left.append(left[i-1]*nums[i-1])
        #print(left)
        
        for i in range(l-2,-1,-1):
            if i==l-2:
                right.insert(0,nums[l-1])
            else:
                right.insert(0,nums[i+1]*right[0])
                
        #print(right)       
        res =[right[0]]
        for i in range(1,l-1):
            res.append(right[i]*left[i])
        res.append(left[l-1])
            
        return res
                
        
