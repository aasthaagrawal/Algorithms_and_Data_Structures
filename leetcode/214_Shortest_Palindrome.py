#https://leetcode.com/problems/shortest-palindrome/
#Used prefix table of KMP algorithm
#Space complexity: O(n) where n is the length of s
#Time complexity: O(n)

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        aux_s = s + "#" + ''.join(reversed(s))
        m = len(aux_s)
        pt = [0]*m
        i = 1
        j = 0
        while i<m:
            if aux_s[i]==aux_s[j]:
                j += 1
                pt[i] = j
                i += 1
            elif j==0:
                i += 1
            else:
                j = pt[j-1]
        return ''.join(reversed(s[pt[-1]:])) + s
