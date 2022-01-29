class Solution:
    
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        def fact(n):
            res=1
            for i in range(2,n+1):
                res*=i
            return res
    
    
        l = len(rectangles)
        d = dict()
        
        for i in range(l):
            ratio = rectangles[i][0]/rectangles[i][1]
            if ratio in d.keys():
                d[ratio]+=1
            else:
                d[ratio] = 1
        print(d)
        count=0
        for key in d.keys():
            if d[key]>1:
                count+=fact(d[key])//(2* fact(d[key]-2))
        return count
        
