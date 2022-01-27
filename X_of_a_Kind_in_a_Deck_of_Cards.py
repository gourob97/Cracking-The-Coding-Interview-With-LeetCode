class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        
        d = dict()
        
        for card in deck:
            if card in d.keys():
                d[card]+=1
            else:
                d[card]=1
         
        
        for i in range(2,10000):
            flag = 0
            for key in d.keys():
                if d[key]%i!= 0:
                    flag = 1
            if flag == 0:
                return True
        
        return False
        
        
        
        
