class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        
        for num in nums:
            if num in d.keys():
                return num
            else:
                d[num] = True
        
