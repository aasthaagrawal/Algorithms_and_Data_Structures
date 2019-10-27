#https://leetcode.com/problems/kth-largest-element-in-a-stream/
#Timelimit exceeds

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        heapq.heapify(self.nums)
        self.k=k
        
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        l=[]
        i=len(self.nums)-self.k
        while(i>=0):
            l.append(heapq.heappop(self.nums))
            i-=1
        for i in l:
            heapq.heappush(self.nums,i)
        return l[-1]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
