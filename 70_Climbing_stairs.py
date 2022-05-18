class Solution:
    def climbStairs(self, n: int) -> int:
        
        solution={}
        
        solution[1]=1
        solution[2]=2
        
        for i in range(3,46):
            solution[i]=solution[i-1]+solution[i-2]
        
        
        return solution[n]
        
        
        
        
        
