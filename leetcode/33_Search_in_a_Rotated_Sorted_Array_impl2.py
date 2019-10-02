#https://leetcode.com/problems/search-in-rotated-sorted-array/
#Complexity: O(log n)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        return self.binSearch(nums,0,n-1,target)
        
    def binSearch(self,nums,l,h,target):
        if l>h:
            return -1
        if l==h:
            if nums[l]==target:
                return l
            else:
                return -1
        m=l+int((h-l)/2)
        if target==nums[m]:
            return m
        if nums[m]<=nums[h]:
            if target>nums[m] and target<=nums[h]:
                return self.binSearch(nums,m+1,h,target)
            else:
                return self.binSearch(nums,l,m-1,target)
        else:
            if target>=nums[l] and target<nums[m]:
                return self.binSearch(nums,l,m-1,target)
            else:
                return self.binSearch(nums,m+1,h,target)
