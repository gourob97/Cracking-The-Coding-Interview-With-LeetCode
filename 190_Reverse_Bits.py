class Solution:
    def reverseBits(self, n: int) -> int:
        
        b =[]
        
        while n>1:
            if n%2:
                rem = 1
            else:
                rem = 0
                
            b.append(rem)
            n=n//2
        
        if n==1:
            b.append(1)
        
        while len(b)!=32:
            b.append(0)
        
        
        
        sum = 0
        
        for i in range(len(b)):
            
            if b[i]==1:
                
                sum+=pow( 2,len(b)-1-i)
        
        return sum   
        
