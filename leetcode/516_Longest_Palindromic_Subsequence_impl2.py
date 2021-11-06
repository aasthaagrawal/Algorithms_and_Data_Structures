#https://leetcode.com/problems/longest-palindromic-subsequence/
#Time Complexity: O(n^2)

class Solution:
    from functools import lru_cache
    def longestPalindromeSubseq(self, s: str) -> int:

        @lru_cache(None)
        def dp(i,j):
            if i==j:
                return 1
            if i>j:
                return 0
            if s[i] == s[j]:
                return 2 + dp(i+1,j-1)
            else:
                return max(dp(i+1,j),dp(i,j-1))

        return dp(0,len(s)-1)
