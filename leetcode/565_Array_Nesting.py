#https://leetcode.com/problems/array-nesting/

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        self.nums, self.res, n = nums, 1, len(nums)
        self.visited = [False]*n
        for i in range(n):
            if not self.visited[nums[i]]:
                self.dfs(self.nums[i], 0)
        return self.res

    def dfs(self, node, l):
        if self.visited[node]:
            self.res = max(self.res, l)
            return
        self.visited[node] = True
        self.dfs(self.nums[node], l+1)
