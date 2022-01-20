class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        req = target - numbers[0]
        index=0
        d=dict()
        d[req]=index
        index+=1
        num = numbers[index]
        l= len(numbers)
        
        while index<l:
            if num in d.keys():
                res=[]
                res.append(d[num]+1)
                res.append(index+1)
                return res
            else:
                req = target - num
                d[req]=index
                index+=1
                num=numbers[index]
