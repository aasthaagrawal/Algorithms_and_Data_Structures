#https://leetcode.com/problems/partition-array-for-maximum-sum/
#Complexity:O(nK)

class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n=len(A)
        dp=[-float("inf") for i in range(n)]
        for i in range(K):
            dp[i]=(i+1)*max(A[:i+1])
        for i in range(K,n):
            for j in range(K):
                dp[i]=max(dp[i],dp[i-j-1]+(j+1)*max(A[i-j:i+1]))
        return dp[n-1]
