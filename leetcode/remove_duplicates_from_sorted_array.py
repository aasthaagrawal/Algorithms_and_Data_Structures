#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#Complexity O(n)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length=len(nums)
        if length > 1:
            index=1
            pointer=1
            while pointer<length:
                if nums[index-1]==nums[pointer]:
                    pointer +=1
                else:
                    nums[index]=nums[pointer]
                    index +=1
                    pointer +=1
            return index
        else:
            return length
