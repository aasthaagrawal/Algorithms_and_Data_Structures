#https://leetcode.com/problems/top-k-frequent-elements/

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        h=[(-v,k) for k,v in d.items()]
        heapq.heapify(h)
        i=0
        result=[]
        while i<k:
            result.append(heapq.heappop(h)[1])
            i+=1
        return result
