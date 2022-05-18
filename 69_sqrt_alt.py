class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x<2:
            return x
        
        left = 1
        
        right = x
        
        while left<right:
            
            mid = (left + right)//2
            
            
            if mid*mid > x:
                right = mid
            elif mid*mid < x:
                left =mid+1 
            else:
                return mid
            
        return left-1
        
            
            
            
                
