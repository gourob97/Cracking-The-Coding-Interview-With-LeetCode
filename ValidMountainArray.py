class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l = len(arr)
        if l<3:
            return False
        i=0
        
        
        
        while i<l-1:
            if arr[i]<arr[i+1]:
                i+=1
            else:
                break
                
        if i==l-1 or i==0:
            return False
        
        while i<l-1:
            if arr[i]<=arr[i+1]:
                return False
            else:
                i+=1
                
        
        return True
       
            
            
    
                
                
                
                    
        
        
