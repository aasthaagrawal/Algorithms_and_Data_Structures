#https://leetcode.com/problems/all-paths-from-source-to-target/
#Time Complexity: O(2^N) as there are 2^(N-2) paths

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.n = len(graph)-1
        self.res = []
        self.graph = graph
        self.paths([0])
        return self.res
        
    def paths(self, path):
        last_node = path[-1]
        if last_node == self.n:
            self.res.append(path[:])
            return
        for node in self.graph[last_node]:
            path.append(node)
            self.paths(path)
            path.pop()
