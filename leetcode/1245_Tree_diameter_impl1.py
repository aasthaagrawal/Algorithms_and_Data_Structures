#https://leetcode.com/problems/tree-diameter/
#Time limit exceeds
#Time Complexity: O(V(V+E))

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        #tree construction
        self.tree = {}
        for edge in edges:
            if edge[0] not in self.tree:
                self.tree[edge[0]] = [edge[1]]
            else:
                self.tree[edge[0]].append(edge[1])
            if edge[1] not in self.tree:
                self.tree[edge[1]] = [edge[0]]
            else:
                self.tree[edge[1]].append(edge[0])

        V = len(self.tree)
        self.result = 0
        for v in range(V):
            visited = [False for i in range(V)]
            self.dfs(v, visited, 0)
        return self.result

    def dfs(self, node, visited, pathLen):
        visited[node] = True
        if pathLen > self.result:
            self.result = pathLen
        for child in self.tree[node]:
            if not visited[child]:
                self.dfs(child, visited, pathLen+1)
