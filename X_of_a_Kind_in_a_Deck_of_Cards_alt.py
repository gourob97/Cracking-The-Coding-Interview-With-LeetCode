class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        def gcd(a,b) :
            if b==0:
                return a
            return gcd(b,a%b)
        
        d = dict()
        
        for card in deck:
            if card in d.keys():
                d[card]+=1
            else:
                d[card]=1
        
        ans = 0 # because gcd(0,n)=n
        
        for key in d.keys():
            ans = gcd(ans,d[key])
        if ans<2:
            return False
        return True
            
        
        
        
        
        
        
