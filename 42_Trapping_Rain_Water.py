class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft=[]
        maxRight=[]
        
        mx = 0
        for i in range(len(height)):
            maxLeft.append(mx)
            
            if height[i]>mx:
                mx = height[i]
            
                
        
                
        mx = 0
        for i in range(len(height)-1, -1, -1):
            
            maxRight.insert(0,mx)
            
            if height[i]>mx:
                mx = height[i]
                
                
        water = 0
        
        for i in range(len(height)):
            water+= max(0 , min(maxLeft[i],maxRight[i])-height[i])
        
        return water
