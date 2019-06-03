#https://leetcode.com/problems/contains-duplicate/
#Complexity: O(len(nums))

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict={}
        length=len(nums)
        for i in range(length):
            if nums[i] in dict:
                return True
            dict[nums[i]]=1
        return False
