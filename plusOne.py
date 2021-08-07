class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for d in digits:
            number = number*10 + d
        number+=1
        ans = []
        
        while number:
            ld = number % 10
            ans.append(ld)
            number=number//10
        ans.reverse()
        return ans
