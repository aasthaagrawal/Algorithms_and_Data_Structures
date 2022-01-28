#https://leetcode.com/problems/evaluate-division/

from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = defaultdict(list)
        for ind,(u,v) in enumerate(equations):
            self.graph[u].append((v,values[ind]))
            self.graph[v].append((u,1/values[ind]))

        res = [-1.0]*len(queries)
        for ind,(u,v) in enumerate(queries):
            if u in self.graph:
                visited = {key: False for key in self.graph}
                res[ind] = self.dfs(u, v, visited, 1)
        return res

    def dfs(self, node, target, visited, prod):
        if node == target:
            return prod
        visited[node] = True
        for child, weight in self.graph[node]:
            if not visited[child]:
                val = self.dfs(child, target, visited, prod*weight)
                if val != -1:
                    return val
        return -1
