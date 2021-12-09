#https://leetcode.com/problems/maximum-average-pass-ratio/
#Time Complexity: O(nlogn + k) where n is the length of classes and k = extrastudents

class Solution:
    import heapq
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [ (-(t-p)/(t*(t+1)), p, t) for p,t in classes]
        heapq.heapify(heap)
        while extraStudents>0:
            b, p, t = heapq.heappop(heap)
            p,t = p+1, t+1
            extraStudents -= 1
            heapq.heappush(heap, ((p-t)/(t*(t+1)), p, t))
        res = sum(p/t for b, p, t in heap)
        return res/len(classes)
