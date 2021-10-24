#https://leetcode.com/problems/map-of-highest-peak/
#Time Complexity = O(mn)

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        self.r = len(isWater)
        self.c = len(isWater[0])
        pat = [[-1,0], [1,0], [0,-1], [0,1]]
        height = [[None for j in range(self.c)] for i in range(self.r)]
        curQ = []

        for i in range(self.r):
            for j in range(self.c):
                if isWater[i][j]==1:
                    height[i][j] = 0
                    curQ.append((i,j))
        level = 1
        nextQ = []
        while curQ:
            while curQ:
                i,j = curQ.pop()
                for pat_r, pat_c in pat:
                    new_i, new_j = pat_r+i, pat_c+j
                    if self.isSafe(new_i,new_j) and height[new_i][new_j]==None:
                        height[new_i][new_j] = level
                        nextQ.append((new_i,new_j))
            level += 1
            curQ = nextQ
            nextQ = []
        return height

    def isSafe(self, i, j):
        if 0 <= i < self.r and 0 <= j < self.c:
            return True
        return False
