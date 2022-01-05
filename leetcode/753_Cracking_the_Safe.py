#https://leetcode.com/problems/cracking-the-safe/


class Solution:
    from itertools import product

    def crackSafe(self, n: int, k: int) -> str:
        if n==1:
            return "".join([str(i) for i in range(k)])

        #creating graph
        self.adj_list = {}
        nodes = ["".join([str(c) for c in cp]) for cp in product(range(k), repeat=n-1)]
        for node in nodes:
            self.adj_list[node] = [node[1:] + str(i) for i in range(k)]

        #Hierholzer's algo
        start = '0'*(n-1)
        self.result = None
        self.totalEdges = k*len(self.adj_list)
        self.dfs(start, 0, start)
        return self.result

    def dfs(self, node, edgeCovered, path):
        if self.totalEdges == edgeCovered:
            self.result = path
            return True
        if len(self.adj_list[node])==0:
            return False
        neighbours = self.adj_list[node]
        for nextNode in neighbours:
            self.adj_list[node].remove(nextNode)
            if self.dfs(nextNode, edgeCovered+1, path+nextNode[-1]):
                return True
            self.adj_list[node].append(nextNode)
        return False
