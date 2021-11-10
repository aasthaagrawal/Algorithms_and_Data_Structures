#https://leetcode.com/problems/tree-of-coprimes/submissions/

class Solution:
    from collections import defaultdict
    from copy import deepcopy
    from math import gcd

    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        self.tree = defaultdict(list)
        self.nums = nums
        for u,v in edges:
            self.tree[u].append(v)
            self.tree[v].append(u)
        self.gcd = [-1]*len(nums)

        self.dp = [[False for j in range(51)] for i in range(51)]
        for i in range(1,51):
            for j in range(1,51):
                if gcd(i,j) == 1:
                    self.dp[i][j]= True

        self.path = defaultdict(list)

        self.dfs(0, None, 0)
        return self.gcd

    def dfs(self, node, par, depth):
        node_val = self.nums[node]
        largestDepth = -1
        for i in range(1,51):
            if self.dp[node_val][i]:
                if self.path[i]:
                    topNode, topDepth = self.path[i][-1]
                    if topDepth>largestDepth:
                        largestDepth = topDepth
                        self.gcd[node] = topNode
        self.path[node_val].append((node,depth))
        for child in self.tree[node]:
            if child != par:
                self.dfs(child, node, depth+1)
        self.path[node_val].pop()
