#https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        from collections import Counter
        
        d = Counter(tasks).most_common()
        l = [(-val, key) for key,val in d]
        heapq.heapify(l)
        res = 0
        while l:
            numKeys = 0
            extracted = []
            while len(l)>0 and numKeys<=n:
                extracted.append(heapq.heappop(l))
                res += 1
                numKeys += 1
            for e in extracted:
                if e[0]+1<0:
                    tup = (e[0]+1, e[1])
                    heapq.heappush(l,tup)
            while l and numKeys<=n:
                res += 1
                numKeys+=1
        return res
