#https://leetcode.com/problems/friend-circles/

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n=len(M)
        self.par=[i for i in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                if M[i][j]==1 and self.par[i]!=self.par[j]:
                    self.union(i,j,n)
        res=set()
        count=0
        for i in self.par:
            if i not in res:
                res.add(i)
                count+=1
        return count
    
    def union(self,i,j,n):
        if self.par[i]<self.par[j]:
            val=self.par[j]
            for x in range(n):
                if self.par[x]==val:
                    self.par[x]=self.par[i]
        else:
            val=self.par[i]
            for x in range(n):
                if self.par[x]==val:
                    self.par[x]=self.par[j]
