#https://leetcode.com/problems/number-of-islands/
#Complexity: 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if grid[i][j]=='0' or visited[i][j]:
                return
            visited[i][j]=True
            if i+1<numRows:
                dfs(i+1,j)
            if j+1<numCols:
                dfs(i,j+1)
            if j-1>=0:
                dfs(i,j-1)
            if i-1>=0:
                dfs(i-1,j)

        numRows=len(grid)
        if numRows==0:
            return 0
        numCols=len(grid[0])
        numIsl=0
        visited=[[False for j in range(numCols)] for i in range(numRows)]
        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j]=='1' and not visited[i][j]:
                    numIsl+=1
                    dfs(i,j)
            
        return numIsl
