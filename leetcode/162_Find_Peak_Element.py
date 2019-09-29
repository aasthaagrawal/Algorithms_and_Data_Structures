#https://leetcode.com/problems/find-peak-element/
#Complexity: O(log n)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        m=l+int((h-l)/2)
        return self.findPeakEleUtil(nums,l,m,h)
    
    def findPeakEleUtil(self,nums,l,m,h):
        if (m==0 or nums[m]>nums[m-1]) and (m==len(nums)-1 or nums[m]>nums[m+1]):
            return m
        if m>0 and nums[m-1]>nums[m]:
            return self.findPeakEleUtil(nums,l,(l+int((m-1-l)/2)),m-1)
        else:
            return self.findPeakEleUtil(nums,m+1,(m+1+int((h-m-1)/2)),h)
