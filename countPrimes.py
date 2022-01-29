import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        
        checklist =[True]*n
        
        i=2
        while i**2<=n :
            if checklist[i]:
                for j in range(i+i,n,i):
                    checklist[j]= False
            i+=1
        
        return sum(checklist[2:])
        
    
