#https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        dp=[1 for i in range(n)]
        result=1
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i] and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
            result=max(result,dp[i])
        return result
