#https://leetcode.com/problems/generate-parentheses/
#Complexity: O(2^n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.n = n
        self.util(0,0,"")
        return self.result
        
    def util(self, n_open, n_close, s):
        if n_open==self.n and n_close==self.n:
            self.result.append(s[:])
            return
        if n_open<self.n:
            self.util(n_open+1,n_close,s+"(")
        if n_close<n_open:
            self.util(n_open,n_close+1,s+")")
