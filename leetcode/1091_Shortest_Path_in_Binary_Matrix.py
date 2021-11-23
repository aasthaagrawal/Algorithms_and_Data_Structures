#https://leetcode.com/problems/shortest-path-in-binary-matrix/
#Time Complexity: O(N)

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pattern = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

        def isValid(i,j):
            if 0<=i<n and 0<=j<n and grid[i][j]==0:
                return True
            return False

        def getNeighbours(i,j):
            l = []
            for pi,pj in pattern:
                child_i, child_j = i+pi, j+pj
                if isValid(child_i, child_j) and not visited[child_i][child_j]:
                    l.append([child_i,child_j])
                    visited[child_i][child_j] = True
            return l

        visited = [[False for j in range(n)] for i in range(n)]
        q = []
        if grid[0][0] == 0:
            q = [[0,0]]
        next_q = []
        pathLen = 0
        while q:
            pathLen += 1
            while q:
                i,j = q.pop(0)
                if i==n-1 and j==n-1:
                    return pathLen
                for child_i, child_j in getNeighbours(i,j):
                    next_q.append([child_i,child_j])
            q = next_q
            next_q = []
        return -1
