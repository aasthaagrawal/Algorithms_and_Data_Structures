#https://leetcode.com/problems/redundant-connection/
#Uses Union-find along with path compression

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.par={}
        for u,v in edges:
            if u not in self.par:
                self.par[u]=u
            if v not in self.par:
                self.par[v]=v
        red=[]
        for u,v in edges:
            if self.par[u]==self.par[v]:
                red.append([u,v])
            else:
                if self.par[u]<self.par[v]:
                    self.changepar(self.par[v],self.par[u])
                else:
                    self.changepar(self.par[u],self.par[v])
        return red[-1]
        
    def changepar(self,pi,pf):
        for key,val in self.par.items():
            if val==pi:
                self.par[key]=pf
