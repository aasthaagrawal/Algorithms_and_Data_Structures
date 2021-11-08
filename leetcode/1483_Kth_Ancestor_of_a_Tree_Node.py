#https://leetcode.com/problems/kth-ancestor-of-a-tree-node/
#Time Complexity: O(nlogn) for init
#Space Complexity: O(nlogn)

class TreeAncestor:
    import math
    def __init__(self, n: int, parent: List[int]):
        self.n = n
        self.parent = parent
        self.max_j = int(math.log2(n)) + 1
        self.st = [[-1 for j in range(self.max_j)] for i in range(n)]
        for i in range(n):
            self.st[i][0] = self.parent[i]

        for j in range(1,self.max_j):
            for i in range(n):
                if self.st[i][j-1]>=0:
                    self.st[i][j] = self.st[self.st[i][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        k_j = int(math.log2(k))
        if k_j >= self.max_j:
            return -1
        while k>0:
            node = self.st[node][k_j]
            k -= (1<<k_j)
            if k == 0 or node == -1:
                break
            k_j = int(math.log2(k))
        return node



# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
