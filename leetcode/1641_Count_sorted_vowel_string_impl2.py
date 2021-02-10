#https://leetcode.com/problems/count-sorted-vowel-strings/
#Time Complexity: O(6n)
#Space Complexity: O(6n)

class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0 for j in range(6)] for i in range(n)]
        for j in range(6):
            dp[0][j] = j
        for i in range(1,n):
            for j in range(1,6):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[n-1][5]
