#https://leetcode.com/problems/is-graph-bipartite/
#Complexity: O(n*len(graph[d])

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d={}
        
        def util(node,prev,toggle):
            if node in d:
                if d[node]==prev:
                    return False
            else:
                setnum=-1
                if toggle:
                    setnum=prev+1
                else:
                    setnum=prev-1
                d[node]=setnum
                toggle=not toggle
                for j in graph[node]: 
                    res=util(j,setnum,toggle)
                    if res==False:
                        return False
            return True
        
        res=True
        for i in range(len(graph)):
            if i not in d:
                res=util(i,-1,True)
                if res==False:
                    break
        return res
