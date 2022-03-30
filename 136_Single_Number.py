class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        d = {}
        
        for num in nums:
            if num in d.keys():
                d[num]+=1
            else:
                d[num]=1
        
        for item in d.keys():
            if d[item] == 1:
                return item
