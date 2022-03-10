import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = []

        rows = len(mat)
        cols = len(mat[0])

        for i in range(rows):
            count = 0
            for j in range(cols):
                if mat[i][j] == 1:
                    count+=1
                else:
                    break

            soldiers.append((count,i))

        heapq.heapify(soldiers)
        res =[]
        while k:
            res.append( heapq.heappop(soldiers)[1]  )
            k-=1

        return res


