#https://leetcode.com/problems/find-if-path-exists-in-graph/
#Space Complexity: O(V + E) where V is the number of vertices and E is the number of edges
#Time complexity: O(E + V)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        self.adj_list = {i:[i] for i in range(n)}
        for edge in edges:
            self.adj_list[edge[0]].append(edge[1])
            self.adj_list[edge[1]].append(edge[0])
        self.visited = [False]*n
        self.end = end
        return self.dfs(start)

    def dfs(self, node):
        self.visited[node] = True
        for i in self.adj_list[node]:
            if i == self.end:
                return True
            if not self.visited[i]:
                res = self.dfs(i)
                if res:
                    return res
        return False
