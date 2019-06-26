#https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rRow=[1]
        pRow=[]*0
        for i in range(1,rowIndex+1):
            pRow=rRow.copy()
            rRow=[]*(i+1)
            for j in range(i+1):
                if j==0 or j==i:
                    rRow.append(1)
                else:
                    rRow.append(pRow[j-1]+pRow[j])
        return rRow
