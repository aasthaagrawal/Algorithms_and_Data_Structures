#https://leetcode.com/problems/find-if-path-exists-in-graph/
#Space Complexity: O(V + E)
#Time Complexity: O(E + V)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        self.adj_list = {i:[i] for i in range(n)}
        for edge in edges:
            self.adj_list[edge[0]].append(edge[1])
            self.adj_list[edge[1]].append(edge[0])
        return self.bfs(start, end, n)
    
    def bfs(self, start, end, n):
        visited = [False]*n
        queue = [start]
        while queue:
            node = queue.pop(0)
            visited[node] = True
            for neighbour in self.adj_list[node]:
                if neighbour == end:
                    return True
                if not visited[neighbour]:
                    queue.append(neighbour)
        return False
