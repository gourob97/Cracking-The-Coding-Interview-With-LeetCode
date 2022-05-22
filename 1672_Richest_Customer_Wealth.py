class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        maxWealth = -100
        
        for cust in accounts:
            maxWealth = max(maxWealth, sum(cust))
        return maxWealth
