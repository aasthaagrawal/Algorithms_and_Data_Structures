#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#Time Complexity: O(n)

class Solution:
    from collections import defaultdict
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0
        start, end, res = 0, 0, 0
        d = defaultdict(int)
        while end < n:
            d[s[end]] += 1
            while d[s[end]] > 1:
                d[s[start]] -= 1
                start += 1
            res = max(res, end-start+1)
            end += 1
        return res
