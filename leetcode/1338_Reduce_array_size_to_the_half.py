#https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    from collections import defaultdict, Counter
    import heapq
    def minSetSize(self, arr: List[int]) -> int:
        to_del = (len(arr)+1)//2
        result = 0
        heap = []

        count = Counter(arr)
        for val in count.values():
            heap.append(-val)
        heapq.heapify(heap)
        del count

        while to_del>0:
            freq = heapq.heappop(heap)
            result += 1
            to_del += freq
        return result
