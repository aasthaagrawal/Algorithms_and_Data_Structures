#https://leetcode.com/problems/decoded-string-at-index/
#Time limit exceeded

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        curTape = []
        for s in S:
            if 47<ord(s)<58:
                curTape *= int(s)
            else:
                curTape.append(s)
        return curTape[K-1]
