class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for index,num in enumerate(nums):
            if target-num in d.keys():
                return list((index,d[target-num]))
            else:
                d[num] = index
                
        
