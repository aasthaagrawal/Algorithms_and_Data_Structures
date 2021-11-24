#https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
#O(nlog n)

class Solution:
    import heapq
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events)
        n = len(events)
        heap = []
        heapq.heapify(heap)
        i, result, cur_day  = 0, 0, events[0][0]
        while i < n:
            while i<n and cur_day == events[i][0]:
                heapq.heappush(heap, events[i][1])
                i += 1

            result += 1
            cur_day += 1
            heapq.heappop(heap)
            while heap and heap[0]<cur_day:
                heapq.heappop(heap)
            if not heap and i<n:
                cur_day = events[i][0]
        while heap:
            if heapq.heappop(heap) >= cur_day:
                cur_day += 1
                result += 1
        return result
