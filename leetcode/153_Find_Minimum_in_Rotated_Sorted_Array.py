#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#Complexity: O(log n)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        return nums[self.findMinAux(nums,0,n-1)]
    
    def findMinAux(self,nums,l,h):
        if l==h:
            return l
        if h-1==l:
            return (l if nums[l]<nums[h] else h)
        m=l+int((h-l)/2)
        if nums[m]>=nums[h]:
            return self.findMinAux(nums,m+1,h)
        else:
            return self.findMinAux(nums,l,m)
