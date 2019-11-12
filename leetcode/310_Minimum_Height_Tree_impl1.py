#https://leetcode.com/problems/minimum-height-trees/
#Time limit exceeds

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        self.ed={}
        for edge in edges:
            if edge[0] in self.ed:
                self.ed[edge[0]].append(edge[1])
            else:
                self.ed[edge[0]]=[edge[1]]
            if edge[1] in self.ed:
                self.ed[edge[1]].append(edge[0])
            else:
                self.ed[edge[1]]=[edge[0]]
                
        minheight=float("inf")
        minheightroot=None
        for i in range(n):
            visited=[False for i in range(n)]
            #visited[i]=True
            height=self.heightoftree(i,visited)
            if height<minheight:
                minheight=height
                minheightroot=[i]
            elif height==minheight:
                minheightroot.append(i)
        return minheightroot

    def heightoftree(self,root,visited):
        visited[root]=True
        h=0
        if root in self.ed:
            for j in self.ed[root]:
                if visited[j]==False:
                    h=max(h,self.heightoftree(j,visited)+1)
        return h
