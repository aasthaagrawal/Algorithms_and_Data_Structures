#https://leetcode.com/problems/parallel-courses/
#Using DFS based Topological sort

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        self.graph = {i:[] for i in range(n)}
        for prevC, nextC in relations:
            self.graph[prevC-1].append(nextC-1)

        self.visited, self.recStack, self.minSemArr, minSem = [False]*n, [False]*n, [None]*n, 0
        for node in range(n):
            if not self.visited[node]:
                res = self.dfs(node)
                if res == -1:
                    return -1
                minSem = max(minSem, res)
        return minSem

    def dfs(self, node):
        self.visited[node] = True
        self.recStack[node] = True
        childSem = 0
        for child in self.graph[node]:
            if self.recStack[child] == True:
                return -1
            if not self.visited[child]:
                res = self.dfs(child)
                if res == -1:
                    return -1
            childSem = max(self.minSemArr[child], childSem)
        self.recStack[node] = False
        self.minSemArr[node] = childSem + 1
        return self.minSemArr[node]

