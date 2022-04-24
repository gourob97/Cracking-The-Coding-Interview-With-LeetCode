class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals  = sorted(intervals, key=itemgetter(0))
        
        #print(intervals)
        
        result = [intervals[0]]
        print(result)
        
        for start,end in intervals[1:]:
            lastEnd = result[-1][1]
            
            if start <= lastEnd:
                result[-1][1]= max(end, lastEnd)
            else:
                result.append([start, end])
            
        return result

