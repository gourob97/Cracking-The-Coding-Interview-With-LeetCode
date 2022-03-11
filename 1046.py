import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i]*=-1
            
        heapq.heapify(stones)
        
        
        
        while len(stones)>1:
            y = heapq.heappop(stones)
            y*=-1
            x = heapq.heappop(stones)
            x*=-1
            
            if x==y:
                continue
            else:
                new = y-x
                
                heapq.heappush(stones, -new)
                
        try:
            return -stones[0]
        except:
            return 0
            
        
        
