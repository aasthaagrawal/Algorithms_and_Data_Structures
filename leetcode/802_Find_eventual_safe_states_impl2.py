#https://leetcode.com/problems/find-eventual-safe-states/
#Spack Complexity: O(V)
#Time Complexity: O(V+E)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        numNodes = len(graph)
        WHITE, GRAY, BLACK = 0,1,2
        colourDict = {i:WHITE for i in range(numNodes)}
        
        def dfs(node):
            if colourDict[node]==GRAY:
                return False
            colourDict[node] = GRAY
            for i in graph[node]:
                if colourDict[i] == BLACK:
                    continue
                if colourDict[i] == GRAY or not dfs(i):
                    return False
            colourDict[node] = BLACK
            return True
        
        return filter(dfs, range(numNodes))
