class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fp = 0
        lp = len(numbers)-1
        
        while fp<lp:
            sum = numbers[fp]+numbers[lp]
            if sum == target:
                return list([fp+1,lp+1])
            
            if sum>target:
                lp-=1
            else:
                fp+=1
      
