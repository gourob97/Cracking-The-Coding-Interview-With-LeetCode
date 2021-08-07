class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num  = int(''.join([str(digit) for digit in digits ]))+1
        mylist = [int(d) for d in list(str(num))]
        return mylist
        
