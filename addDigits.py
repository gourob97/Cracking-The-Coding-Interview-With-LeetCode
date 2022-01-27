class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        
        sum = 0
        while num!=0:
            ld = num%10
            sum+=ld
            num = num//10
            
        return self.addDigits(sum)
            
            
        
