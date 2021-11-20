#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#Time complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        start, end = 0, 0
        res = 0
        d = {}
        while end < n:
            if s[end] in d:
                start = max(d[s[end]],start)
            d[s[end]] = end + 1
            res = max(res, end-start+1)
            end += 1
        return res
