class Solution:
    
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        start = 0
        end = l-1
        while start<end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start+=1
            end-=1
        
        
        
