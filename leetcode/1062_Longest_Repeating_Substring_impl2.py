#https://leetcode.com/problems/longest-repeating-substring/
#Time Complexity: O(N^2) in worst case and O(NlogN) in average case
#Space Complexity: O(N^2)

class Solution:
    def searchDuplicateString(self, L, n, s):
        seen = set()
        for i in range(n-L+1):
            if s[i:i+L] in seen:
                return True
            seen.add(s[i:i+L])
        return False

    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = n
        while left <= right:
            L = left + (right-left)//2
            if self.searchDuplicateString(L, n, s):
                left = L+1
            else:
                right = L-1
        return left - 1
