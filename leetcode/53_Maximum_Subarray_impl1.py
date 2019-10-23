#https://leetcode.com/problems/maximum-subarray/
#Complexity: O(n) both time and space complexity

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        result=dp[0]
        for i in range(1,n):
            dp[i]=max(nums[i],nums[i]+dp[i-1])
            result=max(result,dp[i])
        return result
