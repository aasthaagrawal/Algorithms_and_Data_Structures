#https://leetcode.com/problems/longest-repeating-substring/
#Time Complexity: O(n^2)

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        self.result = 0
        n = len(s)
        for i in range(n-1):
            self.prefixArr(s[i:])
        return self.result
    
    def prefixArr(self,s):
        n = len(s)
        prefix = [0]*n
        i,j = 1,0
        while i<n:
            if s[i] == s[j]:
                j += 1
                prefix[i] = j
                i += 1
                self.result = max(self.result,j)
            elif j==0:
                prefix[i] = 0
                i += 1
            else:
                j = prefix[j-1]
