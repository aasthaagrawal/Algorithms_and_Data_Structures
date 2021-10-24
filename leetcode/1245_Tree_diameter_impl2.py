#https://leetcode.com/problems/tree-diameter/
#Time Complexity: O(V+E)

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        self.tree = defaultdict(list)
        for u,v in edges:
            self.tree[u].append(v)
            self.tree[v].append(u)

        self.result = 0
        self.dfs(0, None)
        return self.result

    def dfs(self, node, parent):
        countChild = 0
        pathLens = []
        for child in self.tree[node]:
            if child != parent:
                countChild += 1
                pathLens.append(self.dfs(child, node))
        if countChild == 0:
            return 1
        if len(pathLens) == 1:
            if self.result < pathLens[0]:
                self.result = pathLens[0]
            return pathLens[0] + 1

        maxLen = max(pathLens)
        pathLens.remove(maxLen)
        secondMaxLen = max(pathLens)
        if self.result < maxLen+secondMaxLen:
            self.result = maxLen+secondMaxLen
        return maxLen + 1
