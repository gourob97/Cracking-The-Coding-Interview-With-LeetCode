class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        minLen = 201
        for word in strs:
            if len(word)<minLen:
                minLen = len(word)
        
        d={}
        
        for i in range(minLen):
            d[i]= strs[0][i]
            
        ans = minLen
        
        for i in range(1,len(strs)):
            for j in range(minLen):
                if strs[i][j]!=d[j]:
                    ans = min(ans,j)
                    break
                    
        if ans == 0:
            return ""
        
        return strs[0][0:ans]
    
 
