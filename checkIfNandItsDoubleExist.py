class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        myset = set()
        for item in arr:
            if item in myset:
                return True
            else:
                myset.add(item*2)
                if item%2 == 0:
                    myset.add(item//2)
        
        return False
