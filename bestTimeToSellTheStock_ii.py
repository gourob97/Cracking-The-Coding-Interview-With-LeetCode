class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        l = len(prices)
        buy = False
        sell = False
        bp = 0
        sp = 0
        profit = 0
        while j<l:
            if( prices[i] < prices[j] ):
                if not buy:
                    buy = True
                    sell = False
                    bp = prices[i]
                    
            elif prices[i] > prices[j]:
                if buy:
                    sell = True
                    buy = False
                    sp = prices[i]
            if sell:
                profit+=sp-bp
                sell=False
            i+=1
            j+=1
        
        if not sell and buy:
            profit +=  prices[l-1] - bp
        
        return profit
                
                    
            
        
