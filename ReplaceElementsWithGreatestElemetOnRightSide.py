class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        mx = arr[l-1]
        
        for i in range(l-2,-1,-1):
            
            temp = mx
            
            if mx<arr[i]:
                mx=arr[i]
            arr[i] = temp
        
        arr[-1]=-1
        return arr
