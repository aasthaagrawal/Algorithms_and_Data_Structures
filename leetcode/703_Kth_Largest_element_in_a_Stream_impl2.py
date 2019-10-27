#https://leetcode.com/problems/kth-largest-element-in-a-stream/
#Complexity:O(nlogk)

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        self.k=k
        for num in nums:
            self.add(num)
        
    def add(self, val: int) -> int:
        if len(self.heap)==self.k:
            heapq.heappushpop(self.heap,val)
        else:
            heapq.heappush(self.heap,val)
        return self.heap[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
