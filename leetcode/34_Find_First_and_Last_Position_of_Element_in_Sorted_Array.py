#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#Complexity: O(logn)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result=[-1,-1]
        le=len(nums)
        if le==0:
            return result
        l=0
        h=le-1
        while l<=h:
            m=l+int((h-l)/2)
            if nums[m]==target:
                if (m-1>=0 and nums[m-1]<target) or m==0:
                    result[0]=m
                    break
                elif m-1>=0 and nums[m-1]==target:
                    h=m-1
            elif nums[m]<target:
                l=m+1
            else:
                h=m-1

        l=result[0]
        h=le-1
        while l<=h:
            m=l+int((h-l)/2)
            if nums[m]==target:
                if (m+1<le and nums[m+1]>target) or m==le-1:
                    result[1]=m
                    break
                elif m+1<le and nums[m+1]==target:
                    l=m+1
            elif nums[m]<target:
                l=m+1
            else:
                h=m-1  
        return result
        
