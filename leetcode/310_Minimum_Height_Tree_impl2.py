#https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==0:
            return []
        elif n==1:
            return [0]
        ed={}
        dd={}
        for edge in edges:
            if edge[0] in ed:
                ed[edge[0]].append(edge[1])
                dd[edge[0]]+=1
            else:
                ed[edge[0]]=[edge[1]]
                dd[edge[0]]=1
            if edge[1] in ed:
                ed[edge[1]].append(edge[0])
                dd[edge[1]]+=1
            else:
                ed[edge[1]]=[edge[0]]
                dd[edge[1]]=1
        q=[]
        for i in range(n):
            if dd[i]==1:
                q.append(i)
        while n>2:
            ql=len(q)
            for i in range(ql):
                v=q.pop(0)
                n-=1
                for j in ed[v]:
                    dd[j]-=1
                    if dd[j]==1:
                        q.append(j)
        result=[]
        while len(q):
            result.append(q.pop(0))
        return result
