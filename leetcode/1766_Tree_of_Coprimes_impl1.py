#https://leetcode.com/problems/tree-of-coprimes/
#Time limit exceeds

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
        self.dfs(0,-1,[])
        return self.gcd

    def dfs(self, node, par, pathStack):
        countChild = 0
        st = deepcopy(pathStack)
        res = None
        while st:
            top = st.pop()
            if gcd(self.nums[top],self.nums[node]) == 1:
                self.gcd[node] = top
                break
        del st
        pathStack.append(node)
        for child in self.tree[node]:
            if child!=par:
                countChild += 1
                self.dfs(child,node,pathStack)
        pathStack.pop()

