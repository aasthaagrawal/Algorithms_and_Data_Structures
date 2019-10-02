#https://leetcode.com/problems/search-in-rotated-sorted-array/
#Complexity: O(log n)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        pivot=self.findPivot(nums,0,n-1)
        if pivot==-1:
            return -1
        if nums[pivot]==target:
            return pivot
        elif target>=nums[pivot] and target<=nums[n-1]:
            return self.findEle(nums,pivot+1,n-1,target)
        else:
            return self.findEle(nums,0,pivot-1,target)
        
    def findPivot(self,nums,l,h):
        if l<=h:
            if l==h:
                return l
            elif l==h-1:
                return (l if nums[l]<nums[h] else h)
            else:
                m=l+int((h-l)/2)
                if nums[m]<nums[h]:
                    return self.findPivot(nums,l,m)
                else:
                    return self.findPivot(nums,m,h)
        return -1
    def findEle(self,nums,l,h,target):
        if l<=h:
            if l==h:
                if target==nums[l]:
                    return l
                else:
                    return -1
            m=l+int((h-l)/2)
            if nums[m]==target:
                return m
            elif nums[m]>target:
                return self.findEle(nums,l,m-1,target)
            else:
                return self.findEle(nums,m+1,h,target)
        return -1
