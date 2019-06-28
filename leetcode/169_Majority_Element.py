#https://leetcode.com/problems/majority-element/
#Complexity: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)
        dict={}
        for i in range(l):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1
        for i in dict:
            if dict[i]>l/2:
                result=i
        return result
