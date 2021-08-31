#https://leetcode.com/problems/delete-operation-for-two-strings/
#Time Complexity = O(rc)
#Space Complexity = O(rc)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        r = len(word1)+1
        c = len(word2)+1
        
        dp = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            dp[i][0] = i
        for j in range(c):
            dp[0][j] = j
        
        for i in range(1,r):
            for j in range(1,c):
                dp[i][j] = dp[i-1][j-1] if word1[i-1]==word2[j-1] else 1+min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
