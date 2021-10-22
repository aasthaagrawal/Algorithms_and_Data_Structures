#https://leetcode.com/problems/path-with-maximum-gold/
#Space Complexity: O(mn)
#Time Complexity: O(mn(4^(mn))) 

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.r = len(grid)
        self.c = len(grid[0])
        self.grid = grid
        self.patterns = [[0,-1], [0,1],[-1,0],[1,0]]
        self.result = 0
        self.visited = [[False for j in range(self.c)] for i in range(self.r)]
        for i in range(self.r):
            for j in range(self.c):
                if self.grid[i][j]==0:
                    self.visited[i][j] = True
        for i in range(self.r):
            for j in range(self.c):
                if not self.visited[i][j]:
                    self.getGoldAmount(i,j,0)
        return self.result

    def getGoldAmount(self, cur_i, cur_j, curSum):
        self.visited[cur_i][cur_j] = True
        curSum += self.grid[cur_i][cur_j]
        numRoutesPossible = 0
        for pat in self.patterns:
            new_i = cur_i+pat[0]
            new_j = cur_j+pat[1]
            if 0 <= new_i < self.r and 0 <= new_j < self.c and not self.visited[new_i][new_j]:
                numRoutesPossible += 1
                self.getGoldAmount(new_i,new_j,curSum)

        if numRoutesPossible==0:
            self.result = max(self.result, curSum)
        self.visited[cur_i][cur_j] = False
        curSum -= self.grid[cur_i][cur_j]
