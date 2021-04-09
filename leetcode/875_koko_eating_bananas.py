#https://leetcode.com/problems/koko-eating-bananas/
#O(nlog w) where w = max(piles) and n = len(piles)

class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.h = h
        return self.bin_search(1, max(self.piles))
    
    def bin_search(self,a,b):
        if a==b:
            return a
        mid = a + (b-a)//2
        if sum(math.ceil(p/mid) for p in self.piles)<=self.h:
            return self.bin_search(a,mid)
        else:
            return self.bin_search(mid+1,b)
