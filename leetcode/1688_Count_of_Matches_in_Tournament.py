#https://leetcode.com/problems/count-of-matches-in-tournament/
#Time Complexity: O(log n)

class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        if n%2==0:
            return n//2 + self.numberOfMatches(n//2)
        else:
            return (n-1)//2 + self.numberOfMatches(1 + ((n-1)//2))
