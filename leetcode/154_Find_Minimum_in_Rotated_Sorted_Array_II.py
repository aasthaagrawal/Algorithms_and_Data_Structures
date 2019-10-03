#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
#Complexity: Worst case is O(n), otherwise O(log n)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return -1
        return nums[self.findMinAux(nums,0,n-1)]
        
    def findMinAux(self,nums,l,h):
        if l==h:
            return l
        if l==h-1:
            return (l if nums[l]<=nums[h] else h)
        m=l+int((h-l)/2)
        if nums[m]<nums[h]:
            return self.findMinAux(nums,l,m)
        elif nums[m]>nums[h]:
            return self.findMinAux(nums,m+1,h)
        if nums[m]==nums[h]:
            if nums[m]==nums[l]:
                return self.findMinAux(nums,l+1,h)
            else:
                return self.findMinAux(nums,l,h-1)
             
