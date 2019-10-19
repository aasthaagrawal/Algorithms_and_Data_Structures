#https://leetcode.com/problems/delete-columns-to-make-sorted/
#Complexity: O(nm)

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        numRows=len(A)
        if numRows<2:
            return 0
        
        numCols=len(A[0])
        result=0
        for j in range(numCols):
            for i in range(numRows-1):
                if A[i][j]>A[i+1][j]:
                    result+=1
                    break
        return result
