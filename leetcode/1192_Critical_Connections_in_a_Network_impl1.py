#https://leetcode.com/problems/critical-connections-in-a-network/
#Time Complexity: O(V+E)
#Space Complexity: O(V+E)

class Solution:
    from collections import defaultdict
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.visited = [False]*n
        self.low_time = [float("inf")]*n
        self.time = 0
        self.discovery_time = [float("inf")]*n
        self.parent = [-1]*n
        self.graph = defaultdict(list)
        self.result = []

        for u,v in connections:
            self.graph[u].append(v)
            self.graph[v].append(u)

        for node in range(n):
            if not self.visited[node]:
                self.dfs(node)

        return self.result

    def dfs(self, cur_node):
        self.visited[cur_node] = True
        self.discovery_time[cur_node] = self.time
        self.low_time[cur_node] = self.time
        self.time += 1
        for node in self.graph[cur_node]:
            if not self.visited[node]:
                self.parent[node] = cur_node
                self.dfs(node)
                self.low_time[cur_node] = min(self.low_time[cur_node],self.low_time[node])
            elif node != self.parent[cur_node]:
                self.low_time[cur_node] = min(self.low_time[cur_node], self.discovery_time[node])

        if self.low_time[cur_node] == self.discovery_time[cur_node] and self.parent[cur_node] != -1:
            self.result.append([cur_node,self.parent[cur_node]])
