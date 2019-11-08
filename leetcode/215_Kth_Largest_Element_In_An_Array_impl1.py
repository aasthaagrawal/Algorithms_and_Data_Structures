#https://leetcode.com/problems/kth-largest-element-in-an-array/
#Complexity: O(nlogn) where n is the length of array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        return nums[-k]
