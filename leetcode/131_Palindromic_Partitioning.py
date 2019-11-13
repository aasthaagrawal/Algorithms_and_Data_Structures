#https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result=[]
        self.s=s
        self.n=len(s)
        self.util(0,[])
        return self.result
        
    def util(self,index,parts):
        if index==self.n:
            self.result.append(parts[:])
            return
        for i in range(index,self.n):
            tmp=self.s[index:i+1]
            if tmp==tmp[::-1]:
                parts.append(self.s[index:i+1])
                self.util(i+1,parts)
                parts.pop(-1)
    
    def ispalindrome(self,s):
        return s==s[::-1]
