#https://leetcode.com/problems/reconstruct-itinerary/
#Space Complexity: O(E + V^2)
#Time Complexity: O(VE + log V)

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        nodes = set()
        for u,v in tickets:
            nodes.add(u)
            nodes.add(v)
        node_to_index = {}
        index_to_node = {}
        nodes = sorted(nodes)
        self.n = len(nodes)
        for i in range(self.n):
            node_to_index[nodes[i]] = i
            index_to_node[i] = nodes[i]

        self.e = len(tickets)
        self.result = []
        self.graph = [[0 for j in range(self.n)] for i in range(self.n)]
        for u,v in tickets:
            u = node_to_index[u]
            v = node_to_index[v]
            self.graph[u][v] += 1

        self.dfs(node_to_index["JFK"],0)
        itinerary = []
        for node in self.result:
            itinerary.append(index_to_node[node])
        return itinerary

    def dfs(self, node, edges_covered):
        self.result.append(node)
        for v in range(self.n):
            if self.graph[node][v] > 0:
                self.graph[node][v] -= 1
                if self.dfs(v,edges_covered+1):
                    return True
                self.graph[node][v] += 1
        if edges_covered == self.e:
            return True
        self.result.pop()
        return False
