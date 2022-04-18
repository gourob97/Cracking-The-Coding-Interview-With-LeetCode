class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        
        max = 0
        
        for num in nums:
            #determining if num is starting of a sequence
            if num-1 not in myset:
                #staring of a secuence
                #so check how long it goes
                
                start = num
                next = num+1
                l = 1
                
                while next in myset:
                    l+=1
                    next+=1
                
                if l>max:
                    max = l
        return max

