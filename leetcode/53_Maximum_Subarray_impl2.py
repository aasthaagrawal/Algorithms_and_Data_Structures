#https://leetcode.com/problems/maximum-subarray/
#Complexity: O(n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result=nums[0]
        curSum=nums[0]
        for i in range(1,len(nums)):
            curSum+=nums[i]
            if curSum<nums[i]:
                curSum=nums[i]
            result=max(result,curSum)
        return result
