#https://leetcode.com/problems/edit-distance/
#Complexity: O(mn)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        auxMat=[[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if j==0:
                    auxMat[i][j]=i
                elif i==0:
                    auxMat[i][j]=j
                elif word2[i-1]==word1[j-1]:
                    auxMat[i][j]=auxMat[i-1][j-1]
                else:
                    auxMat[i][j]=1+min(auxMat[i-1][j-1],auxMat[i-1][j],auxMat[i][j-1])
        return auxMat[n][m]
