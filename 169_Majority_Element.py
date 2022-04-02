class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq = {}
        
        for num in nums:
            if num in freq.keys():
                freq[num]+=1
            else:
                freq[num]=1
        
        
        max = 0
        ans = -1
        
        for num in freq.keys():
            if freq[num]>max:
                max = freq[num]
                ans = num
        return ans
