class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
            
        k  = len(needle)
        n = len(haystack)
        
        if n<k:
            return -1
        
        for i in range(n-k+1):
            haywindow = haystack[i:i+k]
            if haywindow == needle:
                return i
        return -1
            
     
