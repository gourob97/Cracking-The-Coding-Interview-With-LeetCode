class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        
        diff = right-left
        
        max_area = diff * min(height[left], height[right])
        
       
        
        
        while left < right-1:
            #3 tasks
               
            
        
            #1 area of left+1 and right
            #2 area of left and rigt -1
            #if none then, move  the lowest
        
        
        
            area1 = (diff-1) * min(height[left+1], height[right])
            area2 = (diff-1) * min(height[left], height[right-1])
            
            if area1>=area2 and area1 > max_area:
                max_area = area1
                left+=1
                
            elif area2>area1 and area2>max_area:
                max_area=area2
                right-=1
                
            else:
                if height[left]<height[right]:
                    left+=1
                else:
                    right-=1
                
            diff-=1
            
                
            
        return max_area        
            
            
            
        
        
        
        
        
