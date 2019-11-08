#https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        d=[]
        heapq.heapify(d)
        for i in points:
            heapq.heappush(d,(math.sqrt(i[0]**2+i[1]**2),i))
        k=0
        result=[]
        while k<K:
            result.append(heapq.heappop(d)[1])
            k+=1
        return result
