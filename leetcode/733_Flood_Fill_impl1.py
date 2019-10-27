#https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        moves=[[-1,0],[0,-1],[0,1],[1,0]]
        lenR=len(image)
        lenC=len(image[0])
        visited=[[False for j in range(lenC)] for i in range(lenR)]
        initialColour=image[sr][sc]
        
        def dfs(pR,pC):
            if pR<0 or pR>=lenR or pC<0 or pC>=lenC or visited[pR][pC] or image[pR][pC]!=initialColour:
                return
            visited[pR][pC]=True
            image[pR][pC]=newColor
            for i in range(4):
                dfs(pR+moves[i][0],pC+moves[i][1]) 
                
        dfs(sr,sc)
        return image
