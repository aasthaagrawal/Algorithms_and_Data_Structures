#https://leetcode.com/problems/frog-position-after-t-seconds/

from collections import defaultdict

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        #get adjacency list format
        self.graph = defaultdict(list)
        for u,v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.target = target
        self.res = 0
        self.dfs(1, -1, 1, t)
        return self.res

    def dfs(self, node, parent, prob, t):
        #print(node, prob)
        if t < 0:
            return
        count = len(self.graph[node]) -1
        if parent == -1:
            count += 1
        if node == self.target:
            if count == 0 or t == 0:
                self.res = prob
            return
        if count == 0:
            return
        prob /= count
        for child in self.graph[node]:
            if child != parent:
                self.dfs(child, node, prob, t-1)
