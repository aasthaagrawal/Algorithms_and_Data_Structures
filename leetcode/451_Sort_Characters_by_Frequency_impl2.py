#https://leetcode.com/problems/sort-characters-by-frequency/

import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]-=1
            else:
                d[i]=-1
        h=[(value,key) for key,value in d.items()]
        heapq.heapify(h)
        result=[]
        while len(h):
            c,ele=heapq.heappop(h)
            result=result+[ele for i in range(-c)]
        return ''.join(result)
