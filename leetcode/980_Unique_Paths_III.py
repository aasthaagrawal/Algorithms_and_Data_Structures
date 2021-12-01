#https://leetcode.com/problems/unique-paths-iii/
#Time Complexity: O(3^N)

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.numZeroes = 0
        self.r = len(grid)
        self.c = len(grid[0])
        self.end = []
        self.start = []
        self.result = 0
        self.grid = grid
        for i in range(self.r):
            for j in range(self.c):
                if self.grid[i][j] == 0:
                    self.numZeroes += 1
                elif self.grid[i][j] == 1:
                    self.start = [i,j]
                elif self.grid[i][j] == 2:
                    self.end = [i,j]
        self.backtrack(-1,self.start[0],self.start[1])
        return self.result

    def findNextCell(self, i, j):
        pat = [[0,-1], [-1,0], [1,0], [0,1]]
        res = []
        for aux_i, aux_j in pat:
            next_i = i + aux_i
            next_j = j + aux_j
            if 0<= next_i <self.r and 0<= next_j < self.c and self.grid[next_i][next_j] in {0,2}:
                res.append([next_i,next_j])
        return res

    def backtrack(self, numZeroes, i, j):
        if self.end[0] == i and self.end[1] == j:
            if self.numZeroes == numZeroes:
                self.result += 1
            return
        self.grid[i][j] = 1
        for next_i, next_j in self.findNextCell(i,j):
            self.backtrack(numZeroes+1, next_i, next_j)
        self.grid[i][j] = 0
