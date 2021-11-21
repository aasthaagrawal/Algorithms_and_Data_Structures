#https://leetcode.com/problems/find-pivot-index/
#Time complexity: O(n)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        d = [0]*(n+1)
        for i in range(n):
            d[i+1] = d[i] + nums[i]
        for i in range(n):
            if d[i] == d[-1]-d[i+1]:
                return i
        return -1
