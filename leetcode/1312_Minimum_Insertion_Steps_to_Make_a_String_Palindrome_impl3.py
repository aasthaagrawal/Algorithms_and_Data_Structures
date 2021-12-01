#https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
#Time complexity: O(n^2)
#Space complexity: O(n^2)

class Solution:
    from functools import lru_cache
    
    def minInsertions(self, s: str) -> int:
        self.s = s
        return self.util(0, len(s)-1)
    
    @lru_cache(None)
    def util(self, i, j):
        if j-i <= 0:
            return 0
        if self.s[i] == self.s[j]:
            return 0 + self.util(i+1, j-1)
        return 1 + min(self.util(i+1, j), self.util(i, j-1))
