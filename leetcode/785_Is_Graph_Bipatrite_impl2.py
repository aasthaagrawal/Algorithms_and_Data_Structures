#https://leetcode.com/problems/is-graph-bipartite/
#Space Complexity: O(V)
#Time Complexity: O(V+E)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n =len(graph)
        node_class = [None]*n
        visited = [False]*n

        for i in range(n):
            if not visited[i]:
                queue = [i]
                node_class[i] = 0
                while queue:
                    node = queue.pop(0)
                    visited[node] = True
                    class_to_assign = (node_class[node]+1)%2
                    for neighbour in graph[node]:
                        if not visited[neighbour]:
                            queue.append(neighbour)
                            node_class[neighbour] = class_to_assign
                        elif class_to_assign!=node_class[neighbour]:
                            return False
        return True
