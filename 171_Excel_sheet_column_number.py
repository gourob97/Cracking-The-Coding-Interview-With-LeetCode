class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        sum = 0
        
        for i in range(len(columnTitle)):
            digit = ord(columnTitle[i])-64
            base = 26
            position = len(columnTitle)-1-i
            
            sum+=digit*pow(base, position)
            
        return sum
            
        
        
