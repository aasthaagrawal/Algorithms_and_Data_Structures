#https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        numRows=len(grid)
        numCols=len(grid[0])
        dp=[[0 for j in range(numCols)] for i in range(numRows)]
        print(dp)
        for i in range(numRows):
            for j in range(numCols):
                if i==0:
                    if j==0:
                        dp[i][j]=grid[i][j]
                    else:
                        dp[i][j]=grid[i][j]+dp[i][j-1]
                elif j==0:
                    dp[i][j]=dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j]=grid[i][j]+min(dp[i][j-1],dp[i-1][j])
                    
        
        return dp[-1][-1]
