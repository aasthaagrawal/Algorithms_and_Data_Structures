#https://leetcode.com/problems/search-insert-position/
#Complexity O(n)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length=len(nums)
        first=0
        last=length-1
        while(first<=last):
            x=round((last-first)/2)
            if x==0:
                if nums[first]==target:  return first
                if nums[last]==target: return last
                if nums[first]>target and first==0: return first
                if nums[last]<target: return last+1
                if nums[first]<target and nums[last]>target: return last
            
            index=first+x
            if target==nums[index]:
                return index
            elif target<nums[index]:
                last=index
            else:
                first=index
