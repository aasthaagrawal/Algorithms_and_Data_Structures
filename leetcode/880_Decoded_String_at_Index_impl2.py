#https://leetcode.com/problems/decoded-string-at-index/
#Time complexity: O(n)
#Space complexity: O(1)

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        for s in S:
            if s.isdigit():
                size *= int(s)
            else:
                size += 1
        
        for s in reversed(S):
            K %= size
            if K==0 and s.isalpha():
                return s
            if s.isdigit():
                size /= int(s)
            else:
                size -= 1
