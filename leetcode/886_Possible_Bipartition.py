#https://leetcode.com/problems/possible-bipartition/

class Solution:
    from collections import defaultdict
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        n += 1
        self.class_arr = [-1 for i in range(n)]

        self.graph = defaultdict(list)
        for i,j in dislikes:
            self.graph[i].append(j)
            self.graph[j].append(i)

        for i in range(1,n):
            if self.class_arr[i] == -1:
                self.class_arr[i] = 0
                if self.bfs(i) == False:
                    return False
        return True

    def bfs(self,node):
        q = [node]
        while q:
            node = q.pop(0)
            child_class = self.class_arr[node]^1
            for child in self.graph[node]:
                if self.class_arr[child] == self.class_arr[node]:
                    return False
                if self.class_arr[child] == -1:
                    self.class_arr[child] = child_class
                    q.append(child)
        return True
