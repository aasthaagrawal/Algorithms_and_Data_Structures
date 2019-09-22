#https://leetcode.com/problems/reverse-bits/
#Compexity: O(1)

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res=0
        for i in range(32):
            res=res<<1
            if n&1==1:
                res=res^1
            n=n>>1
        return res
