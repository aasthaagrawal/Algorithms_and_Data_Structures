#https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-i for i in nums]
        heapq.heapify(nums)
        i=1
        while i<k:
            heapq.heappop(nums)
            i+=1
        ele=heapq.heappop(nums)
        return -ele
