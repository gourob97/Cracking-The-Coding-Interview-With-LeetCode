class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        
        for char in s:
            if char in d.keys():
                d[char]+=1
            else:
                d[char] = 1
                
        for char in t:
            if char in d.keys():
                d[char]-=1
            else:
                return False
        
        for val in d.values():
            if val!=0:
                return False
        return True
                   
                
        
                
        
        
        
