#https://leetcode.com/problems/uncrossed-lines/
#Complexity: O(rc)

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        r = len(nums1)+1
        c = len(nums2)+1
        dp = [[0 for j in range(c)] for i in range(r)]
        
        for i in range(r):
            dp[i][0]=0
        for j in range(c):
            dp[0][j]=0
        
        for i in range(1,r):
            for j in range(1,c):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
