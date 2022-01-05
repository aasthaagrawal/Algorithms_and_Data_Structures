#https://leetcode.com/problems/numbers-with-same-consecutive-differences/
#Time Complexity: O(2^n)
#Space Complexity: O(2^n)

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.result = []
        self.k = k
        self.n = n
        for i in range(9,0,-1):
            self.dfs(i,i,1)
        return self.result

    def dfs(self, i, cur, curLen):
        if curLen == self.n:
            self.result.append(cur)
            return
        nextDigits = {i+self.k, i-self.k}
        for nextDigit in {i+self.k, i-self.k}:
            if -1 < nextDigit < 10:
                self.dfs(nextDigit, cur*10+nextDigit, curLen+1)
