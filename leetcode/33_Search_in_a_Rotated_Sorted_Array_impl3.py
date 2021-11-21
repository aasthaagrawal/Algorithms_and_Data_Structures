#https://leetcode.com/problems/search-in-rotated-sorted-array/
#Time Complexity: O(n)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        return self.bs(0,len(nums)-1)

    def bs(self, left, right):
        if left<=right:
            mid = left + (right-left)//2
            if self.nums[mid] == self.target:
                return mid
            elif self.nums[mid] >= self.nums[left]:
                if self.nums[left] <= self.target and self.target < self.nums[mid]:
                    return self.bs(left, mid-1)
                return self.bs(mid+1, right)
            else:
                if self.nums[mid] < self.target and self.target <= self.nums[right]:
                    return self.bs(mid+1, right)
                return self.bs(left, mid-1)
        return -1
