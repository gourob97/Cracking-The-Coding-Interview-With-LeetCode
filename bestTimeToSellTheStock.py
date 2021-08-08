class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = prices[0]
        p = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]<a :
                a = prices[i]
                p=a
                    
            elif prices[i]>p :
                p=prices[i]
                
            cf = p-a
                
            if cf>profit:
                profit=cf
                
                
        return profit
        
        
